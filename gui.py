import tkinter as tk
from tkinter import ttk 

class ChatBotGUI(ttk.Frame):

    def __init__(self, root):
        self.root = root
        self.root.title('Weather ChatBot')

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
        

    def run(self):
        self.root.mainloop()

    def send_message(self):
        msg = self.entry_send_message.get()
        if len(msg) == 0:
            return
        
        self.text_chat_history.configure(state = tk.NORMAL)
        self.text_chat_history.delete(1.0, tk.END)    
        self.text_chat_history.insert(tk.END, msg)
        self.text_chat_history.configure(state = tk.DISABLED)

def main():
    root = tk.Tk()
    app = ChatBotGUI(root)
    app.run()

if __name__ == "__main__":
    main()