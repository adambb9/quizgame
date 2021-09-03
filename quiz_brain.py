#make a quiz machine using OOP and questions that can be taken easily from the internet
class Quizbrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(f"The current question number is: {self.question_number}")
        input(f"{current_question.text} (True/False): ")

