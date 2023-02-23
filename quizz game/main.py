from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]

for question in question_data:
    qestion_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(q_text=qestion_text,q_answer=question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()


