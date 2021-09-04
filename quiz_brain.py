#make a quiz machine using OOP and questions that can be taken easily from the internet
class Quizbrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.number_of_questions = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
    
    def current_score(self, answer):
        #if answer == current.question.answer
        if answer == current_question.ander:
            self.score += 1
            print(f"You are correct. Your score is: {self.score}")
        else:
            print(f"You are correct. Your score is: {self.score}")


    

