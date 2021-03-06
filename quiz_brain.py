
class QuizBrain:
    #question_list
    def __init__ (self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        while self.question_number < len(self.question_list):
            return True


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # current_question
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?")
            #answer = input(f"Q.{self.question_number}: {question_bank[question].text} (True/False)?")
        self.check_answers(answer, current_question.answer)

    def check_answers(self, user_answer, right_answer):
        
        if user_answer.lower() != right_answer.lower():
            print(f"Answer is wrong. Correct answer: {right_answer.lower()}")
        else:
            print("Answer is right")
            self.score +=  1
        print(f"Your score so far is {self.score}/{self.question_number}")
        print("\n")
        if self.question_number == len(self.question_list):
            print(f"You have finished the quiz, your final score is {self.score}")
        






