import tkinter as tk
from controllers.controller import CowController

def main():
    root = tk.Tk()
    root.geometry("300x150")
    root.title("Cow Registration System")
    controller = CowController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
