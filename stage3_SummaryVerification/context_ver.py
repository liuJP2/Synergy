_REFINE = """
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'.
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

Here are some examples.
sub_qa pairs:
sub_q1: What does the bar representing employees who have stress represent? What is the value for employees who have stress?
sub_ans1:The blue bar represents employees that experience work-related stress "always", "often" or "sometimes". The percentage value for this group is 63%. Therefore, the answer is 63%.
sub_q2: What does the bar representing employees who don't have stress represent? What is the value for employees who don't have stress?
sub_ans2:The blue bar represents employees that rarely experience work-related stress. The percentage of these employees is 0.35. 
Q: What's the ratio between employees who have stress and those don't have?
ori_answer:9:5(9 to 5)
Explanation: To answer the question, we need to know employees who have stress and who don't have. We find 63% /employees have stress from sub_ans1, and we find 0.35 employees don't have stress from sub_ans2. Unify the two units, expressed as 63 and 35. So we can calculate the ratio between employees who have stress and those don't have: Ratio=63/35. Therefore, the answer is: 1.8.

sub_qa pairs:
sub_q1: What is the percent value of Satisfied?"
sub_ans1:The percent value of \"Satisfied\" is 25.
sub_q2: What is the percent value of Often dissatisfied with work?
sub_ans2:The percentage value for \"Often dissatisfied with work\" is 33.
sub_q3: What is the sum of the percents of Satisfied and Often dissatisfied?
sub_ans3: the sum of the percents of Satisfied and Often dissatisfied is \"Satisfied\"(25) + \"Often dissatisfied with work\"(33)=25+33=58.
sub_q4: What is the percent value of Neutralizing attitude?
sub_ans4:The percentage value for \"Neutralizing attitude\" is 55.
Q: Is the sum of the percents of Satisfied and Often dissatisfied with work more than Neutralizing attitude?"
ori_answer:No
Explanation: To answer the question, we need to know the sum of the percents of Satisfied and Often dissatisfied with work and the value of Neutralizing attitude. We find the sum of the percents of Satisfied and Often dissatisfied is 25+33=58 from [sub_ans1, sub_ans2, sub_ans3], and we find the value of Neutralizing attitude is 55 from sub_ans4. So the sum of the percents of Satisfied and Often dissatisfied(58) is greater than Neutralizing attitude(55). Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the value of meat?
sub_ans1:The pie graph shows that meat has a share of 25%. Therefore, the answer is 25.
sub_q2: What is the value of vegetarian diet?
sub_ans2:The value of vegetarian diet is 25%. This information can be found in the provided table under the \"vegetarian diet\" column for the characteristic \"vegetarian diet\".
Q: What is the difference between meat and vegetarian diet?
ori_answer:There wasn't any difference as both meat and vegetarian diet had value of 25%.
Explanation: To answer the question, we need to know the value of meat and the value of vegetarian diet. We can find the value of meat is 25 from sub_ans1, and find the value of vegetarian diet is 25%. Unify the two units, expressed as 25 and 25. The difference between meat and vegetarian diet is 25-25, the result of the calculation is 0. Therefore, the answer is: 0.

sub_qa pairs:
sub_q1: What is the Mineral Rent (as % /of GDP) of Canada in 1983?
sub_ans1:The mineral rent (as percentage of GDP) of Canada in 1983 was 3.62.
sub_q2: What is the Mineral Rent (as % /of GDP) of Canada in 1986?
sub_ans2:The mineral rent (as percentage of GDP) of Canada in 1986 is 4.99.
Q: What is the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986?
ori_answer:3.62-4.99
Explanation: To answer the question, we need to know the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986. We find that the Mineral Rent (as % /of GDP) of Canada in 1983 is 3.62% /from sub_ans1, and the Mineral Rent (as % /of GDP) of Canada in 1986 us 4.99 from sub_ans2. So we can calculate the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986: 3.62-4.99, the result of the calculation "3.62-4.99" is -1.37. Therefore, the answer is: -1.37.

sub_qa pairs:
sub_q1: What is the number of people with a sweet tooth?
sub_ans1:The chart shows that 50% \of people have a sweet tooth.
sub_q2: How many people don't like sweets?
sub_ans2: The number of people who don't like sweets is relatively small.
Q: What is the ratio of the people who have a sweet tooth versus those who don't?
ori_answer: 5:3
Explanation: To answer the question, we need to know the number of people who like sweets. We find that 50% \\approve from sub_ans1. However, we couldn't find a specific number of people who don't like sweets. There are not enough information to deduce the answer, the value of ori_answer is used, we can see that "5:3" includes numerical calculations, so it is calculated to get the final result 5:3=1.66. Therefore, the answer is: 1.66.

sub_qa pairs:
sub_q1: What is the value of Unhappiness?
sub_ans1:The value of Unhappiness is 78.
sub_q2: What is the value of Happiness?
sub_ans2:The value of \"Happiness\" according to the given table is 20%.
Q: How many times is Unhappiness more than Happiness?
ori_answer:39 times
Explanation: To answer the question, we need to know the value of Unhappiness and the value of Happiness. We can find the value of Unhappiness is 78 from sub_ans1, and find the value of Happiness is 20%. Unify the two units, expressed as 78 and 20. To find out how many times Unhappiness is more than Happiness, divide the value of Dissatisfied by the value of Satisfied: 78:20, the result of the calculation "78:20" is 3.9. Therefore, the answer is: 3.9.

Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""


# 3-shot
_REFINE_3 = """
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'.
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

Here are some examples.
sub_qa pairs:
sub_q1: What does the bar representing employees who have stress represent? What is the value for employees who have stress?
sub_ans1:The blue bar represents employees that experience work-related stress "always", "often" or "sometimes". The percentage value for this group is 63%. Therefore, the answer is 63%.
sub_q2: What does the bar representing employees who don't have stress represent? What is the value for employees who don't have stress?
sub_ans2:The blue bar represents employees that rarely experience work-related stress. The percentage of these employees is 0.35. 
Q: What's the ratio between employees who have stress and those don't have?
ori_answer:9:5(9 to 5)
Explanation: To answer the question, we need to know employees who have stress and who don't have. We find 63% /employees have stress from sub_ans1, and we find 0.35 employees don't have stress from sub_ans2. Unify the two units, expressed as 63 and 35. So we can calculate the ratio between employees who have stress and those don't have: Ratio=63/35. Therefore, the answer is: 1.8.

sub_qa pairs:
sub_q1: What is the percent value of Satisfied?
sub_ans1:The percent value of \"Satisfied\" is 25.
sub_q2: What is the percent value of Often dissatisfied with work?
sub_ans2:The percentage value for \"Often dissatisfied with work\" is 33.
sub_q3: What is the sum of the percents of Satisfied and Often dissatisfied?
sub_ans3: the sum of the percents of Satisfied and Often dissatisfied is \"Satisfied\"(25) + \"Often dissatisfied with work\"(33)=25+33=58.
sub_q4: What is the percent value of Neutralizing attitude?
sub_ans4:The percentage value for \"Neutralizing attitude\" is 55.
Q: Is the sum of the percents of Satisfied and Often dissatisfied with work more than Neutralizing attitude?"
ori_answer:No
Explanation: To answer the question, we need to know the sum of the percents of Satisfied and Often dissatisfied with work and the value of Neutralizing attitude. We find the sum of the percents of Satisfied and Often dissatisfied is 25+33=58 from [sub_ans1, sub_ans2, sub_ans3], and we find the value of Neutralizing attitude is 55 from sub_ans4. So the sum of the percents of Satisfied and Often dissatisfied(58) is greater than Neutralizing attitude(55). Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the value of meat?
sub_ans1:The pie graph shows that meat has a share of 25%. Therefore, the answer is 25.
sub_q2: What is the value of vegetarian diet?
sub_ans2:The value of vegetarian diet is 25%. This information can be found in the provided table under the \"vegetarian diet\" column for the characteristic \"vegetarian diet\".
Q: What is the difference between meat and vegetarian diet?
ori_answer:There wasn't any difference as both meat and vegetarian diet had value of 25%.
Explanation: To answer the question, we need to know the value of meat and the value of vegetarian diet. We can find the value of meat is 25 from sub_ans1, and find the value of vegetarian diet is 25%. Unify the two units, expressed as 25 and 25. The difference between meat and vegetarian diet is 25-25, the result of the calculation is 0. Therefore, the answer is: 0.


Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""


# 1-shot
_REFINE_1 = """
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'.
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

Here are some examples.
sub_qa pairs:
sub_q1: What does the bar representing employees who have stress represent? What is the value for employees who have stress?
sub_ans1:The blue bar represents employees that experience work-related stress "always", "often" or "sometimes". The percentage value for this group is 63%. Therefore, the answer is 63%.
sub_q2: What does the bar representing employees who don't have stress represent? What is the value for employees who don't have stress?
sub_ans2:The blue bar represents employees that rarely experience work-related stress. The percentage of these employees is 0.35. 
Q: What's the ratio between employees who have stress and those don't have?
ori_answer:9:5(9 to 5)
Explanation: To answer the question, we need to know employees who have stress and who don't have. We find 63% /employees have stress from sub_ans1, and we find 0.35 employees don't have stress from sub_ans2. Unify the two units, expressed as 63 and 35. So we can calculate the ratio between employees who have stress and those don't have: Ratio=63/35. Therefore, the answer is: 1.8.

Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""

# 9-shot
_REFINE_9 = """
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'.
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

Here are some examples.
sub_qa pairs:
sub_q1: What does the bar representing employees who have stress represent? What is the value for employees who have stress?
sub_ans1:The blue bar represents employees that experience work-related stress "always", "often" or "sometimes". The percentage value for this group is 63%. Therefore, the answer is 63%.
sub_q2: What does the bar representing employees who don't have stress represent? What is the value for employees who don't have stress?
sub_ans2:The blue bar represents employees that rarely experience work-related stress. The percentage of these employees is 0.35. 
Q: What's the ratio between employees who have stress and those don't have?
ori_answer:9:5(9 to 5)
Explanation: To answer the question, we need to know employees who have stress and who don't have. We find 63% /employees have stress from sub_ans1, and we find 0.35 employees don't have stress from sub_ans2. Unify the two units, expressed as 63 and 35. So we can calculate the ratio between employees who have stress and those don't have: Ratio=63/35. Therefore, the answer is: 1.8.

sub_qa pairs:
sub_q1: What is the percent value of Satisfied?
sub_ans1:The percent value of \"Satisfied\" is 25.
sub_q2: What is the percent value of Often dissatisfied with work?
sub_ans2:The percentage value for \"Often dissatisfied with work\" is 33.
sub_q3: What is the sum of the percents of Satisfied and Often dissatisfied?
sub_ans3: the sum of the percents of Satisfied and Often dissatisfied is \"Satisfied\"(25) + \"Often dissatisfied with work\"(33)=25+33=58.
sub_q4: What is the percent value of Neutralizing attitude?
sub_ans4:The percentage value for \"Neutralizing attitude\" is 55.
Q: Is the sum of the percents of Satisfied and Often dissatisfied with work more than Neutralizing attitude?"
ori_answer:No
Explanation: To answer the question, we need to know the sum of the percents of Satisfied and Often dissatisfied with work and the value of Neutralizing attitude. We find the sum of the percents of Satisfied and Often dissatisfied is 25+33=58 from [sub_ans1, sub_ans2, sub_ans3], and we find the value of Neutralizing attitude is 55 from sub_ans4. So the sum of the percents of Satisfied and Often dissatisfied(58) is greater than Neutralizing attitude(55). Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the value of meat?
sub_ans1:The pie graph shows that meat has a share of 25%. Therefore, the answer is 25.
sub_q2: What is the value of vegetarian diet?
sub_ans2:The value of vegetarian diet is 25%. This information can be found in the provided table under the \"vegetarian diet\" column for the characteristic \"vegetarian diet\".
Q: What is the difference between meat and vegetarian diet?
ori_answer:There wasn't any difference as both meat and vegetarian diet had value of 25%.
Explanation: To answer the question, we need to know the value of meat and the value of vegetarian diet. We can find the value of meat is 25 from sub_ans1, and find the value of vegetarian diet is 25%. Unify the two units, expressed as 25 and 25. The difference between meat and vegetarian diet is 25-25, the result of the calculation is 0. Therefore, the answer is: 0.

sub_qa pairs:
sub_q1: What is the Mineral Rent (as % /of GDP) of Canada in 1983?
sub_ans1:The mineral rent (as percentage of GDP) of Canada in 1983 was 3.62.
sub_q2: What is the Mineral Rent (as % /of GDP) of Canada in 1986?
sub_ans2:The mineral rent (as percentage of GDP) of Canada in 1986 is 4.99.
Q: What is the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986?
ori_answer:3.62-4.99
Explanation: To answer the question, we need to know the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986. We find that the Mineral Rent (as % /of GDP) of Canada in 1983 is 3.62% /from sub_ans1, and the Mineral Rent (as % /of GDP) of Canada in 1986 us 4.99 from sub_ans2. So we can calculate the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986: 3.62-4.99, the result of the calculation "3.62-4.99" is -1.37. Therefore, the answer is: -1.37.

sub_qa pairs:
sub_q1: What is the number of people with a sweet tooth?
sub_ans1:The chart shows that 50% \of people have a sweet tooth.
sub_q2: How many people don't like sweets?
sub_ans2: The number of people who don't like sweets is relatively small.
Q: What is the ratio of the people who have a sweet tooth versus those who don't?
ori_answer: 5:3
Explanation: To answer the question, we need to know the number of people who like sweets. We find that 50% \\approve from sub_ans1. However, we couldn't find a specific number of people who don't like sweets. There are not enough information to deduce the answer, the value of ori_answer is used, we can see that "5:3" includes numerical calculations, so it is calculated to get the final result 5:3=1.66. Therefore, the answer is: 1.66.

sub_qa pairs:
sub_q1: What is the value of Unhappiness?
sub_ans1:The value of Unhappiness is 78.
sub_q2: What is the value of Happiness?
sub_ans2:The value of \"Happiness\" according to the given table is 20%.
Q: How many times is Unhappiness more than Happiness?
ori_answer:39 times
Explanation: To answer the question, we need to know the value of Unhappiness and the value of Happiness. We can find the value of Unhappiness is 78 from sub_ans1, and find the value of Happiness is 20%. Unify the two units, expressed as 78 and 20. To find out how many times Unhappiness is more than Happiness, divide the value of Dissatisfied by the value of Satisfied: 78:20, the result of the calculation "78:20" is 3.9. Therefore, the answer is: 3.9.

sub_qa pairs:
sub_q1: What does the bar represent for each year?
sub_ans1:The bar chart on the chart shows the percentage of undergraduate graduates who studied in Shanghai between 1998 and 2008.
Q:Between which year does the bar show the proportion of undergraduate graduates is 25%
ori_answer:1999  According to the chart, there are 25 percentage of undergraduate graduates in 1999.
Explanation: To answer the question, we need to know which year's bar has 25 percent of undergraduate graduates. We couldn't find any relevant information to deduce the correct answer, so the value of ori_answer is used. Therefore, the answer is: 1999.

sub_qa pairs:
sub_q1: What is the value of the green bar for the year 2002?
sub_ans1: The value of the green bar for the year 2002 is 48%.
sub_q2: What is the value of the green bar for the year 2003?
sub_ans2: The value of the green bar for the year 2003 is 45%.
sub_q3: What is the value of the green bar for the year 2004?
sub_ans3: The value of the green bar for the year 2004 is 66%.
Q: What's the average of the green bar values from 2002 to 2004?
ori_answer: 240/3
Explanation: To answer the question, we need to know the values of the green bar for each year in 2002 to 2004. From sub_ans1, sub_ans2, and sub_ans3, we have the values 48%, 45%, and 66% \respectively. To find the average of these bar, we can adding these values first: 78 + 79 + 83 = 240. Then we find there are three years, we divide this sum by 3 to get the average: 240/3. The result of the calculation "240/3" is 80. Therefore, the answer is: 80.

sub_qa pairs:
sub_q1: What is the average value of the blue bars?
sub_ans1: The average value of the blue bars is 65.
sub_q2: What is the average value of the red bars?"
sub_ans2: The average value of the red bars is 72.56%.
Q: Is the average of blue bars smaller than the average of red bars?",
ori_answer: Yes
Explanation: To answer the question, we need to know the average value of the blue bars and the red bars. From sub_ans1, we find the average value of the blue bars is 65. From sub_ans2, we find the average value of the red bars is 72.56%. Unify the two units, expressed as 65 and 72.56. Comparing these two values, 65 is less than 72.56. Therefore, the answer is: Yes.

Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""


# 12-shot
_REFINE_12 = """
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'.
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

Here are some examples.
sub_qa pairs:
sub_q1: What does the bar representing employees who have stress represent? What is the value for employees who have stress?
sub_ans1:The blue bar represents employees that experience work-related stress "always", "often" or "sometimes". The percentage value for this group is 63%. Therefore, the answer is 63%.
sub_q2: What does the bar representing employees who don't have stress represent? What is the value for employees who don't have stress?
sub_ans2:The blue bar represents employees that rarely experience work-related stress. The percentage of these employees is 0.35. 
Q: What's the ratio between employees who have stress and those don't have?
ori_answer:9:5(9 to 5)
Explanation: To answer the question, we need to know employees who have stress and who don't have. We find 63% /employees have stress from sub_ans1, and we find 0.35 employees don't have stress from sub_ans2. Unify the two units, expressed as 63 and 35. So we can calculate the ratio between employees who have stress and those don't have: Ratio=63/35. Therefore, the answer is: 1.8.

sub_qa pairs:
sub_q1: What is the percent value of Satisfied?
sub_ans1:The percent value of \"Satisfied\" is 25.
sub_q2: What is the percent value of Often dissatisfied with work?
sub_ans2:The percentage value for \"Often dissatisfied with work\" is 33.
sub_q3: What is the sum of the percents of Satisfied and Often dissatisfied?
sub_ans3: the sum of the percents of Satisfied and Often dissatisfied is \"Satisfied\"(25) + \"Often dissatisfied with work\"(33)=25+33=58.
sub_q4: What is the percent value of Neutralizing attitude?
sub_ans4:The percentage value for \"Neutralizing attitude\" is 55.
Q: Is the sum of the percents of Satisfied and Often dissatisfied with work more than Neutralizing attitude?"
ori_answer:No
Explanation: To answer the question, we need to know the sum of the percents of Satisfied and Often dissatisfied with work and the value of Neutralizing attitude. We find the sum of the percents of Satisfied and Often dissatisfied is 25+33=58 from [sub_ans1, sub_ans2, sub_ans3], and we find the value of Neutralizing attitude is 55 from sub_ans4. So the sum of the percents of Satisfied and Often dissatisfied(58) is greater than Neutralizing attitude(55). Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the value of meat?
sub_ans1:The pie graph shows that meat has a share of 25%. Therefore, the answer is 25.
sub_q2: What is the value of vegetarian diet?
sub_ans2:The value of vegetarian diet is 25%. This information can be found in the provided table under the \"vegetarian diet\" column for the characteristic \"vegetarian diet\".
Q: What is the difference between meat and vegetarian diet?
ori_answer:There wasn't any difference as both meat and vegetarian diet had value of 25%.
Explanation: To answer the question, we need to know the value of meat and the value of vegetarian diet. We can find the value of meat is 25 from sub_ans1, and find the value of vegetarian diet is 25%. Unify the two units, expressed as 25 and 25. The difference between meat and vegetarian diet is 25-25, the result of the calculation is 0. Therefore, the answer is: 0.

sub_qa pairs:
sub_q1: What is the Mineral Rent (as % /of GDP) of Canada in 1983?
sub_ans1:The mineral rent (as percentage of GDP) of Canada in 1983 was 3.62.
sub_q2: What is the Mineral Rent (as % /of GDP) of Canada in 1986?
sub_ans2:The mineral rent (as percentage of GDP) of Canada in 1986 is 4.99.
Q: What is the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986?
ori_answer:3.62-4.99
Explanation: To answer the question, we need to know the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986. We find that the Mineral Rent (as % /of GDP) of Canada in 1983 is 3.62% /from sub_ans1, and the Mineral Rent (as % /of GDP) of Canada in 1986 us 4.99 from sub_ans2. So we can calculate the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986: 3.62-4.99, the result of the calculation "3.62-4.99" is -1.37. Therefore, the answer is: -1.37.

sub_qa pairs:
sub_q1: What is the number of people with a sweet tooth?
sub_ans1:The chart shows that 50% \of people have a sweet tooth.
sub_q2: How many people don't like sweets?
sub_ans2: The number of people who don't like sweets is relatively small.
Q: What is the ratio of the people who have a sweet tooth versus those who don't?
ori_answer: 5:3
Explanation: To answer the question, we need to know the number of people who like sweets. We find that 50% \\approve from sub_ans1. However, we couldn't find a specific number of people who don't like sweets. There are not enough information to deduce the answer, the value of ori_answer is used, we can see that "5:3" includes numerical calculations, so it is calculated to get the final result 5:3=1.66. Therefore, the answer is: 1.66.

sub_qa pairs:
sub_q1: What is the value of Unhappiness?
sub_ans1:The value of Unhappiness is 78.
sub_q2: What is the value of Happiness?
sub_ans2:The value of \"Happiness\" according to the given table is 20%.
Q: How many times is Unhappiness more than Happiness?
ori_answer:39 times
Explanation: To answer the question, we need to know the value of Unhappiness and the value of Happiness. We can find the value of Unhappiness is 78 from sub_ans1, and find the value of Happiness is 20%. Unify the two units, expressed as 78 and 20. To find out how many times Unhappiness is more than Happiness, divide the value of Dissatisfied by the value of Satisfied: 78:20, the result of the calculation "78:20" is 3.9. Therefore, the answer is: 3.9.

sub_qa pairs:
sub_q1: What does the bar represent for each year?
sub_ans1:The bar chart on the chart shows the percentage of undergraduate graduates who studied in Shanghai between 1998 and 2008.
Q:Between which year does the bar show the proportion of undergraduate graduates is 25%
ori_answer:1999  According to the chart, there are 25 percentage of undergraduate graduates in 1999.
Explanation: To answer the question, we need to know which year's bar has 25 percent of undergraduate graduates. We couldn't find any relevant information to deduce the correct answer, so the value of ori_answer is used. Therefore, the answer is: 1999.

sub_qa pairs:
sub_q1: What is the value of the green bar for the year 2002?
sub_ans1: The value of the green bar for the year 2002 is 48%.
sub_q2: What is the value of the green bar for the year 2003?
sub_ans2: The value of the green bar for the year 2003 is 45%.
sub_q3: What is the value of the green bar for the year 2004?
sub_ans3: The value of the green bar for the year 2004 is 66%.
Q: What's the average of the green bar values from 2002 to 2004?
ori_answer: 240/3
Explanation: To answer the question, we need to know the values of the green bar for each year in 2002 to 2004. From sub_ans1, sub_ans2, and sub_ans3, we have the values 48%, 45%, and 66% \respectively. To find the average of these bar, we can adding these values first: 78 + 79 + 83 = 240. Then we find there are three years, we divide this sum by 3 to get the average: 240/3. The result of the calculation "240/3" is 80. Therefore, the answer is: 80.

sub_qa pairs:
sub_q1: What is the average value of the blue bars?
sub_ans1: The average value of the blue bars is 65.
sub_q2: What is the average value of the red bars?
sub_ans2: The average value of the red bars is 72.56%.
Q: Is the average of blue bars smaller than the average of red bars?
ori_answer: Yes
Explanation: To answer the question, we need to know the average value of the blue bars and the red bars. From sub_ans1, we find the average value of the blue bars is 65. From sub_ans2, we find the average value of the red bars is 72.56%. Unify the two units, expressed as 65 and 72.56. Comparing these two values, 65 is less than 72.56. Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the maximum number of Yes votes in a single year?
sub_ans1: The maximum number of Yes votes is 15034.
sub_q2: What is the maximum number of No votes in a single year?
sub_ans2: The maximum number of No votes is 6512.
Q: What is the difference between the person with the most Yes votes and the person with the most No votes in a single year?
ori_answer: 18034-4512=13522
Explanation: To answer the question, we need to know the maximum number of Yes votes and maximum number of NO votes. From sub_ans1, we find the maximum number of Yes votes is 15034. From sub_ans2, we find the maximum number of No votes is 6512. The difference between them is 15034-6512, the result of the calculation is 8522. Therefore, the answer is: 8522.

sub_qa pairs:
sub_q1: What is the value of Excellent in All candidants?
sub_ans1: The value of Excellent for all candidants can be found in the table with a value of 33.
sub_q2: What is the value of Good in All candidants?
sub_ans2: The value of Good for all candidants can be found in the chart with a value of 51.
sub_q3: What is the value of Ordinary in All candidants?
sub_ans3: The key word Ordinary for all candidants can be found by looking at the middle row in the table. According to the data provided, it's nan. Therefore, based on the information available, we couldn't get the specific value of Ordinary.
Q: What is the sum value of Excellent, Good, and Ordinary in All candidants?
ori_answer: 196
Explanation: To answer the question, we need to know the value of Excellent, Good, and Ordinary in All candidants. From sub_ans1, we find the value of Excellent is 33. From sub_ans2, we can find the value of Good is 51. However, we could not find the value of Oridinary in the sub-qa pairs provided. So the ori_answer is used as the correct answer. Therefore, the answer is: 196.

sub_qa pairs:
sub_q1: What is the number of people who have employment pressure?
sub_ans1: The number of people who have employment pressure is 3,159.
sub_q2: What is the number of people who are optimistic about employment?
sub_ans2: The number of people who are optimistic about employment is 4,506.
Q: What is the ratio of the people who have employment pressure versus those who are optimistic about employment?
ori_answer: 3,159/4,506
Explanation: To answer the question, we need to know the value of people who have employment pressure and who are optimistic about employment. We can find the value of who have employment pressure is 3,159 from sub_ans1, and find the value of who are optimistic about employment is 4,506. To find out how many times Unhappiness is more than Happiness, divide the value of Dissatisfied by the value of Satisfied: 3159:4506, the result of the calculation "3159:4506" is 0.7. Therefore, the answer is: 0.7.

Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""
_REFINE_PlotQA = """
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. If calculation is involved, please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.
Here are some examples.

sub_qa pairs:
sub_q1: What is the Mineral Rent (as % /of GDP) of Canada in 1983?
sub_ans1:The mineral rent (as percentage of GDP) of Canada in 1983 was 3.62.
sub_q2: What is the Mineral Rent (as % /of GDP) of Canada in 1986?
sub_ans2:The mineral rent (as percentage of GDP) of Canada in 1986 is 4.99.
Q: What is the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986?
ori_answer:1.37
Explanation: To answer the question, we need to know the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986. We find that the Mineral Rent (as % /of GDP) of Canada in 1983 is 3.62% /from sub_ans1, and the Mineral Rent (as % /of GDP) of Canada in 1986 us 4.99 from sub_ans2. So we can calculate the difference between the Mineral Rent (as % /of GDP) of Canada in 1983 and that in 1986: difference=3.62-4.99=-1.37. Therefore, the answer is: -1.37.

sub_qa pairs:
sub_q1: What is the percent value of Satisfied?"
sub_ans1:The percent value of \"Satisfied\" is 25.\n\nTherefore, the answer is 25.
sub_q2: What is the percent value of Often dissatisfied with work?
sub_ans2:The percentage value for \"Often dissatisfied with work\" is 33.\n\nTherefore, the answer is 33.
sub_q3: What is the sum of the percents of Satisfied and Often dissatisfied?
sub_ans3:To find the sum of the percentages for \"Satisfied\" (25) and \"Often dissatisfied with work\" (33), we simply add these two numbers together:\n\n25 + 33 = 58\n\nSo, the total percentage that The sum of workers' satisfaction and dissatisfaction with their working hours is 58%.
sub_q4: What is the percent value of Neutralizing attitude?
sub_ans4:The percentage value for \"Neutralizing attitude\" is 55.\n\nTherefore, the answer is 55.
Q: Is the sum of the percents of Satisfied and Often dissatisfied with work more than Neutralizing attitude?
ori_answer:No
Explanation: To answer the question, we need to know the sum of the percents of Satisfied and Often dissatisfied with work and the value of Neutralizing attitude. We find the sum of the percents of Satisfied and Often dissatisfied is 25+33=58 from [sub_ans1, sub_ans2, sub_ans3], and we find the value of Neutralizing attitude is 55 from sub_ans4. So the sum of the percents of Satisfied and Often dissatisfied(58) is greater than Neutralizing attitude(55). Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the value of meat?
sub_ans1:The pie graph shows that meat has a share of 25%. The table also confirms this with its data for \"meat\", which states it as having a Share of Respondents of 25%. Therefore, both sources agree on the same information.\n\nTherefore, the answer is 25.
sub_q2: What is the value of vegetarian diet?
sub_ans2:The value of vegetarian diet is 25%. This information can be found in the provided table under the \"vegetarian diet\" column for the characteristic \"vegetarian diet\".
Q: What is the difference between meat and vegetarian diet?
ori_answer:There wasn't any difference as both meat and vegetarian diet had value of 25%.
Explanation: To answer the question, we need to know the value of meat and the value of vegetarian diet. We can find the value of meat is 25% \from sub_ans1, and find the value of vegetarian diet is 25%. The difference between meat and vegetarian diet is 25\%-25\%=0%. Therefore, the answer is: 0%.

sub_qa pairs:
sub_q1: What does the bar represent for each year?
sub_ans1:The bars on this graph show how many percentage points out of total tertiary enrollment were made up by international students studying in Taiwan or Serbia between 2000 to 2008.
Q:Between which year does the bar show a 5 percent share of students from home?
ori_answer:2005  According to the chart, there are 5 percent share of students from home in 2005.
Explanation: To answer the question, we need to know which year's bar has 5 percent share of students from home. We couldn't find any relevant information to deduce the correct answer, so the value of ori_answer is used. Therefore, the answer is: 2005.

sub_qa pairs:
sub_q1: What is the value of Unhappiness?
sub_ans1:The value of Unhappiness is 78.
sub_q2: What is the value of Happiness?
sub_ans2:The value of \"Happiness\" according to the given table is 20%.
Q: How many times is Unhappiness more than Happiness?
ori_answer:39times
Explanation: To answer the question, we need to know the value of Unhappiness and the value of Happiness. We can find the value of Unhappiness is 78 from sub_ans1, and find the value of Happiness is 20%. Unify the two units, expressed as 78 and 20. To find out how many times Unhappiness is more than Happiness, divide the value of Dissatisfied by the value of Satisfied: 78 / 20 = 78 / 20 = 3.9. Therefore, the answer is: 3.9.

Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved, please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori answer is used as the correct answer.
sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""



# extract new 6-shot examples from 12-shot
_REFINE_new6 = """
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'.
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

Here are some examples.
sub_qa pairs:
sub_q1: What does the bar represent for each year?
sub_ans1:The bar chart on the chart shows the percentage of undergraduate graduates who studied in Shanghai between 1998 and 2008.
Q:Between which year does the bar show the proportion of undergraduate graduates is 25%
ori_answer:1999  According to the chart, there are 25 percentage of undergraduate graduates in 1999.
Explanation: To answer the question, we need to know which year's bar has 25 percent of undergraduate graduates. We couldn't find any relevant information to deduce the correct answer, so the value of ori_answer is used. Therefore, the answer is: 1999.

sub_qa pairs:
sub_q1: What is the value of the green bar for the year 2002?
sub_ans1: The value of the green bar for the year 2002 is 48%.
sub_q2: What is the value of the green bar for the year 2003?
sub_ans2: The value of the green bar for the year 2003 is 45%.
sub_q3: What is the value of the green bar for the year 2004?
sub_ans3: The value of the green bar for the year 2004 is 66%.
Q: What's the average of the green bar values from 2002 to 2004?
ori_answer: 240/3
Explanation: To answer the question, we need to know the values of the green bar for each year in 2002 to 2004. From sub_ans1, sub_ans2, and sub_ans3, we have the values 48%, 45%, and 66% \respectively. To find the average of these bar, we can adding these values first: 78 + 79 + 83 = 240. Then we find there are three years, we divide this sum by 3 to get the average: 240/3. The result of the calculation "240/3" is 80. Therefore, the answer is: 80.

sub_qa pairs:
sub_q1: What is the average value of the blue bars?
sub_ans1: The average value of the blue bars is 65.
sub_q2: What is the average value of the red bars?
sub_ans2: The average value of the red bars is 72.56%.
Q: Is the average of blue bars smaller than the average of red bars?
ori_answer: Yes
Explanation: To answer the question, we need to know the average value of the blue bars and the red bars. From sub_ans1, we find the average value of the blue bars is 65. From sub_ans2, we find the average value of the red bars is 72.56%. Unify the two units, expressed as 65 and 72.56. Comparing these two values, 65 is less than 72.56. Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the maximum number of Yes votes in a single year?
sub_ans1: The maximum number of Yes votes is 15034.
sub_q2: What is the maximum number of No votes in a single year?
sub_ans2: The maximum number of No votes is 6512.
Q: What is the difference between the person with the most Yes votes and the person with the most No votes in a single year?
ori_answer: 18034-4512=13522
Explanation: To answer the question, we need to know the maximum number of Yes votes and maximum number of NO votes. From sub_ans1, we find the maximum number of Yes votes is 15034. From sub_ans2, we find the maximum number of No votes is 6512. The difference between them is 15034-6512, the result of the calculation is 8522. Therefore, the answer is: 8522.

sub_qa pairs:
sub_q1: What is the value of Excellent in All candidants?
sub_ans1: The value of Excellent for all candidants can be found in the table with a value of 33.
sub_q2: What is the value of Good in All candidants?
sub_ans2: The value of Good for all candidants can be found in the chart with a value of 51.
sub_q3: What is the value of Ordinary in All candidants?
sub_ans3: The key word Ordinary for all candidants can be found by looking at the middle row in the table. According to the data provided, it's nan. Therefore, based on the information available, we couldn't get the specific value of Ordinary.
Q: What is the sum value of Excellent, Good, and Ordinary in All candidants?
ori_answer: 196
Explanation: To answer the question, we need to know the value of Excellent, Good, and Ordinary in All candidants. From sub_ans1, we find the value of Excellent is 33. From sub_ans2, we can find the value of Good is 51. However, we could not find the value of Oridinary in the sub-qa pairs provided. So the ori_answer is used as the correct answer. Therefore, the answer is: 196.

sub_qa pairs:
sub_q1: What is the number of people who have employment pressure?
sub_ans1: The number of people who have employment pressure is 3,159.
sub_q2: What is the number of people who are optimistic about employment?
sub_ans2: The number of people who are optimistic about employment is 4,506.
Q: What is the ratio of the people who have employment pressure versus those who are optimistic about employment?
ori_answer: 3,159/4,506
Explanation: To answer the question, we need to know the value of people who have employment pressure and who are optimistic about employment. We can find the value of who have employment pressure is 3,159 from sub_ans1, and find the value of who are optimistic about employment is 4,506. To find out how many times Unhappiness is more than Happiness, divide the value of Dissatisfied by the value of Satisfied: 3159:4506, the result of the calculation "3159:4506" is 0.7. Therefore, the answer is: 0.7.

Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""



# extract new 6-shot examples from 12-shot
_REFINE_new6_2="""
Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'.
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(Pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

Here are some examples.
sub_qa pairs:
sub_q1: What does the bar representing employees who have stress represent? What is the value for employees who have stress?
sub_ans1:The blue bar represents employees that experience work-related stress "always", "often" or "sometimes". The percentage value for this group is 63%. Therefore, the answer is 63%.
sub_q2: What does the bar representing employees who don't have stress represent? What is the value for employees who don't have stress?
sub_ans2:The blue bar represents employees that rarely experience work-related stress. The percentage of these employees is 0.35. 
Q: What's the ratio between employees who have stress and those don't have?
ori_answer:9:5(9 to 5)
Explanation: To answer the question, we need to know employees who have stress and who don't have. We find 63% /employees have stress from sub_ans1, and we find 0.35 employees don't have stress from sub_ans2. Unify the two units, expressed as 63 and 35. So we can calculate the ratio between employees who have stress and those don't have: Ratio=63/35. Therefore, the answer is: 1.8.

sub_qa pairs:
sub_q1: What is the value of meat?
sub_ans1:The pie graph shows that meat has a share of 25%. Therefore, the answer is 25.
sub_q2: What is the value of vegetarian diet?
sub_ans2:The value of vegetarian diet is 25%. This information can be found in the provided table under the \"vegetarian diet\" column for the characteristic \"vegetarian diet\".
Q: What is the difference between meat and vegetarian diet?
ori_answer:There wasn't any difference as both meat and vegetarian diet had value of 25%.
Explanation: To answer the question, we need to know the value of meat and the value of vegetarian diet. We can find the value of meat is 25 from sub_ans1, and find the value of vegetarian diet is 25%. Unify the two units, expressed as 25 and 25. The difference between meat and vegetarian diet is 25-25, the result of the calculation is 0. Therefore, the answer is: 0.

sub_qa pairs:
sub_q1: What is the number of people with a sweet tooth?
sub_ans1:The chart shows that 50% \of people have a sweet tooth.
sub_q2: How many people don't like sweets?
sub_ans2: The number of people who don't like sweets is relatively small.
Q: What is the ratio of the people who have a sweet tooth versus those who don't?
ori_answer: 5:3
Explanation: To answer the question, we need to know the number of people who like sweets. We find that 50% \\approve from sub_ans1. However, we couldn't find a specific number of people who don't like sweets. There are not enough information to deduce the answer, the value of ori_answer is used, we can see that "5:3" includes numerical calculations, so it is calculated to get the final result 5:3=1.66. Therefore, the answer is: 1.66.

sub_qa pairs:
sub_q1: What does the bar represent for each year?
sub_ans1:The bar chart on the chart shows the percentage of undergraduate graduates who studied in Shanghai between 1998 and 2008.
Q:Between which year does the bar show the proportion of undergraduate graduates is 25%
ori_answer:1999  According to the chart, there are 25 percentage of undergraduate graduates in 1999.
Explanation: To answer the question, we need to know which year's bar has 25 percent of undergraduate graduates. We couldn't find any relevant information to deduce the correct answer, so the value of ori_answer is used. Therefore, the answer is: 1999.

sub_qa pairs:
sub_q1: What is the average value of the blue bars?
sub_ans1: The average value of the blue bars is 65.
sub_q2: What is the average value of the red bars?
sub_ans2: The average value of the red bars is 72.56%.
Q: Is the average of blue bars smaller than the average of red bars?
ori_answer: Yes
Explanation: To answer the question, we need to know the average value of the blue bars and the red bars. From sub_ans1, we find the average value of the blue bars is 65. From sub_ans2, we find the average value of the red bars is 72.56%. Unify the two units, expressed as 65 and 72.56. Comparing these two values, 65 is less than 72.56. Therefore, the answer is: Yes.

sub_qa pairs:
sub_q1: What is the value of Excellent in All candidants?
sub_ans1: The value of Excellent for all candidants can be found in the table with a value of 33.
sub_q2: What is the value of Good in All candidants?
sub_ans2: The value of Good for all candidants can be found in the chart with a value of 51.
sub_q3: What is the value of Ordinary in All candidants?
sub_ans3: The key word Ordinary for all candidants can be found by looking at the middle row in the table. According to the data provided, it's nan. Therefore, based on the information available, we couldn't get the specific value of Ordinary.
Q: What is the sum value of Excellent, Good, and Ordinary in All candidants?
ori_answer: 196
Explanation: To answer the question, we need to know the value of Excellent, Good, and Ordinary in All candidants. From sub_ans1, we find the value of Excellent is 33. From sub_ans2, we can find the value of Good is 51. However, we could not find the value of Oridinary in the sub-qa pairs provided. So the ori_answer is used as the correct answer. Therefore, the answer is: 196.

Correct the ori_answer to the question according to sub_qa pairs. Please provide your explanation first, then answer the question in a short phrase starting by 'therefore, the answer is:'
Note that:
1. Please fill in the correct_answer with the shortest possible answer. If calculation is involved(such as "+", "-", "*", "/", ":"), please give specific calculation results(pay attention to the unity of the unit of account).
2. If ori_answer is correct, simply fill in ori_answer at answer.
3. If there is no relevant information or not enough information to deduce the answer, the value of ori_answer is used as the correct answer.

sub_qa pairs:
{}
Q:{}
ori_answer:{}
"""
