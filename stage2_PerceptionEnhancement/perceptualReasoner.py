import base64
import json 
from http import HTTPStatus
import os
import time
import torch
import requests
import PIL
from PIL import Image
from io import BytesIO
import chartTableP # prompts for perception stage

from llava.mm_utils import get_model_name_from_path
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from llava.conversation import conv_templates, SeparatorStyle
from llava.model.builder import load_pretrained_model
from llava.utils import disable_torch_init
from llava.mm_utils import tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria
seedd = 3407
torch.manual_seed(seedd)

import dashscope

import google.generativeai as genai
genai.configure(api_key='', transport='rest')

def getColTable(tablefrom, table_str, delimiter=' | '):
    table_rows = [row.strip() for row in table_str.replace('<0x0A>', '\n').split('\n') if row]
    if 'PlotQA' in tablefrom:
        title = table_rows[0].split(delimiter)[1]
        columns = table_rows[1].split(delimiter)
        data = []
        for row in table_rows[2:]:
            row_data = row.split(delimiter)
            entry = {col: val for col, val in zip(columns, row_data)}
            data.append(entry)
        return json.dumps(str({'title': title, 'columns': columns, 'data': data}))
    else:
        columns = table_rows[0].split(delimiter)
        data = []
        for row in table_rows[1:]:
            row_data = row.split(delimiter)
            entry = {col: val for col, val in zip(columns, row_data)}
            data.append(entry)
        return json.dumps(str({'columns': columns, 'data': data}))

def getinput(table_path, tablefrom, root_path):
    dict_table = {}
    with open(table_path, 'r') as f1:
       tables = json.load(f1)
       for item in tables:
          dict_table[item['imgname'].split('/')[-1]] = item['table']
    # list_dir = os.listdir(root_path)
    aa = []
    with open(root_path, 'r') as f2:
        data = json.load(f2)
        for item in data:
            tmp_imgname = item['imgname']
            if '\n\nAnswer' in item['subq']:
                subq = ""
            item22 = item['subq'].replace('\n\n', '\n')
            subq = item22.split('\n')
            aa.append({'imgid': tmp_imgname, 'question': item['question'], 'subq': subq, 'label': item['label'],
                       'table': getColTable(tablefrom, dict_table[item['imgname']])})
    return aa

def geminiV(inputs):
    generation_config = {"temperature": 0, "top_p": 0, "top_k": None}
    image = inputs['image']
    text = inputs['text']
    img = PIL.Image.open(image)
    processed_flag = False
    ii = 0
    while not processed_flag:
        try:
           model = genai.GenerativeModel('gemini-pro-vision', generation_config=generation_config)
           response = model.generate_content([text, img], stream=False)
           
           return response.text
        except Exception as e:
           if ii >= 8:
              res = f'wrong!!, {str(e)}; the image is: {image}'
              return res
        #    print(e)
           print('Error! Sleep for 5s.')
           ii += 1
           time.sleep(5)

def qwenVPlus(inputs):
    image = inputs['image']
    text = inputs['text']
    messages = [{"role": "user", "content": [{"image": 'file://' + image}, {"text": text}]}]
    processed_flag = False
    ii = 0
    while not processed_flag:
        try:
            response = dashscope.MultiModalConversation.call(model='qwen-vl-plus', messages=messages, top_p=0.001, top_k=1)
            if response.status_code == HTTPStatus.OK:
               res = response['output']['choices'][0]['message']['content'][0]['text']
            else:
               res = f'wrong!!, {e}; the image is: {image}'
            return res
        except Exception as e:
            if ii >= 5:
               res = f'wrong!!, {e}; the image is: {image}'
               return res
            ii += 1
            time.sleep(5)

def llava(tokenizer, model, image_processor, model_name, inputs):
    image_file = inputs['image']
    text_inputs = inputs['text']
    qs = text_inputs
    if model.config.mm_use_im_start_end:
        qs = DEFAULT_IM_START_TOKEN + DEFAULT_IMAGE_TOKEN + DEFAULT_IM_END_TOKEN + '\n' + qs
    else:
        qs = DEFAULT_IMAGE_TOKEN + '\n' + qs
    if 'llama-2' in model_name.lower():
        conv_mode = "llava_llama_2"
    elif "v1" in model_name.lower():
        conv_mode = "llava_v1"
    elif "mpt" in model_name.lower():
        conv_mode = "mpt"
    else:
        conv_mode = "llava_v0"
    conv = conv_templates[conv_mode].copy()
    conv.append_message(conv.roles[0], qs)
    conv.append_message(conv.roles[1], None)
    prompt = conv.get_prompt()

    input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).cuda()
    stop_str = conv.sep if conv.sep_style != SeparatorStyle.TWO else conv.sep2
    keywords = [stop_str]
    stopping_criteria = KeywordsStoppingCriteria(keywords, tokenizer, input_ids)

    if image_file.startswith('http') or image_file.startswith('https'):
        response = requests.get(image_file)
        image = Image.open(BytesIO(response.content)).convert('RGB')
    else:
        image = Image.open(image_file).convert('RGB')

    image_tensor = image_processor.preprocess(image, return_tensors='pt')['pixel_values'].half().cuda()
    with torch.inference_mode():
        try:
            output_ids = model.generate(input_ids, images=image_tensor, do_sample=True, temperature=0.001,
            max_new_tokens=1024, use_cache=True, stopping_criteria=[stopping_criteria])
        except Exception as e:
            return "wrong!!" + str(e)
    outputs = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0].strip()
    return outputs

def gpt4v(inputs):
    image = inputs['image']
    text = inputs['text']
    with open(image, "rb") as image_file:
        img_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    processed_flag = False

    api_key = ""
    url = "" # https://api.openai.com/v1/chat/completions
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4-turbo-2024-04-09",  # vision-preview
        "temperature": 0.0,
        "messages": [
            {"role": "system", "content": "you are an assistant"},
            {"role": "user", "content": [
                {"type":"text", "text": text},
                {"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{img_base64}"}}
                ]
            }
        ]
    }
    processed_flag = False
    while not processed_flag:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            processed_flag = False
            print(result)
            print(e)
            print('Error! Sleep for 5s.')
            time.sleep(5)
def multimodal_conversation_call(tokenizer, model, image_processor, model_name, inputs, MLLMs_type):
    if MLLMs_type == "geminiV":
        return geminiV(inputs)
    elif MLLMs_type == "qwenVPlus":
        return qwenVPlus(inputs)
    elif MLLMs_type == "llava":
        return llava(tokenizer, model, image_processor, model_name, inputs)
    elif MLLMs_type == "gpt4v":
        return gpt4v(inputs)
    else:
        return "unknow MLLM"

def run(table_path, tablefrom, subQsfile, res_split, img_root_path, LLMs_type, MLLMs_type):
    inputs = getinput(table_path, tablefrom, subQsfile)
    model_name = ""
    tokenizer=""
    model=""
    image_processor=""
    if MLLMs_type == "llava":
        model_path = "/models/llava-v1.5-13b"
        disable_torch_init()
        model_name = get_model_name_from_path(model_path)
        tokenizer, model, image_processor, context_len = load_pretrained_model(model_path=model_path, model_base=None, model_name=model_name)
    for item in inputs:
        tmp_imgname = item['imgid']
        img_path = os.path.join(img_root_path, tmp_imgname)
        tmp_table = item['table']
        tmp_question = item['question']
        tmp_subq = item['subq'] 
        tmp_label = item['label']
        cleaned_question = "".join(c for c in tmp_question if c.isalnum() or c in (' ', '_', '-'))
        filename = f"/res/2perceptual_{LLMs_type}subQ_{MLLMs_type}/{res_split}/[{tmp_imgname}]_{cleaned_question}.json"
        subqID = 0
        sub_response = []
        usingT = chartTableP # prompts for perception stage
        
        if len(tmp_subq) > 1:
            txt_input = usingT.template.format(tmp_table, tmp_subq[subqID].split(':', 1)[1])
        else:
            txt_input = usingT.final_0sub.format(tmp_table, tmp_question)
        test_input = {"image": img_path, "text": txt_input}
        if not os.path.exists(filename):
            if len(tmp_subq) > 1:
                history_subQApairs = ''
                response = None
                for subq_id in range(len(tmp_subq) - 1):
                    if subq_id == 0:
                        response = multimodal_conversation_call(tokenizer, model, image_processor, model_name, test_input, MLLMs_type)
                    else:
                        subqID += 1
                        txt_input = usingT.template.format(tmp_table, tmp_subq[subqID].split(':', 1)[1])
                        test_input = {"image": img_path, "text": txt_input}
                        response = multimodal_conversation_call(tokenizer, model, image_processor, model_name, test_input, MLLMs_type)
                    sub_response.append(response)
                    history_subQApairs += f'\nsub_q{subqID + 1}:{tmp_subq[subqID].split(":", 1)[1]}' + f'\nsub_ans{subqID+1}:' + response + '\n'
                final_txt_input = usingT.final_nsub.format(tmp_table, history_subQApairs, tmp_question)
                final_input = {"image": img_path, "text": final_txt_input}
                response_final = multimodal_conversation_call(tokenizer, model, image_processor, model_name, final_input, MLLMs_type)
            else:
                response_final = multimodal_conversation_call(tokenizer, model, image_processor, model_name, test_input, MLLMs_type)
            tmp_save = {"imgname": img_path, "table": tmp_table, "query": tmp_question, "sub_q": tmp_subq, "sub_res": sub_response, "response": response_final, "label": tmp_label}
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(tmp_save, json_file, ensure_ascii=False, indent=4)
if __name__ == '__main__':
    tablefrom = '' # ChartQA, PlotQA
    img_root_path = r''
    table_path = r''
    subQsfile = r'' # decomposer generates
    res_split = ""
    MLLMs_type = "" #  geminiV qwenVPlus llava gpt4v(not gpt-4-vision-preview)
    LLMs_type = "" # which decomposer generates the subquestions
    
    run(table_path=table_path, tablefrom=tablefrom, subQsfile=subQsfile, res_split=res_split, img_root_path=img_root_path, LLMs_type=LLMs_type, MLLMs_type=MLLMs_type)
