from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question (question_text,question_answer)
    question_bank.append(new_question)

new_qbo = QuizBrain(question_bank)
while new_qbo.still_has_questions():
    new_qbo.next_question()

print("Quiz is completed")
print(f"The final score is : {new_qbo.score}/{new_qbo.question_number}")


