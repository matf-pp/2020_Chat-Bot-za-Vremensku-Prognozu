from tkinter import *
from tkinter import ttk 


def init_gui():
    root = Tk()
    root.title('Weather ChatBot')

    frame_root = ttk.Frame(root)
    frame_root.pack(fill = BOTH, expand = TRUE)

    #? TextBox
    frame_chat_history = ttk.Frame(root, padding = (10, 10, 10, 10))
    frame_chat_history.pack(side = TOP, fill = BOTH, expand = TRUE)    

    text_chat_history = Text(frame_chat_history)
    text_chat_history.pack(fill = BOTH, expand = TRUE)
    
    #? Send Message
    frame_send_message = ttk.Frame(root, padding = (10, 0, 10, 10))
    frame_send_message.pack(side = BOTTOM, fill = BOTH, expand = TRUE)

    entry_send_message = ttk.Entry(frame_send_message)
    entry_send_message.pack(side = LEFT, fill = BOTH, expand = TRUE)

    btn_send_message = ttk.Button(frame_send_message, text = 'Send')
    btn_send_message.pack(side = RIGHT, fill = BOTH, padx = 10)
    

    root.mainloop()

if __name__ == "__main__":
    init_gui()