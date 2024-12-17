# if len(subQ)==n, n>1
# for subQ_i,i<n, using template
template = """
Analyze the chart and review the table, then answer the following questions. Additionally, if the table contains untrusted values, get the relevant values from chart.
here is the table in JSON format:
{}

Q: {}

"""


# when i==n, using final_nsub
final_nsub = """
Analyze the chart to answer the question no more than three words.
Part of the analysis results of the chart are provided below. You can refer to the chart, table and some sub-QA pairs(the table and sub-QA pairs are not guaranteed to be exactly right) to get the final answer.
Additionally, if the table contains untrusted or Nan values, get the relevant values from chart.

This is a table in JSON format:
{}

sub-QA pairs for the chart:
{}

Q: {}
a short answer is:
"""


# if there is no subQ, using final_0sub
final_0sub = """Here is the chart and its associated table to answer this question. Please provide your explanation first, then answer the question step by step.
table in JSON format:
{}

Q: {}
the final short answer should start with "the answer is ".
"""
