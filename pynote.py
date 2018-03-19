from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class Notepad:

    def __init__(self, root):
        # create window
        root.title('pyNote - simple text editor with a fancy name')
        text_frame = Frame(root, width=600, height=600)
        text_frame.pack(fill="both", expand=True)
        text_frame.grid_propagate(False)
        text_frame.grid_rowconfigure(0, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)

        self.text = Text(text_frame, borderwidth=1, relief="sunken")
        self.text.config(font=('lucida console', 12), undo=True, wrap='word')
        self.text.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

        scrollbar = Scrollbar(text_frame, command=self.text.yview)
        scrollbar.grid(row=0, column=1, sticky='nsew')
        self.text['yscrollcommand'] = scrollbar.set

        # creating menu
        self.menu = Menu(root)
        root.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=lambda: self.new_file())
        self.file_menu.add_command(label='Open', command=lambda: self.open_file())
        self.file_menu.add_command(label='SaveAs', command=lambda: self.save_file())
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=lambda: self.exit_tool())
        self.help_menu = Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        self.help_menu.add_command(label='About', command=lambda: self.about())

    def save_file(self):
        file = self.text.get('1.0', END)
        save_to = filedialog.asksaveasfilename()
        with open(save_to, 'w+') as save:
            save.write(file)

    def open_file(self):
        file = filedialog.askopenfilename(title='Select a file',
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        with open(file, 'rb') as opened:
            contents = opened.read()
            self.text.insert('1.0', contents)

    @staticmethod
    def exit_tool():
        if messagebox.askokcancel('Quit', 'Do you really want to quit?'):
            window.destroy()

    def new_file(self):
        if messagebox.askokcancel('New file', 'Do you want to create a new file? Unsaved changes will be lost.'):
            self.text.delete('1.0', END)

    @staticmethod
    def about():
        messagebox.showinfo('About', 'Simple text editor with a fancy name \nby Marcin Brzeski')


window = Tk()
pyNote = Notepad(window)
window.mainloop()
