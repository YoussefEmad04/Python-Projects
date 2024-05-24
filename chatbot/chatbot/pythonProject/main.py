import json
from difflib import get_close_matches
import tkinter as tk
from tkinter import scrolledtext, messagebox

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def submit_question():
    user_input = entry.get()
    if user_input.lower() == 'quit':
        root.quit()
        return

    best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

    if best_match:
        answer = get_answer_for_question(best_match, knowledge_base)
        chat_log.insert(tk.END, f"You: {user_input}\n")
    else:
        chat_log.insert(tk.END, f"You: {user_input}\n")
        chat_log.insert(tk.END, "Bot: I don't know the answer, can you teach me?\n\n")
        messagebox.showinfo("Teach Bot", "I don't know the answer. Please provide the answer or skip.")

def teach_answer():
    user_input = entry.get()
    new_answer = answer_entry.get()
    if new_answer.lower() != "skip":
        knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
        save_knowledge_base("knowledge_base.json", knowledge_base)
        chat_log.insert(tk.END, f"Bot: Thank you! I have learned a new response.\n\n")
    else:
        chat_log.insert(tk.END, "Bot: Skipped learning new response.\n\n")
    answer_entry.delete(0, tk.END)

knowledge_base = load_knowledge_base('knowledge_base.json')

root = tk.Tk()
root.title("Chat Bot")
root.geometry("500x400")
root.configure(bg="#001f3f")

chat_frame = tk.Frame(root, bg="#001f3f")
chat_frame.pack(pady=10)

chat_log = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=60, height=15, bg="#003366", fg="white")
chat_log.pack()

entry_frame = tk.Frame(root, bg="#001f3f")
entry_frame.pack(pady=5)

entry_label = tk.Label(entry_frame, text="You: ", bg="#001f3f", fg="white")
entry_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(entry_frame, width=40, bg="#00509e", fg="white")
entry.grid(row=0, column=1, padx=5)

submit_button = tk.Button(entry_frame, text="Submit", command=submit_question, bg="#0074d9", fg="white")
submit_button.grid(row=0, column=2, padx=5)

answer_label = tk.Label(entry_frame, text="Answer: ", bg="#001f3f", fg="white")
answer_label.grid(row=1, column=0, padx=5)

answer_entry = tk.Entry(entry_frame, width=40, bg="#00509e", fg="white")
answer_entry.grid(row=1, column=1, padx=5)

teach_button = tk.Button(entry_frame, text="Teach", command=teach_answer, bg="#0074d9", fg="white")
teach_button.grid(row=1, column=2, padx=5)

root.mainloop()
