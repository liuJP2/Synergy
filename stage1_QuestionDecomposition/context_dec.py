examples = '''Based on the table_head, break down the following questions according to its grammatical structure.
Note that:
1.if the question does not require any computations, simply insert the original question into sub_q1;
2.If the subquestion involves chart shapes or colors, a question for represent should be inserted at that sub_q; 
3.If there is no entity linked to table_head, the decomposition is directly based on the literal meaning of the question;
Here are some examples.

table_head:{{
    col_head: ["Entity", "Very strong", "Strong", "Not very strong", "No complaints"],
    row_head: ["Entity", "People in cities & people in rural areas", "Young & folder people", "Black & white people", "Rich & poor people", "Democrats & Republicans"]
    }}
Q: what's the number of very strong young and folder people?
entites link to table_head: very strong->col_head["Very strong"], young and folder people->row_head["Young & folder people"]
sub_questions:
sub_q1: what's the number of very strong young and folder people?

Q: What is the difference in value between Blue bar and Green bar?
entites link to table_head: None
sub_questions:
sub_q1: What is the Blue bar represent? What is the value of Blue bar?
sub_q2: What is the Green bar represent? What is the value of Green bar?
sub_q3: What is the difference in value between Blue bar and Green bar?

Q: Is the median of all the bars in Strong category greater than the highest value of gray bar?
entites link to table_head: Strong->row_head["Strong"]
sub_questions:
sub_q1: What is the median value of all the bars in Strong category?
sub_q2: What is the gray bar represent? What is the highest value of gray bar?
sub_q3: Is the median of all the bars in Strong category greater than the highest value of gray bar?

Q: What is the ratio of the blue and dark blue pie?
entites link to table_head: None
sub_questions:
sub_q1: What is the blue pie represent? what is the value of the blue pie?
sub_q2: What is the dark blue pie represent? What is the value of the dark blue pie?
sub_q3: What is the ratio of the blue and dark blue pie?

Based on the table_head, break down the following questions according to its grammatical structure.
Note that:
1.if the question does not require any computations, simply insert the original question into sub_q1;
2.If the subquestion involves chart shapes or colors, a question for represent should be inserted at that sub_q; 
3.If there is no entity linked to table_head, the decomposition is directly based on the literal meaning of the question;
{}
Q: {}
'''


examples_plotqa = '''Based on the table_head, break down the following questions according to its grammatical structure.
Note that:
1.if the question does not require any computations, simply insert the original question into sub_q1;
2.If the subquestion involves chart shapes or colors, a question for represent should be inserted at that sub_q; 
3.If there is no entity linked to table_head, the decomposition is directly based on the literal meaning of the question;
Here are some examples.

table_head:{{
    col_head: ["Entity", "Very strong", "Strong", "Not very strong", "No complaints"],
    row_head: ["Entity", "People in cities & people in rural areas", "Young & folder people", "Black & white people", "Rich & poor people", "Democrats & Republicans"]
    }}
Q: what's the number of very strong young and folder people?
entites link to table_head: very strong->col_head["Very strong"], young and folder people->row_head["Young & folder people"]
sub_questions:
sub_q1: what's the number of very strong young and folder people?

Q: What is the difference in value between Blue bar and Green bar?
entites link to table_head: None
sub_questions:
sub_q1: What is the Blue bar represent? What is the value of Blue bar?
sub_q2: What is the Green bar represent? What is the value of Green bar?
sub_q3: What is the difference in value between Blue bar and Green bar?

Q: Is the median of all the bars in Strong category greater than the highest value of gray bar?
entites link to table_head: Strong->row_head["Strong"]
sub_questions:
sub_q1: What is the median value of all the bars in Strong category?
sub_q2: What is the gray bar represent? What is the highest value of gray bar?
sub_q3: Is the median of all the bars in Strong category greater than the highest value of gray bar?

Q: What is the ratio of the blue and dark blue pie?
entites link to table_head: None
sub_questions:
sub_q1: What is the blue pie represent? what is the value of the blue pie?
sub_q2: What is the dark blue pie represent? What is the value of the dark blue pie?
sub_q3: What is the ratio of the blue and dark blue pie?

Based on the table_head, break down the following questions according to its grammatical structure.
Note that:
1.if the question does not require any computations, simply insert the original question into sub_q1;
2.If the subquestion involves chart shapes or colors, a question for represent should be inserted at that sub_q; 
3.If there is no entity linked to table_head, the decomposition is directly based on the literal meaning of the question;
{}
The title for the table: {}
Q: {}
'''

"""

Q: What's the lefmost value of bar in Black and white people?
entities link to table_head: black and white people->row_head["Black & white people"]
sub_questions:
sub_q1: What's the lefmost value of bar in Black and white people?


Q: What is the value of the navy blue bar in middle?
entities link to table_head: None
sub_questions:
sub_q1: What is the navy blue bar represent? What is the value of the navy blue bar in middle?

"""
