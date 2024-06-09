from tkinter import *
from tkinter import ttk
import os
import random

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

        self.createTitleField()
        self.createMainframeReliefSelector()

        # meters = StringVar()
        # ttk.Label(self.mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text="Create Application", command=self.createApplication).grid(column=3, row=3, sticky=W)

        # ttk.Label(self.mainframe, text="feet").grid(column=4, row=1, sticky=W)
        # ttk.Label(self.mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        # ttk.Label(self.mainframe, text="meters").grid(column=3, row=2, sticky=W)


        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.title_entry.focus()
        root.bind("<Return>", self.createApplication)
    
    def createTitleField(self):
        ttk.Label(self.mainframe, text="App Title").grid(column=1, row=1, sticky=(W, E))
        self.title = StringVar()
        self.title_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.title)
        self.title_entry.grid(column=2, row=1, sticky=(W, E))
        return 

    def createMainframeReliefSelector(self):
        ttk.Label(self.mainframe, text="Mainframe Relief").grid(column=1, row=2, sticky=(W, E))
        self.relief_values = ['flat', 'raised', 'sunken', 'solid', 'ridge', 'groove']
        self.mainframe_relief = StringVar()
        self.mainframe_relief_entry = ttk.Combobox(self.mainframe, values=self.relief_values, width=20, textvariable=self.mainframe_relief)
        self.mainframe_relief_entry.grid(column=2, row=2, sticky=(W, E))
        return
        
    def createApplication(self, *args):
        if not self.validateFields():
            print("Error: Some fields are invalid.")
            return False

        new_folder = 'app' + str(random.randrange(0,100))
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        
        with open('templates/app.config', 'r') as file:
            data = file.read()
            data = data.replace("<<APP_TITLE>>", "\"" + self.title.get() + "\"", 1)
            data = data.replace("<<MAINFRAME_RELIEF>>", "\"" + self.mainframe_relief.get() + "\"", 1)

            with open(os.path.join(new_folder, 'app.py'), 'w') as new_file:
                new_file.write(data)
        
        with open('main.py', 'r') as file:
            data = file.read()
            with open(os.path.join(new_folder, 'main.py'), 'w') as new_file:
                new_file.write(data)
        
            

    def validateFields(self):
        return True
        
