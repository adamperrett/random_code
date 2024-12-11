import pandas as pd
import random
import tkinter as tk
from tkinter import ttk
from time import sleep

# Load the CSV file
data = pd.read_csv('BRC_Collaboration_Raffle_Submissions_2024-12-11.csv')  # Replace 'your_file.csv' with the actual CSV file path


# Function to run the raffle
def run_raffle():
    # Reset the winner label for a new spin
    winner_label['text'] = ""

    # Create a spinning effect
    for _ in range(20):  # Adjust the range for longer or shorter spinning
        random_index = random.randint(0, len(data) - 1)
        spinning_label['text'] = f"Shuffling:\n{data.iloc[random_index]['Name of first co-author']} & {data.iloc[random_index]['Name of second co-author']}" \
                                 f"\n\n{data.iloc[random_index]['Enter a combination of research areas']}"
        spinning_label.update()
        sleep(0.1)

    # Select a random winner
    winner_index = random.randint(0, len(data) - 1)
    winner = data.iloc[winner_index]

    # Hide the spinning label and display the winner
    spinning_label['text'] = ""
    winner_label['text'] = f"Winner:\n{winner['Name of first co-author']} & {winner['Name of second co-author']}\n\n{winner['Enter a combination of research areas']}"

# GUI setup
root = tk.Tk()
root.title("Research Raffle")

# Ensure the window resizes gracefully
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Center the content
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Spinning label
spinning_label = ttk.Label(frame, text="Press the button to spin!", font=("Helvetica", 24), anchor="center", justify="center")
spinning_label.grid(row=0, column=0, pady=10, sticky="nsew")

# Raffle button
raffle_button = ttk.Button(frame, text="Run Raffle", command=run_raffle)
raffle_button.grid(row=1, column=0, pady=10, sticky="nsew")

# Winner label
winner_label = ttk.Label(frame, text="", font=("Helvetica", 26), foreground="green", anchor="center", justify="center")
winner_label.grid(row=2, column=0, pady=20, sticky="nsew")

# Start the application
root.mainloop()
