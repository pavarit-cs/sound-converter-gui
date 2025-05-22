import tkinter as tk
from tkinter import filedialog

# --- Setting Main Window ---
app = tk.Tk()
app.title("Sound Converter")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 450
x_coordinate = (screen_width // 2) - (WINDOW_WIDTH // 2)
y_coordinate = (screen_height // 2) - (WINDOW_HEIGHT // 2)
app.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_coordinate}+{y_coordinate}')
app.resizable(False, False)

# --- value for GUI ---
input_path = tk.StringVar()
output_path = tk.StringVar()
output_type = ["wav", "mp3", "m4a"]
output_format = tk.StringVar()
output_format.set(output_type[0])

# --- Function handlers ---
def open_file_dialog():
    input_path.set(filedialog.askopenfilename(initialdir="Downloads", filetypes=(
        ("All supported audio files", "*.wav *.mp3 *.m4a"),
        ("wav files", "*.wav"),
        ("mp3 files", "*.mp3"),
        ("m4a files", "*.m4a"))))

    if input_path:
        label_input_select.config(text=f"{output_path}")

# --- Widgets for GUI ---
label_greeting = tk.Label(text='Welcome to Sound Converter!')
label_greeting.pack(pady=50)

button_openfile = tk.Button(app, text="Select your file", command=open_file_dialog)
button_openfile.pack(pady=10)
label_input_select = tk.Label(app, textvariable=input_path, font=("Courier New", 11), fg="red")
label_input_select.pack(pady=5)

dropdown_menu = tk.OptionMenu(app, output_format, *output_type)
dropdown_menu.pack(pady=20)
button_convert = tk.Button(app,
                           text="convert",
                           font=("Arial", 18),
                           fg="white",
                           bg="#4CAF50",
                           activebackground="#45a049",
                           activeforeground="white",
                           relief="raised",
                           borderwidth=4, )
button_convert.pack(pady = 20)




# --- Looper for tkinter ---
app.mainloop()