import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.construct_ui()

    def construct_ui(self):
        """ Builds the UI """
        # Interface
        self.root = Tk()
        self.root.title('Flashcard Language app 🇪🇸󠁧󠁿')
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text=f'Score: {self.quiz.score}', font=('Arial', 10, 'normal'), bg=THEME_COLOR)
        self.label_score.grid(row=1, column=2, pady=(0, 15))

        self.content = Canvas(width=300, height=250, bg = '#fff')
        self.content_text = self.content.create_text(150, 125,
                                                     width=260,
                                                     text='this is some example text',
                                                     font=('Arial', 20, 'italic'),
                                                     fill='black')
        self.content.grid(row=2, column=1, columnspan=2)

        button_wrong = PhotoImage(file='./images/false.png')
        button_right = PhotoImage(file='./images/true.png')

        self.button_wrong = Button(image=button_wrong, highlightthickness=0, border=0, command=self.chose_false)
        self.button_right = Button(image=button_right, highlightthickness=0, border=0, command=self.chose_true)

        self.button_wrong.grid(row=3, column=1, pady=(20, 0))
        self.button_right.grid(row=3, column=2, pady=(20, 0))

        self.next_question()

        self.root.mainloop()

    def next_question(self) -> None:
        """ Display a question in the content frame """
        self.content.config(bg='white')
        self.label_score.config(text=f'score: {self.quiz.score}')

        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.content.itemconfig(self.content_text, text=question)
        else:
            message = f""" All questions are asked! Your final score is {self.quiz.score} """
            self.content.itemconfig(self.content_text, text=message)
            self.button_right.config(state=DISABLED)
            self.button_wrong.config(state=DISABLED)



    def chose_false(self):
        """ Clicked the false button """
        return self.give_feedback(self.quiz.check_answer('False'))

    def chose_true(self):
        """ Clicked the True button """
        return self.give_feedback(self.quiz.check_answer('True'))

    def give_feedback(self, answer) -> None:
        """ Checks if the given answer is correct """

        if answer:
            self.content.config(bg='green')
        else:
            self.content.config(bg='red')

        self.root.after(500, self.next_question)
