import customtkinter as ctk
from ui.main_window import MainWindow

def main():
    app = ctk.CTk()
    app.title("Stardew Valley Companion")
    app.geometry("760x420")
    app.resizable(False, False)

    window = MainWindow(app)
    window.pack(fill="both", expand=True)

    app.mainloop()

if __name__ == "__main__":
    main()