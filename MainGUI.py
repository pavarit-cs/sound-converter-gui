import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
from converter import  convert_audio_file

# --- Debugging: Print Python's perceived PATH ---
#print("--- Python's PATH Environment Variable ---")
#print(os.environ.get('PATH'))


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
        label_input_select.config(text=f"{input_path}")

def update_output_path(*args):
    current_input_path = input_path.get()
    selected_format = output_format.get()

    base_name = os.path.basename(current_input_path)
    without_ext_name = os.path.splitext(base_name)[0]

    new_name = f"{without_ext_name}.{selected_format}"
    output_directory = os.path.dirname(current_input_path)
    full_output_path = os.path.join(output_directory, new_name)
    output_path.set(full_output_path)
def convert():
    convert_audio_file(input_path.get(), output_path.get(), output_format.get())
    success, message = convert_audio_file(input_path.get(), output_path.get(), output_format.get())

    if success:
        messagebox.showinfo("Success!", message)
        label_result.config(text=f"status: {message}", fg="green")
    else:
        messagebox.showerror("Error", message)
        label_result.config(text=f"status: {message}", fg="red")
# --- Widgets for GUI ---
label_greeting = tk.Label(text='Welcome to Sound Converter!')
label_greeting.pack(pady=50)

button_openfile = tk.Button(app, text="Select your file", command=open_file_dialog)
button_openfile.pack(pady=10)
label_input_select = tk.Label(app, textvariable=input_path, font=("Courier New", 11), fg="red")
label_input_select.pack(pady=5)

dropdown_menu = tk.OptionMenu(app, output_format, *output_type)
dropdown_menu.pack(pady=20)
output_format.trace("w", update_output_path)
button_convert = tk.Button(app,
                           text="convert",
                           font=("Arial", 18),
                           fg="white",
                           bg="#4CAF50",
                           activebackground="#45a049",
                           activeforeground="white",
                           relief="raised",
                           borderwidth=4,
                           command=convert)
button_convert.pack(pady = 20)
label_result = tk.Label(app, font=("success", 13), fg="green")





# --- Looper for tkinter ---
app.mainloop()