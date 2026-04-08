import json
import os
import sys

def resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, relative_path)

def load_season(season: str) -> dict:
    path = resource_path(os.path.join("data", f"{season}.json"))
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Ficheiro não encontrado: {path}")