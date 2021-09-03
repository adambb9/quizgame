from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))


quiz = Quizbrain(question_bank)
quiz.next_question()

    


