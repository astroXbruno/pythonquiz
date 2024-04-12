class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.current_question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.current_question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.current_question_number]
        self.current_question_number += 1
        user_answer = input(f"Q.{self.current_question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == str(correct_answer).lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

    def start_quiz(self):
        while self.still_has_questions():
            self.next_question()
