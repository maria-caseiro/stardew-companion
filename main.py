import customtkinter as ctk

def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("Stardew Valley Companion")
    app.geometry("640x360")
    app.resizable(False, False)

    app.mainloop()

if __name__ == "__main__":
    main()