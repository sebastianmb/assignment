import tkinter as tk
from client.gui_app import Frame, barra_menu

# initiallize app
def main():
    root = tk.Tk()
    root.title("Assignment")

    root.resizable(0,0)

    barra_menu(root)

    app= Frame(root = root)

    # run app
    app.mainloop()
if __name__=='__main__':
    main()