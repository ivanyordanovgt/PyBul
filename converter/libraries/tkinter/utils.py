import tkinter as tk
import winsound


class Message_data:
    def __init__(self, icon, sound):
        self.icon = icon
        self.sound = sound

MESSAGE_DATA = {
    "error": Message_data("❌", winsound.MB_ICONHAND),
    "warning": Message_data("⚠️", winsound.MB_ICONEXCLAMATION),
    "info": Message_data("☑️", winsound.MB_OK)
}

"покажи съобщение с текст 'Не може така!' с бутони 'ок', 'чао' "


def display_error_message(
        title="warning", 
        message="An unexpected error occurred.", 
        x=100, y=100, 
        buttons=None,
        photo_path=None
        ):
    if title.lower() not in MESSAGE_DATA.keys():
        title = 'info'
    message_data: Message_data = MESSAGE_DATA[title.lower()]
    winsound.MessageBeep(message_data.sound)

    if buttons is None:
        buttons = [{"label": "OK", "command": lambda: None}] 

    root = tk.Tk()
    root.title(title)
    
    root.geometry(f"500x200+{x}+{y}")
    root.resizable(False, False)
    root.configure(bg="white")

    frame = tk.Frame(root, bg="white")
    frame.place(x=15, y=15, relwidth=1, relheight=1)
    error_params = {
        "font": ("Segoe UI", 30),
        "width": 4,
        "bg": "white"
    }
    if photo_path:
        error_params['image'] = tk.PhotoImage(file=photo_path)
    else: 
        error_params['text'] = message_data.icon
        
    error_icon = tk.Label(frame, **error_params)
    error_icon.place(x=0, y=20)

    message_label = tk.Label(frame, text=message, bg="white", fg="black", font=("Segoe UI", 11), anchor="w", wraplength=350)
    message_label.place(x=90, y=30, width=380)  # Positioned next to the icon

    button_x = 15
    for i, button in enumerate(buttons):
        print("---> BUTTON:", button)
        button_widget = tk.Button(
            root,
            text=button["label"], 
            command=lambda cmd=button["command"]: (cmd(), root.destroy()),  # Close the window after button press
            font=("Segoe UI", 10), 
            bg="white", 
            relief="raised", 
            width=10
        )
        button_widget.place(x=button_x, y=150)
        button_x += 105

    # Run the Tkinter event loop
    root.mainloop()

# Example usage
# display_error_message(
#     "warning",
#     "An unexpected error occurred. Please contact support. This message should wrap properly.",
#     500, 
#     200, 
#     buttons=[ 
#         {"label": "Retry", "command": lambda: print("Retry clicked")},
#         {"label": "Cancel", "command": lambda: print("Cancel clicked")}
#     ]
# )
