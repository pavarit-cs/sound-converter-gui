import tkinter as tk

#Setting Main Window
app = tk.Tk()
app.title("Sound Converter")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 450
x_coordinate = (screen_width // 2) - (WINDOW_WIDTH // 2)
y_coordinate = (screen_height // 2) - (WINDOW_HEIGHT // 2)
app.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_coordinate}+{y_coordinate}')


label_greeting = tk.Label(text='Welcome!')
label_greeting.pack()

app.resizable(False, False)
app.mainloop()