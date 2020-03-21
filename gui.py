from tkinter import *
from tkinter import ttk 


def init_gui():
    root = Tk()
    root.title('Weather ChatBot')

    frame_root = ttk.Frame(root)
    frame_root.grid(column = 0, row = 0)

    frame_chat_history = ttk.Frame(root, padding = (10, 10, 10, 10))
    frame_send_message = ttk.Frame(root, padding = (10, 0, 10, 10))

    frame_chat_history.grid(column = 0, row = 0)    
    frame_send_message.grid(column = 0, row = 1)

    text_chat_history = Text(frame_chat_history)
    text_chat_history.grid(column = 0, row = 0)

    entry_send_message = ttk.Entry(frame_send_message)
    entry_send_message.grid(column = 0, row = 0)

    btn_send_message = ttk.Button(frame_send_message, text = 'Send')
    btn_send_message.grid(column = 1, row = 0)
    

    root.mainloop()

if __name__ == "__main__":
    init_gui()