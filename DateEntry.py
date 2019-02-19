import tkinter.ttk as ttk
from datetime import datetime

class DateEntry(ttk.Entry):
    def __init__(self, master, text="YYYY-MM-DD", **kwargs):
        ttk.Entry.__init__(self, master, **kwargs)
        self.master = master
        self.text = text
        self.bind('<FocusIn>', self._focus_in)
        self.bind('<FocusOut>', self._focus_out)
        self.insert(0, text)
        self.configure(foreground='grey')

    def _focus_in(self, event=None):
        if self.text == self.get():
            self.delete(0, 'end')
        self.configure(foreground='black')
        self.configure(background='white')
    
    def _focus_out(self, event=None):
        if self.get() == '':
            self.configure(foreground='grey')
            self.insert(0, self.text)
            return

        date_valid = True
        try:
            datetime.strptime(self.get(), '%Y-%m-%d')
        except ValueError:
            date_valid = False

        if date_valid:
            self.configure(foreground='black')
            self.configure(background='white')
        else:
            self.configure(foreground='red')
            self.configure(background='red')

    @property
    def is_valid(self):
        try:
            datetime.strptime(self.get(), '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_date(self):
        if self.is_valid:
            return datetime.strptime(self.get(), '%Y-%m-%d')

    @property
    def year(self):
        if self.is_valid:
            return self.get()[0:4]

    @property
    def month(self):
        if self.is_valid:
            return self.get()[5:7]

    @property
    def day(self):
        if self.is_valid:
            return self.get()[8:]
