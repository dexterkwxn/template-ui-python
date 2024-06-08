from tkinter import *
from tkinter import ttk

TITLE="Template UI Maker"
MAINFRAME_PADDING=[3,3,12,20]
BORDER_WIDTH=5
MAINFRAME_RELIEF='raised'

class MainUI:
    def __init__(self, root, title=TITLE, mainframe_padding=MAINFRAME_PADDING, border_width=BORDER_WIDTH, mainframe_relief=MAINFRAME_RELIEF):
        self.root = root
        root.title(TITLE)

        self.mainframe = ttk.Frame(root, padding=' '.join([str(x) for x in mainframe_padding[:4]]), borderwidth=border_width, relief=mainframe_relief)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        title, title_entry = self.createTitleField()

        meters = StringVar()
        ttk.Label(self.mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text="Calculate", command=lambda x: print("CALCULATE")).grid(column=3, row=3, sticky=W)

        ttk.Label(self.mainframe, text="feet").grid(column=4, row=1, sticky=W)
        ttk.Label(self.mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(self.mainframe, text="meters").grid(column=3, row=2, sticky=W)


        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        title_entry.focus()
        root.bind("<Return>", lambda x: print("RETURN"))
    
    def createTitleField(self):
        ttk.Label(self.mainframe, text="App Title").grid(column=1, row=1, sticky=(W, E))
        title = StringVar()
        title_entry = ttk.Entry(self.mainframe, width=20, textvariable=title)
        title_entry.grid(column=2, row=1, sticky=(W, E))
        return title, title_entry
    
    def createMainframeReliefSelector(self):
        ttk.Label(self.mainframe, text="Mainframe Relief").grid(column=1, row=1, sticky=(W, E))
        values = ['flat', 'raised', 'sunken', 'solid', 'ridge', 'groove']
        title = StringVar()
        title_entry = ttk.Combobox(self.mainframe, width=20, textvariable=title)
        title_entry.grid(column=2, row=1, sticky=(W, E))
        return title, title_entry
        
        
