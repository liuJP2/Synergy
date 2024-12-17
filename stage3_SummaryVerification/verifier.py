import json 
import os
import time
import requests
from stage3_SummaryVerification import  _REFINE_9,_REFINE_1,_REFINE_3, _REFINE, _REFINE_12 # We organize the prompt into the prompt folder
from openai import OpenAI
import google.generativeai as genai

def llama3_8b(prompt):
    client = OpenAI(
        api_key="",
        base_url=""
    )
    processed_flag = False
    while not processed_flag:
        try:
            completion = client.chat.completions.create(
                model="llama3-8B-instruct",
                temperature=0.0001,
                top_p=0.0001,
                messages=[
                    {"role": "system", "content": "you are an assistant"},
                    {"role": "user", "content": prompt},
                ],
            )
            input_tokens = completion.usage.prompt_tokens
            output_tokens = completion.usage.completion_tokens
            response = completion.choices[0].message.content
            return  response,input_tokens,output_tokens
        except Exception as e:
            processed_flag = False
            print(e)
            print('Error! Sleep for 5s.')
            time.sleep(5)
            
def gpt4(prompt):
    api_key = ""
    url = "https://api.openai.com/v1/chat/completions" 
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4-1106-preview",
        "temperature": 0.0,
        "messages": [
            {"role": "system", "content": "you are an assistant"},
            {"role": "user", "content": prompt}
        ]
    }
    processed_flag = False
    while not processed_flag:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            result = response.json()
            generated_result = result["choices"][0]["message"]["content"]
            statistic = result
            return generated_result, statistic
        except Exception as e:
            processed_flag = False
            print(result)
            print(e)
            print('Error! Sleep for 5s.')
            time.sleep(5)

def gemini(prompt):
    generation_config = {"temperature": 0.0, "top_p": 0.0, "top_k": None}
    genai.configure(api_key='', transport='rest')
    model = genai.GenerativeModel('models/gemini-pro', generation_config = generation_config)
    processed_flag = False
    ii = 0
    while not processed_flag:
        try:
            response = model.generate_content(prompt)
            input_tokens = model.count_tokens(prompt).total_tokens
            output_tokens = model.count_tokens(response.text).total_tokens
            return response.text, input_tokens, output_tokens
        except Exception as e:
            if ii >= 5:
                res = f'wrong!!, {str(e)}'
                return res, "wrong!!", "wrong!!"
            ii += 1
            processed_flag = False
            print(e)
            print('Error! Sleep for 5s.')
            time.sleep(5)

def fewshot(few_shot, sub_qa, final_q, final_res):
    if few_shot == "9":
        inputs = _REFINE_9.format(sub_qa, final_q, final_res)
    elif few_shot == "3":
        inputs = _REFINE_3.format(sub_qa, final_q, final_res)
    elif few_shot == "1":
        inputs = _REFINE_1.format(sub_qa, final_q, final_res)
    elif few_shot == "12":
        inputs = _REFINE_12.format(sub_qa, final_q, final_res)
    else:# 6
        inputs = _REFINE.format(sub_qa, final_q, final_res)
    return inputs
def run(read_path, write_path, LLMs, few_shot):
    if not os.path.exists(write_path):
        os.makedirs(write_path)
    with open(read_path, 'r') as f1:
        data = json.load(f1)
        for item in data:
            imgname = item['imgname']
            label = str(item['label'])
            cleaned_label = "".join(c for c in label if c.isalnum() or c in (' ', '_', '-', '.'))
            tmp_imgid = imgname.split('/')[-1]
            tmp_write_path = os.path.join(write_path, f"[{tmp_imgid}]_{cleaned_label}.json")
            if not os.path.exists(tmp_write_path):
                if len(item['sub_res']) == 0:
                    final_q = item['query']
                    final_res = item['response']
                    save = {'imgname': imgname, 'q': final_q, 'sub_q': 'None', 'sub_ans': 'None', 'ori_res': final_res, 'res': final_res, 'label': label}
                else:
                    print(f'using {LLMs}')
                    subqs = item['sub_q'][:-1]
                    subans = item['sub_res']
                    sub_qa = ''
                    for ii in range(len(subans)):
                        suba = subans[ii].replace('\n', ' ')
                        sub_qa += f"{subqs[ii]}\nsub_ans{ii+1}:{suba}\n"
                    final_q = item['sub_q'][-1].split(':', 1)[-1] if ":" in item['sub_q'][-1] else item['sub_q'][-1]
                    final_res = item['response'].replace('\n', ' ')
                    inputs = fewshot(few_shot, sub_qa, final_q, final_res)
                    if LLMs == "gpt4":
                        pred_res, my_statistic = gpt4(inputs)
                    elif LLMs == "gemini":
                        pred_res,input_tokens,output_tokens = gemini(inputs)
                    elif LLMs == "llama":
                        pred_res,input_tokens,output_tokens = llama3_8b(inputs)
                    if LLMs == 'llama3_8b' or LLMs == "gemini":
                        save = {'imgname': imgname, 'q': final_q, 'sub_q': subqs, 'sub_ans': subans, 'ori_res': final_res, 'res': pred_res, 'label': label, "input_tokens": input_tokens, "output_tokens": output_tokens}
                    else:
                        save = {'imgname': imgname, 'q': final_q, 'sub_q': subqs, 'sub_ans': subans, 'ori_res': final_res, 'res': pred_res, 'label': label, 'statistic': my_statistic}
                with open(tmp_write_path, 'w', encoding='utf-8') as json_file:
                    json.dump(save, json_file, ensure_ascii=False, indent=4)
                    print(f'{tmp_write_path} not exit, writting')
            
            
if __name__ == '__main__':
    MLLMs = ""
    few_shot = "6" # "3", "9", "1", "12" # "6", 
    LLMs1 = ""
    LLMs2 = ""
    read_path = r''
    write_path = f'/res/3refine/{LLMs1}_{MLLMs}_{LLMs2}/{few_shot}/human_val'
    run(read_path, write_path, LLMs2, few_shot)
