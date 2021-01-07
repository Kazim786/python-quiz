class Question:
    def __init__ (self, text, answer):
        self.text = text 
        self.answer = answer 




#Method syntax example
    # def follow(self, user):
    #     user.followers += 1
    #     self.following += 1



question_1 = Question("is 2+3=5?", "True")

print(question_1.text)

answer = input("Is the answer True or False?")
if answer == question_1.answer:
    print("You got it correct")

    