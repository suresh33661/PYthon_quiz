import tkinter as tk
from tkinter import messagebox

# Define quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_choice": "Paris",
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_choice": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["Elephant", "Giraffe", "Whale Shark", "Blue Whale"],
        "correct_choice": "Blue Whale",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.question_index = 0
        self.score = 0

        # Configure colors and fonts
        self.root.configure(bg="#1E90FF")  # Background color
        self.question_color = "#FFFFFF"     # Question text color
        self.button_color = "#32CD32"       # Button background color
        self.button_text_color = "#FFFFFF"  # Button text color

        # Create and configure widgets
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14), fg=self.question_color, bg=root.cget("bg"))
        self.question_label.pack()

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), bg=self.button_color, fg=self.button_text_color, command=lambda i=i: self.check_answer(i))
            self.choice_buttons.append(button)
            button.pack()

        self.next_button = tk.Button(root, text="Next Question", font=("Arial", 12), bg=self.button_color, fg=self.button_text_color, state=tk.DISABLED, command=self.next_question)
        self.next_button.pack()

        self.display_question(0)

    def display_question(self, index):
        if index < len(questions):
            self.question_index = index
            question_data = questions[index]
            self.question_label.config(text=question_data["question"])

            for i in range(4):
                self.choice_buttons[i].config(text=question_data["choices"][i])

            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Quiz Complete", f"Your Score: {self.score}/{len(questions)}")

    def check_answer(self, choice):
        question_data = questions[self.question_index]
        selected_choice = question_data["choices"][choice]
        correct_choice = question_data["correct_choice"]

        if selected_choice == correct_choice:
            self.score += 1

        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.display_question(self.question_index + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
