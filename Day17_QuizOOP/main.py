
# Imports
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = [Question(q['question'], q['correct_answer']) for q in question_data]
quiz = QuizBrain(questions)

while quiz.questions_left():
    quiz.next_question()

quiz.printFinalScore()