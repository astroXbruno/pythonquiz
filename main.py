import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Randomly select 10 questions from question_data
selected_questions = random.sample(question_data, 10)

# Create Question objects for selected questions
question_bank = [Question(q["question"], q["correct_answer"]) for q in selected_questions]

# Initialize the quiz brain with the question bank
quiz = QuizBrain(question_bank)

# Start the quiz
quiz.start_quiz()

# Display the final score
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")
