from question_model import Question


class QuizBrain:

    def __init__(self, question_list: [Question]):
        self.score = 0
        self.idx = 0
        self.question_list = question_list

    def next_question(self) -> None:
        """ Serves the next question in the questions_list. (Starting at index: 0) """

        # Get current question
        question: Question = self.question_list[self.idx]

        # Increase index
        self.idx += 1

        # Ask question
        answer: str = input(f"Q {self.idx}: {question.text} 'true' or 'false' ? : ")

        # Check answer
        self.check_answer(answer, question.answer)

    def questions_left(self) -> bool:
        """ Show if there are still questions to be asked. """
        return self.idx < (len(self.question_list))

    def check_answer(self, user_answer: str, question_answer: str):
        """ Check if the answer on a given question is correct """
        if user_answer.lower() == question_answer.lower():
            print('Correct Answer')
            self.score += 1
        else:
            print('Incorrect Answer')

        print(f"The correct answer is {question_answer}")
        print(f"Your current score is: {self.score} / {self.idx}")
        print("\n"*2)

    def printFinalScore(self) -> None:
        """ This function should be called after the quiz is done. This function presents the final score """
        print(f"You've completed the quiz!")
        print(f"Your final score is {self.score} / {self.idx}")


