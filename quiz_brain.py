from main import question_bank

class QuizBrain:
    #question_list
    def __init__ (self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # current_question
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?")
            #answer = input(f"Q.{self.question_number}: {question_bank[question].text} (True/False)?")

# a_question = Question(question["text"], question["answer"])


#  for question in current_question:
#             answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?")
#             #answer = input(f"Q.{self.question_number}: {question_bank[question].text} (True/False)?")

#             # answer = input("(True/False)?")
#             if answer != question_bank[question].answer:
#                 print("Incorrect answer")