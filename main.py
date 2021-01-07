from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []



for question in question_data:
    # print(question["text"])
    a_question = Question(question["text"], question["answer"])

    question_bank.append(a_question)

# print(len(question_bank))
print(question_bank[0].text)
#Did it by myself 

# print(QuizBrain)

quiz = QuizBrain(question_bank)

# quiz.next_question()


while quiz.still_has_questions() == True:
    quiz.next_question()