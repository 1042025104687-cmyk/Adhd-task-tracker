import tkinter as tk

class ADHDTaskTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ADHD Task Tracker")
        self.root.geometry("400x300")

        self.bg_color = "#2b2b2b"
        self.fg_color = "#e6e6e6"
        self.entry_bg = "#3a3a3a"
        self.button_bg = "#393939"
        self.button_active = "#505050"
        self.listbox_bg = "#232323"
        self.listbox_select_bg = "#4a90e2"
        self.listbox_select_fg = "#ffffff"

        self.root.configure(bg=self.bg_color)

        self.root.option_add("*background", self.bg_color)
        self.root.option_add("*foreground", self.fg_color)

        self.root.option_add("*Button.background", self.button_bg)
        self.root.option_add("*Button.foreground", self.fg_color)
        self.root.option_add("*Button.activeBackground", self.button_active)

        self.root.option_add("*Entry.background", self.entry_bg)
        self.root.option_add("*Entry.foreground", self.fg_color)
        self.root.option_add("*Entry.fieldBackground", self.entry_bg)

        self.root.option_add("*Listbox.background", self.listbox_bg)
        self.root.option_add("*Listbox.foreground", self.fg_color)
        self.root.option_add("*Listbox.selectBackground", self.listbox_select_bg)
        self.root.option_add("*Listbox.selectForeground", self.listbox_select_fg)

        self.tasks = []
        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.remove_task_button = tk.Button(self.root, text="Remove Selected Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_indices = self.task_listbox.curselection()
        for index in reversed(selected_indices):
            self.task_listbox.delete(index)
            del self.tasks[index]
            self.task_entry.delete(0, tk.END)
    
if __name__ == "__main__":
    app = ADHDTaskTracker()
    app.root.mainloop()