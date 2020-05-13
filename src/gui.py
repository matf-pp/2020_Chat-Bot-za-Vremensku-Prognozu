import tkinter as tk
from tkinter import ttk 
import messaging
import os
from typing import Tuple, List


class ChatBotGUI(ttk.Frame):

    def __init__(self, root):
        
        self.root = root
        self.root.title('Weather ChatBot')
        self.root.resizable(0, 0)
        self.root.iconbitmap(self.get_img_path())

        self.frame_root = ttk.Frame(self.root)
        self.frame_root.pack(fill = tk.BOTH, expand = tk.TRUE)

        #? TextBox
        self.frame_chat_history = ttk.Frame(self.root, padding = (10, 10, 10, 10))
        self.frame_chat_history.pack(side = tk.TOP, fill = tk.BOTH, expand = tk.TRUE)    

        self.text_chat_history = tk.Text(self.frame_chat_history)
        self.text_chat_history.pack(fill = tk.BOTH, expand = tk.TRUE)
        self.text_chat_history.configure(state = tk.DISABLED)
        
        #? Send Message
        self.frame_send_message = ttk.Frame(self.root, padding = (10, 0, 10, 10))
        self.frame_send_message.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = tk.TRUE)

        self.entry_send_message = ttk.Entry(self.frame_send_message)
        self.entry_send_message.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)

        self.btn_send_message = ttk.Button(self.frame_send_message, text = 'Send', command = self.send_message)
        self.btn_send_message.pack(side = tk.RIGHT, fill = tk.BOTH, padx = 10)
        self.root.bind('<Return>', self.send_message)
        
        self.chat_history: List[Tuple[str, str]] = []
        self.display_welcome_message()

    def get_img_path(self):
        #? linux doesn't support standard icon files
        if os.name != 'nt':
            return 
        
        current_dir = os.path.curdir
        path = os.path.join(current_dir, '../img', 'icon.ico')
        
        return path


    def run(self):
        self.root.mainloop()

    def display_welcome_message(self):
        #? user_msg is None because we don't have any user response on program start
        self.chat_history.append((None, messaging.display_welcome_message()))
        self.populate_chat()

    def send_message(self, event=None):
        msg = self.entry_send_message.get()
        if len(msg) == 0:
            return
        
        messaging_response = messaging.receive_message_and_make_response(msg)
        self.chat_history.append(messaging_response)
        self.populate_chat()
        self.entry_send_message.delete(0, tk.END)

    def populate_chat(self):
        self.text_chat_history.configure(state = tk.NORMAL)
        self.text_chat_history.delete(1.0, tk.END)    
        
        for user_msg, chatbot_res in self.chat_history:
            if user_msg:
                self.text_chat_history.insert(tk.END, user_msg)
            if chatbot_res:
                self.text_chat_history.insert(tk.END, chatbot_res)
        
        self.text_chat_history.see('end')
        self.text_chat_history.configure(state = tk.DISABLED)

def main():
    root = tk.Tk()
    app = ChatBotGUI(root)
    app.run()

if __name__ == "__main__":
    main()