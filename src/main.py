from customtkinter import *

# Set appearance and color theme
set_appearance_mode("dark")
set_default_color_theme("blue")

# Create the main application window
app = CTk()
app.geometry("550x700")

# Define the font for the text input field
text_font = CTkFont(family="Arial", size=20)

# Create a text input field with the specified width, height, and font
textInputField = CTkEntry(app, width=500, height=50, corner_radius=50, font=text_font)
textInputField.pack(padx=20, pady=20)

textInputField.focus()

# Create a frame for the buttons
buttonFrame = CTkFrame(app)
buttonFrame.pack(padx=20, pady=20)

# Initialize the rm variable
rm = False

# Function to handle button clicks
def button_click(symbol):
    global rm
    if symbol not in ["=", "del", "<<", ">>"]:
        if rm:
            textInputField.delete(0, 'end')
            rm = False
        cursor_position = textInputField.index('insert')
        textInputField.insert(cursor_position, symbol)
    elif symbol == "del":
        textInputField.delete(0, 'end')
    elif symbol == "<<":
        cursor_position = textInputField.index('insert')
        if cursor_position > 0:
            textInputField.icursor(cursor_position - 1)
    elif symbol == ">>":
        cursor_position = textInputField.index('insert')
        if cursor_position > 0:
            textInputField.icursor(cursor_position + 1)
    else:
        evalthisnow = textInputField.get()
        try:
            result = eval(evalthisnow)
            textInputField.delete(0, 'end')  # Clear the text field
            textInputField.insert(0, str(result))  # Display the result
            rm = True
        except Exception as e:
            textInputField.delete(0, 'end')
            textInputField.insert(0, "Error: " + str(e))
            rm = True

# Function to create buttons in a grid
def create_buttons():
    button_texts = ["<", ">", "<<", ">>", "(", ")", "%", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", ".", "0", "del", "="]
    for i, text in enumerate(button_texts):
        button = CTkButton(buttonFrame, font=text_font, text=text, width=85, height=85, corner_radius=30, command=lambda t=text: button_click(t))
        button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

# Create and arrange the buttons
create_buttons()

# Make the window non-resizable
app.resizable(False, False)

# Start the application's main event loop
app.mainloop()
