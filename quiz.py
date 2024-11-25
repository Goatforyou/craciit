import tkinter as tk
from tkinter import messagebox
import random

# Sample questions
questions = {
    "simple": [
        {"question": "What is the value of sin(90 degrees)?", "options": ["0", "1", "√2", "√3"], "answer": "1"},
        {"question": "Which of the following is a noble gas?", "options": ["Oxygen", "Hydrogen", "Neon", "Nitrogen"], "answer": "Neon"},
        {"question": "What is the boiling point of water?", "options": ["100°C", "0°C", "50°C", "200°C"], "answer": "100°C"},
        {"question": "What is 3 + 5?", "options": ["7", "8", "9", "10"], "answer": "8"},
        {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": "Delhi"},
        {"question": "What is 10% of 200?", "options": ["10", "20", "30", "40"], "answer": "20"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "answer": "H2O"},
        {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"], "answer": "Blue Whale"},
        {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
        {"question": "What is the freezing point of water?", "options": ["0°C", "32°F", "100°F", "100°C"], "answer": "0°C"},
        {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"question": "What is the square root of 16?", "options": ["2", "3", "4", "5"], "answer": "4"},
        {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Pound"], "answer": "Yen"},
        {"question": "Which is the smallest planet in our solar system?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"},
        {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
        {"question": "Which element has the atomic number 1?", "options": ["Hydrogen", "Helium", "Oxygen", "Carbon"], "answer": "Hydrogen"},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
        {"question": "What is the main ingredient in guacamole?", "options": ["Tomato", "Avocado", "Onion", "Pepper"], "answer": "Avocado"},
        {"question": "Which animal is known as the King of the Jungle?", "options": ["Tiger", "Lion", "Elephant", "Bear"], "answer": "Lion"},
        {"question": "What is the fastest land animal?", "options": ["Cheetah", "Lion", "Horse", "Elephant"], "answer": "Cheetah"},
        {"question": "Which is the largest desert in the world?", "options": ["Sahara", "Gobi", "Arabian", "Antarctic"], "answer": "Sahara"},
        {"question": "What is the capital of Italy?", "options": ["Venice", "Florence", "Rome", "Milan"], "answer": "Rome"},
        {"question": "What is the primary gas in the Earth's atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Nitrogen"},
]}

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.master.geometry("400x400")
        self.current_question = 0
        self.score = 0
        self.difficulty = ""
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Select Difficulty Level", font=("Arial", 16))
        self.label.pack(pady=20)

        self.simple_button = tk.Button(self.master, text="Simple", command=lambda: self.start_quiz("simple"))
        self.simple_button.pack(pady=5)

        self.hard_button = tk.Button(self.master, text="Hard", command=lambda: self.start_quiz("hard"))
        self.hard_button.pack(pady=5)

        self.advanced_button = tk.Button(self.master, text="Advanced", command=lambda: self.start_quiz("advanced"))
        self.advanced_button.pack(pady=5)

    def start_quiz(self, level):
        self.difficulty = level
        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        if self.current_question < len(questions[self.difficulty]):
            question_data = questions[self.difficulty][self.current_question]
            self.clear_frame()
            self.label = tk.Label(self.master, text=question_data["question"], font=("Arial", 14))
            self.label.pack(pady=20)

            for option in question_data["options"]:
                button = tk.Button(self.master, text=option, command=lambda opt=option: self.check_answer(opt))
                button.pack(pady=5)

        else:
            self.show_score()

    def check_answer(self, selected_option):
        correct_answer = questions[self.difficulty][self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            self.show_feedback("Correct!", "green")
        else:
            self.show_feedback("Wrong!", "red")
        self.current_question += 1
        self.master.after(1000, self.show_question)

    def show_feedback(self, message, color):
        feedback_label = tk.Label(self.master, text=message, fg=color, font=("Arial", 14))
        feedback_label.pack(pady=20)
        self.master.after(1000, feedback_label.destroy)

    def show_score(self):
        self.clear_frame()
        score_label = tk.Label(self.master, text=f"Your score: {self.score}/{len(questions[self.difficulty])}", font=("Arial", 16))
        score_label.pack(pady=20)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
