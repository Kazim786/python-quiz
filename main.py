from question_model import Question
from data import question_data

question_bank = []



for question in question_data:
    # print(question["text"])
    a_question = Question(question["text"], question["answer"])

    question_bank.append(a_question)

# print(len(question_bank))
print(question_bank)
#Did it by myself 

