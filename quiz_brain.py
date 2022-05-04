import html

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


    def next_question(self):
        self.current_question= self.questions_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        #user_answer= input(f"Q.{self.question_number}: {q_text} (True/False): ")
        #self.check_answer(user_answer,self.current_question.answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
        print(f"Right answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")


    def final_score(self, score, question_number):
        print(f"Your final score was{score},{question_number}")


