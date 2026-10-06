import tkinter as tk

# ---------------- QUESTIONS ----------------

questions = [
    {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    {
        "question": "What's next?\n2, 4, 6, 8, ?",
        "answer": "10"
    },
    {
        "question": "What is the deepest point in the ocean?",
        "answer": "challenger deep"
    }
]

score = 0
current_question = 0


# ---------------- FUNCTIONS ----------------

def submit_answer():
    global score

    answer = entry.get().lower().strip()
    correct_answer = questions[current_question]["answer"]

    if answer == correct_answer:
        score += 1
        result_label.config(text="Correct! ✓")
    else:
        result_label.config(text="Wrong! ✗")

    entry.delete(0, tk.END)

    next_button.config(
        text="Next Question",
        command=next_question
    )


def next_question():
    global current_question

    current_question += 1

    if current_question >= len(questions):
        show_result()
        return

    question_label.config(
        text=questions[current_question]["question"]
    )

    progress_label.config(
        text=f"Question {current_question + 1}/3"
    )

    result_label.config(text="")

    next_button.config(
        text="Submit Answer",
        command=submit_answer
    )


def show_result():

    question_label.config(
        text=f"Test Complete!\n\nScore: {score}/3"
    )

    progress_label.config(text="RESULT")

    if score <= 1:
        rank = "NOOB"
    elif score == 2:
        rank = "NORMAL"
    else:
        rank = "ELITE"

    result_label.config(
        text=f"Your Rank: {rank}"
    )

    entry.pack_forget()
    next_button.pack_forget()


# ---------------- WINDOW ----------------

root = tk.Tk()

root.title("Simple IQ Logic Test")
root.geometry("500x500")
root.resizable(False, False)


# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="🧠 IQ LOGIC TEST",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=30)


# ---------------- PROGRESS ----------------

progress_label = tk.Label(
    root,
    text="Question 1/3",
    font=("Arial", 12)
)

progress_label.pack()


# ---------------- QUESTION ----------------

question_label = tk.Label(
    root,
    text=questions[0]["question"],
    font=("Arial", 18, "bold"),
    wraplength=400
)

question_label.pack(pady=40)


# ---------------- ANSWER BOX ----------------

entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25
)

entry.pack()


# ---------------- RESULT ----------------

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)

result_label.pack(pady=20)


# ---------------- BUTTON ----------------

next_button = tk.Button(
    root,
    text="Submit Answer",
    font=("Arial", 14),
    width=20,
    command=submit_answer
)

next_button.pack(pady=10)


# ---------------- CREATOR CREDIT ----------------

credit_label = tk.Label(
    root,
    text="Made by Lavya Savaliya\n06/10/2026",
    font=("Arial", 9)
)

credit_label.place(
    relx=0.98,
    rely=0.96,
    anchor="se"
)


# ---------------- START APP ----------------

root.mainloop()
