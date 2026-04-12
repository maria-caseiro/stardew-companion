import customtkinter as ctk

class EventDetail(ctk.CTkFrame):
    def __init__(self, parent, event: dict):
        # Overlay frame
        super().__init__(parent, fg_color="#C3CC9B")
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Button-1>", lambda e: self.destroy())

        # Central content
        panel = ctk.CTkFrame(
            self,
            corner_radius=12,
            fg_color="#f2edcb",
            border_width=1,
            border_color="#5a8a3c",
            width=400,
            height=260,
        )
        panel.place(relx=0.5, rely=0.5, anchor="center")
        panel.pack_propagate(False)

        # Event name
        ctk.CTkLabel(
            panel,
            text=event["name"],
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="transparent",
            text_color="#18280E",
        ).pack(pady=(25, 2))

        # Event day
        if event["start_day"] == event["end_day"]:
            day_text = f"Day {event['start_day']}"
        else:
            day_text = f"Days {event['start_day']}–{event['end_day']}"

        ctk.CTkLabel(
            panel,
            text=day_text,
            font=ctk.CTkFont(size=12),
            fg_color="transparent",
            text_color="gray",
        ).pack()

        # Divider
        ctk.CTkFrame(panel, height=1, fg_color="#c8c09a").pack(
            fill="x", padx=25, pady=15
        )

        # Event description
        ctk.CTkLabel(
            panel,
            text=event["description"],
            font=ctk.CTkFont(size=13),
            fg_color="transparent",
            text_color="#18280E",
            wraplength=320,
            justify="center",
        ).pack(padx=20)

        # Event note
        ctk.CTkLabel(
            panel,
            text=event["notes"],
            font=ctk.CTkFont(size=11),
            fg_color="transparent",
            text_color="gray",
            wraplength=360,
            justify="center",
        ).pack(padx=20, pady=(6, 0))

        # Close button
        ctk.CTkButton(
            panel,
            text="Close",
            width=80,
            fg_color="#5a8a3c",
            hover_color="#3e6724",
            text_color="white",
            command=self.destroy,
        ).place(relx=0.5, rely=0.86, anchor="center")
