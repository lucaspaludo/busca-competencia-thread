import tkinter as tk
from time import sleep

def exibirPopup(titulo, mensagem):
    popup = tk.Tk()

    popup.title(titulo)

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    popup.geometry(f'300x100+{screen_width-310}+{screen_height-180}')

    label = tk.Label(popup, text=mensagem)

    label.pack(pady=10)
    popup.after(5000, popup.destroy)
    popup.mainloop()