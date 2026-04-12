import os
import customtkinter as ctk
from PIL import Image
from data_loader import resource_path

ICON_FOLDERS = ["farming", "fishing", "foraging", "items", "mining", "recipes"]
FONT = "Segoe UI"

class NPCDetail(ctk.CTkFrame):
    def __init__(self, parent, npc: dict):
        # Overlay frame
        super().__init__(parent, fg_color="#C3CC9B")
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Button-1>", lambda e: self.destroy())

        # Image cache
        self._image_cache = {}

        # Central content
        panel = ctk.CTkFrame(
            self,
            corner_radius=12,
            fg_color="#f2edcb",
            border_width=2,
            border_color="#5a8a3c",
            width=460,
            height=320,
        )
        panel.place(relx=0.5, rely=0.5, anchor="center")
        panel.pack_propagate(False)

        # Left column
        left = ctk.CTkFrame(panel, fg_color="transparent", width=340)
        left.place(x=20, y=20)

        # NPC name
        ctk.CTkLabel(
            left,
            text=npc["npc"],
            font=ctk.CTkFont(family=FONT, size=15, weight="bold"),
            fg_color="transparent",
            text_color="#18280E",
            anchor="w"
        ).pack(anchor="w")

        # Birthday day
        ctk.CTkLabel(
            left,
            text=f"Day {npc['day']}",
            font=ctk.CTkFont(family=FONT, size=11),
            fg_color="transparent",
            text_color="gray",
            anchor="w"
        ).pack(anchor="w", pady=(2, 0))

        # Description
        ctk.CTkLabel(
            left,
            text=npc["description"],
            font=ctk.CTkFont(family=FONT, size=12),
            fg_color="transparent",
            text_color="#18280E",
            wraplength=260,
            justify="left",
            anchor="w"
        ).pack(anchor="w", pady=(8, 0))

        # Divider
        ctk.CTkFrame(left, height=2, width=260, fg_color="#c8c09a").pack(pady=(15,5), anchor="w")

        # Loves label
        ctk.CTkLabel(
            left,
            text="Loves",
            font=ctk.CTkFont(family=FONT, size=11, weight="bold"),
            fg_color="transparent",
            text_color="#18280E",
            anchor="w"
        ).pack(anchor="w", pady=(0, 4))

        # Loves icons
        loves_row = ctk.CTkFrame(left, fg_color="transparent")
        loves_row.pack(anchor="w")

        for item in npc["loves"]:
            self._item_icon(loves_row, item)

        # Likes label
        ctk.CTkLabel(
            left,
            text="Likes",
            font=ctk.CTkFont(family=FONT, size=11, weight="bold"),
            fg_color="transparent",
            text_color="#18280E",
            anchor="w"
        ).pack(anchor="w", pady=(10, 4))

        # Likes icons
        likes_row = ctk.CTkFrame(left, fg_color="transparent")
        likes_row.pack(anchor="w")

        for item in npc["likes"]:
            self._item_icon(likes_row, item)

        # Portrait
        portrait_img = self._load_portrait(npc["portrait"])
        if portrait_img:
            ctk.CTkLabel(
                panel,
                image=portrait_img,
                text="",
                fg_color="transparent"
            ).place(x=305, y=25, anchor="nw")

        # Close button
        ctk.CTkButton(
            panel,
            text="Close",
            width=80,
            fg_color="#5a8a3c",
            hover_color="#3e6724",
            text_color="white",
            cursor="hand2",
            command=self.destroy,
        ).place(relx=0.5, rely=0.88, anchor="center")

    def _load_portrait(self, filename: str):
        # Load NPC portrait
        try:
            path = resource_path(os.path.join("assets", "npcs", filename))
            return ctk.CTkImage(Image.open(path), size=(128, 128))
        except Exception:
            return None

    def _find_icon(self, filename: str, size: tuple):
        # Search subfolders for icon
        key = (filename, size)
        if key in self._image_cache:
            return self._image_cache[key]
        for folder in ICON_FOLDERS:
            path = resource_path(os.path.join("assets", "icons", folder, filename))
            if os.path.exists(path):
                img = ctk.CTkImage(Image.open(path), size=size)
                self._image_cache[key] = img
                return img
        return None

    def _item_icon(self, parent, item: dict):
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(side="left", padx=2)

        img = self._find_icon(item["icon"], (30, 30))
        label = ctk.CTkLabel(
            container,
            image=img,
            text="",
            fg_color="transparent",
        )
        label.pack()

        # Store tooltip reference
        self._tooltip = None

        def on_enter(e):
            # Destroy previous tooltip
            if self._tooltip:
                self._tooltip.place_forget()
                self._tooltip.destroy()

            # Tooltip label
            self._tooltip = ctk.CTkLabel(
                self,
                text=item["name"],
                font=ctk.CTkFont(family=FONT, size=10),
                fg_color="#18280E",
                text_color="white",
                corner_radius=4,
            )
            x = label.winfo_rootx() - self.winfo_rootx() + 12
            y = label.winfo_rooty() - self.winfo_rooty() - 20
            self._tooltip.place(x=x, y=y)

        def on_leave(e):
            if self._tooltip:
                self._tooltip.place_forget()

        label.bind("<Enter>", on_enter)
        label.bind("<Leave>", on_leave)