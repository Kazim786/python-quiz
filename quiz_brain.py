from main import question_bank

class QuizBrain:
    def __init__ (self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self, text, answer, question_bank):
        self.question_number += 1
        for question in question_bank:
            print(f"Q.{self.question_number}: {question_bank[question].text}")
            answer = input("(True/False)?")
            if answer != question_bank[question].answer:
                print("Incorrect answer")

# a_question = Question(question["text"], question["answer"])


