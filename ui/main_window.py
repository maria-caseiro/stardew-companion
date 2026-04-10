import os
import customtkinter as ctk
from PIL import Image
from data_loader import load_season, resource_path

SEASONS = ["spring", "summer", "fall", "winter"]

# Fixed card dimensions
EVENT_CARD_WIDTH = 110
EVENT_CARD_HEIGHT = 110
NPC_CARD_WIDTH = 60
NPC_CARD_HEIGHT = 110

class MainWindow(ctk.CTkFrame):
    # Main frame
    def __init__(self, parent):
        super().__init__(parent, fg_color="#C3CC9B")        
        self._image_cache = {}
        self.season_data = {}
        self._preload_seasons()
        self._build_nav()
        self._content_area()
        self._render_season("spring")

    # Preload all four seasons
    def _preload_seasons(self):
        for s in SEASONS:
            self.season_data[s] = load_season(s)

    # Season nav buttons
    def _build_nav(self):
        nav = ctk.CTkFrame(self, fg_color="transparent")
        nav.pack(anchor="center", pady=(12, 0))

        for season in SEASONS:
            btn = ctk.CTkButton(
                nav,
                text=season.capitalize(),
                width=100,
                fg_color="#5a8a3c",
                hover_color="#3e6724",
                text_color="white",
                command=lambda s=season: self._render_season(s)
            )
            btn.pack(side="left", padx=4)

    # Events and birthdays container
    def _content_area(self):
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="both", expand=True, padx=16)

    def _render_season(self, season: str):
        # Remove all widgets before loading another season 
        for widget in self.content.winfo_children():
            widget.destroy()

        data = self.season_data[season]

        # Events section label
        ctk.CTkLabel(
            self.content,
            text="Events",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="transparent",
            text_color="#18280E"
        ).pack(anchor="w", pady=(0, 2))

        # Event grid container
        events_grid = ctk.CTkFrame(self.content, fg_color="transparent")
        events_grid.pack(fill="x", pady=(0, 12))

        for i, event in enumerate(data["events"]):
            self._event_card(events_grid, event, row=0, col=i)

        # Birthdays section label
        ctk.CTkLabel(
            self.content,
            text="Birthdays",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="transparent",
            text_color="#18280E"
        ).pack(anchor="w", pady=(0, 2))

        # Birthday grid container
        npc_grid = ctk.CTkFrame(self.content, fg_color="transparent")
        npc_grid.pack(fill="x")

        for i, npc in enumerate(data["birthdays"]):
            self._npc_card(npc_grid, npc, row=0, col=i)

    def _load_image(self, folder: str, filename: str, size: tuple):
        key = (filename, size)
        if key in self._image_cache:
            return self._image_cache[key]
        try:
            path = resource_path(os.path.join("assets", folder, filename))
            img = ctk.CTkImage(Image.open(path), size=size)
            self._image_cache[key] = img
            return img
        except Exception:
            return None

    def _event_card(self, parent, event: dict, row: int, col: int):
        card = ctk.CTkFrame(
            parent,
            corner_radius=8,
            fg_color="#f2edcb",
            width=EVENT_CARD_WIDTH,
            height=EVENT_CARD_HEIGHT
        )
        card.grid(row=row, column=col, padx=4, pady=2, sticky="n")
        card.grid_propagate(False)

        # Event icon
        img = self._load_image("icons", "Event_Icon.png", (28, 28))
        ctk.CTkLabel(
            card,
            image=img,
            text="",
            fg_color="transparent"
        ).place(relx=0.5, rely=0.25, anchor="center")

        # Event name
        ctk.CTkLabel(
            card,
            text=event["name"],
            font=ctk.CTkFont(size=10, weight='bold'),
            fg_color="transparent",
            text_color="#18280E",
            wraplength=EVENT_CARD_WIDTH - 15
            ).place(relx=0.5, rely=0.55, anchor="center")

        # Event day
        if event["start_day"] == event["end_day"]:
            day_text = f"Day {event['start_day']}"
        else:
            day_text = f"Days {event['start_day']}–{event['end_day']}"

        ctk.CTkLabel(
            card,
            text=day_text,
            font=ctk.CTkFont(size=10),
            fg_color="transparent",
            text_color="gray"
        ).place(relx=0.5, rely=0.78, anchor="center")

    def _npc_card(self, parent, npc: dict, row: int, col: int):
        card = ctk.CTkFrame(
            parent,
            corner_radius=8,
            fg_color="#f2edcb",
            width=NPC_CARD_WIDTH,
            height=NPC_CARD_HEIGHT
        )
        card.grid(row=row, column=col, padx=4, pady=4, sticky="n")
        card.grid_propagate(False)

        # NPC icon
        img = self._load_image("npcs", npc["icon"], (35, 35))
        ctk.CTkLabel(
            card, 
            image=img, 
            text="", 
            fg_color="transparent"
        ).place(relx=0.5, rely=0.28, anchor="center")

        # NPC name
        ctk.CTkLabel(
            card,
            text=npc["npc"],
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="transparent",
            text_color="#18280E",
            wraplength=NPC_CARD_WIDTH - 5
        ).place(relx=0.5, rely=0.58, anchor="center")

        # Birthday day
        ctk.CTkLabel(
            card,
            text=f"Day {npc['day']}",
            font=ctk.CTkFont(size=9),
            fg_color="transparent",
            text_color="gray"
        ).place(relx=0.5, rely=0.78, anchor="center")