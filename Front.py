import tkinter as tk
from tkinter import *      


class App_start(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.shared_data = {
            "first_num": tk.StringVar(),
            "second_num": tk.StringVar()
        }

        self.frames = {}
        for F in (Encryption, Operation, Result):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Encryption")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Encryption(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logo = tk.Label(self, text="Encryption", font=('Helvetica', 30)).pack()   
        input_prompt = tk.Label(self, text="Enter your numbers here", font=('Times', 20)).pack()

        first_entry = tk.Entry(self, textvariable=self.controller.shared_data["first_num"], width=40)
        first_entry.pack()

        second_entry = tk.Entry(self, textvariable=self.controller.shared_data["second_num"], width=40)
        second_entry.pack()

        info1 = tk.Label(self, text="Your plaintext inputs will be hidden from view after encrypting").pack()
        info2 = tk.Label(self, text="Your password will be needed in order to access your results").pack()
        add_password = tk.Label(self, text="You must add a password before encrypting", font=('Times', 12)).pack()

        hide_pw = tk.StringVar()
        password_box = tk.Entry(self, textvariable=hide_pw, width=40, show='*').pack() 

        encrypt_button = tk.Button(self, text="Encrypt", font=('Times', 12), command=lambda: controller.show_frame("Operation")).pack()
        clear_button = tk.Button(self, text="Clear", font=('Times', 12), command=lambda: self.reset(hide_pw, first_entry, second_entry)).pack()

    def reset(self, pw, first, second):

        pw.set("")
        first.delete(0, tk.END)
        second.delete(0, tk.END)


class Operation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        back = tk.Button(self, text="Back", font=('Times', 12), command=lambda: controller.show_frame("Encryption")).pack()
        logo = tk.Label(self, text="Encryption", font=('Helvetica', 30)).pack()
        message_prompt = tk.Label(self, text="Here are your encrypted numbers", font=('Times, 16')).pack()

        first_enc = self.controller.shared_data["first_num"].get()
        first_label = tk.Label(self, text="Some encrypted value 1").pack()

        second_enc = self.controller.shared_data["second_num"].get()
        second_label = tk.Label(self, text="Some encrypted value 2").pack()

        add_button = tk.Button(self, text="Addition", command=lambda: controller.show_frame("Result")).pack()
        mult_button = tk.Button(self, text="Multiplication", command=lambda: controller.show_frame("Result")).pack()


class Result(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        back = tk.Button(self, text="Back", font=('Times', 12), command=lambda: controller.show_frame("Operation")).pack()
        logo = tk.Label(self, text="Encryption", font=('Helvetica', 30)).pack()
        enc_msg = tk.Label(self, text="Here is your encrypted result", font=('Helvetica', 20)).pack()

        result = tk.Label(self, text="Some encrypted answer", width=40).pack()

        decrypt_button = tk.Button(self, text="Decrypt", font=('Times', 12)).pack()
        dec_msg = tk.Label(self, text="Here is your decrypted result", font=('Times', 12)).pack()

        dec_result = tk.Entry(self, width=40)
        dec_result.pack()

        restart = tk.Button(self, text="Restart", font=('Times', 12), command=lambda: controller.show_frame("Encryption")).pack()


# class Saved(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller    

#         back = tk.Button(self, text="Back", font=('Times', 12), command=lambda: controller.show_frame("Result")).pack()
#         logo = tk.Label(self, text="Encryption", font=('Helvetica', 30)).pack()
#         saved_msg = tk.Label(self, text="Here are your saved results:", font=('Times', 12)).pack()
#         results = tk.Text(self, width=40).pack()


if __name__ == "__main__":
    app = App_start()
    app.mainloop()