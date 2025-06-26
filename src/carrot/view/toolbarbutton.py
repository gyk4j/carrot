import tkinter as tk

# from tkinter import messagebox
# from tkinter import PhotoImage

from .tooltip import Tooltip
from controller.event import ActionEvent
from controller.event import ActionListener

class ToolBarButton:

    def __init__(self, toolbar, text: str, icon: str):
        # , action_listener: ActionListener
        self.text = text
        self.icon = icon
        self.image = tk.PhotoImage(file=self.icon)
        self.button = tk.Button(
            toolbar,
            relief=tk.FLAT,
            #compound = tk.TOP,
            #text=self.text,
            command=self._on_clicked,
            image=self.image
        )
        self.tooltip = Tooltip(self.button, self.text)
        # self.action_listener = action_listener
        self.button.pack(side=tk.LEFT, padx=0, pady=0)    
        
    def _on_clicked(self):
        action_event = ActionEvent(
            self.button, 
            ActionEvent.ACTION_PERFORMED, 
            self.text
        )

        # tk.messagebox.showinfo(
        #     title="%s title" % (action_event.action_command),
        #     message="%s clicked" % (action_event.action_command)
        # )