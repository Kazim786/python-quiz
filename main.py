from question_model import Question
from data import question_data

question_bank = []

#for loop in python
# all_fruits = ["apple",
# "banana", "orange"]
# for fruit in all_fruits:
# print(fruit)

#Appending to a list
# all_fruits = ["apple",
# "banana", "orange"]
# all_fruits.append("pear")

for question in question_data:
    # print(question["text"])
    a_question = Question(question["text"], question["answer"])

    question_bank.append(a_question)

# print(len(question_bank))
print(question_bank)

