import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


selected_questions = random.sample(question_data, 10)


question_bank = [Question(q["question"], q["correct_answer"]) for q in selected_questions]


quiz = QuizBrain(question_bank)


quiz.start_quiz()


print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")
