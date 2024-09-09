import tkinter as tk
from tkinter import messagebox, filedialog
import random
import time
import os
import sys

from PIL import ImageTk, Image

# Sample sentences for typing practice
EASY_SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast is a useful skill.",
    "The sky is blue and clear.",
    "Cats love to play with yarn.",
    "She sells seashells by the seashore.",
    "A stitch in time saves nine.",
    "Time flies when you are having fun.",
    "Reading books can expand your mind.",
    "Practice makes perfect.",
    "Birds sing beautifully in the morning.",
    "The sun rises in the east.",
    "A rolling stone gathers no moss.",
    "The grass is greener on the other side.",
    "An apple a day keeps the doctor away.",
    "Actions speak louder than words.",
    "Silence is golden.",
    "A picture is worth a thousand words.",
    "All that glitters is not gold.",
    "Beauty is in the eye of the beholder.",
    "Better late than never.",
    "Cleanliness is next to godliness.",
    "Fortune favors the bold.",
    "Haste makes waste.",
    "Honesty is the best policy.",
    "Knowledge is power.",
    "Laughter is the best medicine.",
    "Patience is a virtue.",
    "Practice makes a man perfect.",
    "Rome was not built in a day.",
    "The early bird catches the worm."
]
MEDIUM_SENTENCES = [
    "Python is an interpreted high-level programming language.",
    "Artificial Intelligence is transforming the world.",
    "The five boxing wizards jump quickly.",
    "Machine learning algorithms can predict outcomes accurately.",
    "Data structures like lists and dictionaries are fundamental in Python.",
    "The internet has revolutionized the way we communicate.",
    "Software development requires logical thinking and problem-solving skills.",
    "Learning new languages opens doors to different cultures and perspectives.",
    "Technology is evolving at an unprecedented pace in the modern era.",
    "Algorithms are step-by-step procedures for solving specific problems.",
    "The brain is an incredibly complex organ responsible for our thoughts.",
    "Climate change is a pressing issue that requires immediate action.",
    "Physics explains the fundamental laws that govern the universe.",
    "Astronomy involves the study of stars, planets, and galaxies.",
    "The scientific method involves observation, experimentation, and analysis.",
    "Mathematics is the language of the universe, explaining patterns and phenomena.",
    "Robotics integrates multiple disciplines to create autonomous machines.",
    "Understanding human psychology is key to effective communication.",
    "The economy influences the daily lives of people around the world.",
    "Artificial neural networks are inspired by the human brain's structure.",
    "Quantum computing could revolutionize computational power and efficiency.",
    "Cybersecurity is essential in protecting sensitive data from hackers.",
    "Biotechnology is leading to advances in medicine and healthcare.",
    "Philosophy explores the fundamental nature of knowledge and existence.",
    "The human body is made up of trillions of cells, each with its function.",
    "The history of ancient civilizations provides insight into human development.",
    "Genetic engineering allows us to modify the DNA of living organisms.",
    "Renewable energy sources are vital for sustainable development.",
    "Understanding different programming paradigms can enhance coding skills.",
    "Natural language processing enables computers to understand human language."
]
HARD_SENTENCES = [
    "How razorback-jumping frogs can level six piqued gymnasts!",
    "Jinxed wizards pluck ivy from the big quilt.",
    "Crazy Fredrick bought many very exquisite opal jewels.",
    "The vexingly quick wizard jumped over a lazy ox.",
    "Amazingly few discotheques provide jukeboxes for visitors' enjoyment.",
    "Exquisite turquoise jewelry was found in a quaint curio shop.",
    "Jack quickly amazed the few by exploring novel glyphs.",
    "Bright vixens jump; dozy fowl quack while the boy jams.",
    "Few quips galvanized the hazy lynx into jumping bravely.",
    "The journey of a thousand miles begins with a single step.",
    "A jovial fisherman quickly vexed the whimsical judge.",
    "My watchful eyes gazed upon the overzealous sphinx of Egypt.",
    "Quick jabs perplexed the zany fighter in a boxing match.",
    "A wizard’s quirky fox jumps over the very high moon.",
    "The unique blacksmith can jinx quartz into elaborate jewels.",
    "Puzzling oxen jumped quickly after consuming herbal elixirs.",
    "Sphinx of black quartz, judge my very vexingly perplexed wizard!",
    "The job of waxing linoleum frequently puzzles experts in chemistry.",
    "Six sharp sharks jumped over a quirky but perplexed quail.",
    "Five jumping wizards vex the quick thinking boxer in a match.",
    "Jumping jacks, zigzagging ducks, and quirky oxen all kept quiet.",
    "A dozen zippy quick jabs puzzled the mighty boxing champ.",
    "Oddly exquisite nymphs wave loving firefly quartz-jewels at the crowd.",
    "Jumpy dogs vex hard when they see fuzzy wizards fly by.",
    "The quick brown fox jumps over the jagged quartz of the hill.",
    "Wizards enchant bumpy frogs to quickly jump over jagged rocks.",
    "Jack’s jazzy movements puzzled a vexingly wise Sphinx of quartz.",
    "Victor quickly jinxed the haunted wizard with bizarre glyphs.",
    "A zephyr flew quietly across the perplexed jumping wizard's path.",
    "The perplexed wizard jinxes the quick and quirky jumping frogs."
]


class TypingPracticeApp:
    def __init__(self, root):
        self.root = root
        # Determine if the application is running as a bundled executable
        if getattr(sys, 'frozen', False):
            # Running as a bundled executable
            icon_path = os.path.join(sys._MEIPASS, "keyboard_4316.ico")
        else:
            # Running as a script
            script_dir = os.path.dirname(__file__)
            icon_path = os.path.join(script_dir, "keyboard_4316.ico")


        # Set the icon for the window

        self.root.iconbitmap(bitmap=icon_path)
        self.root.configure(bg='black')
        self.image = tk.PhotoImage(file=r"typing_pro_imges/bg.png")
        self.img_lbl = tk.Label(self.root, image=self.image, bg="black")
        self.img_lbl.place(x=0, y=0)
        self.root.title("Typing Pro")
        self.root.geometry("804x511")
        self.root.resizable(False, False)  # Make the window non-resizable
        self.current_sentence = ""
        self.start_time = None
        self.timer_running = False
        self.user_data = []  # To store progress data

        # Create UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Difficulty Level Option Frame
        self.difficulty_var = tk.StringVar(value="easy")

        # Radio Buttons for Difficulty Levels
        self.easy_image_normal = tk.PhotoImage(file=r"typing_pro_imges/easy_normal.png")
        self.easy_image_pressed = tk.PhotoImage(file=r"typing_pro_imges/easy_pressed.png")
        self.medium_image_normal = tk.PhotoImage(file=r"typing_pro_imges/medium_normal.png")
        self.medium_image_pressed = tk.PhotoImage(file=r"typing_pro_imges/medium_pressed.png")
        self.hard_image_normal = tk.PhotoImage(file=r"typing_pro_imges/hard_normal.png")
        self.hard_image_pressed = tk.PhotoImage(file=r"typing_pro_imges/hard_pressed.png")
        self.start_but_img = tk.PhotoImage(file=r"typing_pro_imges/start_button.png")
        self.reset_but_img = tk.PhotoImage(file=r"typing_pro_imges/reset_button.png")
        self.import_but_img = tk.PhotoImage(file=r"typing_pro_imges/import_button.png")
        "typing_pro_imges/bg.png"
        self.r1 = tk.Button(
            bg="#1E1E1E",
            activebackground="#1E1E1E",
            border=0,
            image=self.easy_image_pressed,  # Set the normal image initially
            command=lambda: self.set_difficulty("easy")  # Call the function with "easy" argument

        )
        self.r1.place(x=265, y=91)

        self.r2 = tk.Button(
            bg="#1E1E1E",
            activebackground="#1E1E1E",
            border=0,
            image=self.medium_image_normal,  # Set the normal image initially
            command=lambda: self.set_difficulty("medium")  # Call the function with "easy" argument

        )
        self.r2.place(x=358, y=91)

        self.r3 = tk.Button(
            bg="#1E1E1E",
            activebackground="#1E1E1E",
            border=0,
            image=self.hard_image_normal,  # Set the normal image initially
            command=lambda: self.set_difficulty("hard")  # Call the function with "easy" argument

        )
        self.r3.place(x=451, y=91)
        # self.r1 = tk.Radiobutton(self.difficulty_frame, text="Easy", variable=self.difficulty_var, value="easy",
        #                          font=("Arial", 12))
        # self.r2 = tk.Radiobutton(self.difficulty_frame, text="Medium", variable=self.difficulty_var, value="medium",
        #                          font=("Arial", 12))
        # self.r3 = tk.Radiobutton(self.difficulty_frame, text="Hard", variable=self.difficulty_var, value="hard",
        #                          font=("Arial", 12))

        # Align Radio Buttons in the Center and Position them Left, Center, Right

        # Sentence display
        self.sentence_label = tk.Label(self.root, text="", font=("Arial", 16), bg="#1E1E1E", foreground="white",
                                       wraplength=700, )
        self.sentence_label.pack(pady=170)

        # Input field
        self.input_text = tk.Text(self.root, height=5, width=60, fg="white",
                                  bg="#282727", border=0, font=("Arial", 14), wrap="word")
        self.input_text.place(x=70, y=205)
        self.input_text.bind("<KeyRelease>", self.check_typing)
        self.input_text.config(state=tk.DISABLED)  # Initially disabled

        # Result display
        self.result_label = tk.Label(self.root, text="", bg="#1E1E1E", foreground="white", font=("Arial", 12))
        self.result_label.place(x=300, y=330)

        # Start and Reset buttons
        self.start_button = tk.Button(self.root, image=self.start_but_img, bg="#1E1E1E",
                                      activebackground="#1E1E1E",
                                      border=0, text="Start", command=self.start_typing_test, font=("Arial", 12))
        self.start_button.place(x=288, y=382)
        self.reset_button = tk.Button(self.root, bg="#1E1E1E",
                                      activebackground="#1E1E1E",
                                      border=0,
                                      image=self.reset_but_img,
                                      text="Reset", command=self.reset, font=("Arial", 12))
        self.reset_button.place(x=362, y=382)
        self.reset_button.config(state=tk.DISABLED)  # Initially disabled

        # Theme Selection

        # Load Custom Sentences
        self.custom_button = tk.Button(self.root, bg="#1E1E1E",
                                       activebackground="#1E1E1E",
                                       border=0,
                                       image=self.import_but_img,
                                       text="Load Custom Sentences", command=self.load_custom_sentences,
                                       font=("Arial", 12))
        self.custom_button.place(x=436, y=382)
    def set_difficulty(self, difficulty):
        """Updates the difficulty variable based on the button clicked."""
        self.difficulty_var.set(difficulty)
        print(difficulty)
        # Reset all button images to normal state
        self.r1.config(image=self.easy_image_normal)
        self.r2.config(image=self.medium_image_normal)
        self.r3.config(image=self.hard_image_normal)

        # Set the pressed state image for the selected button
        if difficulty == "easy":
            self.r1.config(image=self.easy_image_pressed)
        elif difficulty == "medium":
            self.r2.config(image=self.medium_image_pressed)
        elif difficulty == "hard":
            self.r3.config(image=self.hard_image_pressed)

    def start_typing_test(self):
        # Select sentence pool based on difficulty
        difficulty = self.difficulty_var.get()
        if difficulty == "easy":
            sentence_pool = EASY_SENTENCES
        elif difficulty == "medium":
            sentence_pool = MEDIUM_SENTENCES
        else:
            sentence_pool = HARD_SENTENCES

        # Start test
        self.current_sentence = random.choice(sentence_pool)
        self.sentence_label.config(text=self.current_sentence)
        self.input_text.config(state=tk.NORMAL)  # Enable text input
        self.input_text.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()
        self.start_button.config(state=tk.DISABLED)  # Disable start button
        self.reset_button.config(state=tk.NORMAL)  # Enable reset button

    def check_typing(self, event):
        if not self.timer_running:
            return

        typed_text = self.input_text.get("1.0", tk.END).strip()
        self.highlight_errors(typed_text)

        if typed_text == self.current_sentence:
            self.timer_running = False
            self.calculate_results()

    def highlight_errors(self, typed_text):
        self.input_text.tag_remove("error", "1.0", tk.END)
        for i in range(len(typed_text)):
            if i < len(self.current_sentence) and typed_text[i] != self.current_sentence[i]:
                self.input_text.tag_add("error", f"1.{i}", f"1.{i + 1}")
                self.input_text.tag_config("error", foreground="red")

    def calculate_results(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        word_count = len(self.current_sentence.split())
        wpm = (word_count / time_taken) * 60
        typed_text = self.input_text.get("1.0", tk.END).strip()
        correct_chars = sum(
            1 for i, c in enumerate(typed_text) if i < len(self.current_sentence) and c == self.current_sentence[i])
        accuracy = (correct_chars / len(self.current_sentence)) * 100
        self.result_label.config(text=f"Time: {time_taken:.2f} seconds | WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%")
        self.input_text.config(state=tk.DISABLED)
        self.user_data.append({"wpm": wpm, "accuracy": accuracy})  # Track progress
        messagebox.showinfo("Typing Test Completed", "Great job! Check your results.")

    def reset(self):
        self.input_text.config(state=tk.DISABLED)
        self.sentence_label.config(text="")
        self.result_label.config(text="")
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.result_label.config(text=f"Time Elapsed: {elapsed_time:.2f} seconds")
            self.root.after(100, self.update_timer)  # Update every 100 ms

    def load_custom_sentences(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                custom_sentences = file.readlines()
            self.update_sentence_pool(custom_sentences)

    def update_sentence_pool(self, sentences):
        global EASY_SENTENCES, MEDIUM_SENTENCES, HARD_SENTENCES
        EASY_SENTENCES = sentences if len(sentences) < 5 else EASY_SENTENCES
        MEDIUM_SENTENCES = sentences if 5 <= len(sentences) < 8 else MEDIUM_SENTENCES
        HARD_SENTENCES = sentences if len(sentences) >= 8 else HARD_SENTENCES
        messagebox.showinfo("Custom Sentences Loaded", "Custom sentences have been successfully loaded!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingPracticeApp(root)
    root.mainloop()
