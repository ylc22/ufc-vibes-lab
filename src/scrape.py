"""Polite UFCStats scraper for fighter career statistics."""

from __future__ import annotations
import re
import time
from typing import Dict, List, Optional
import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE = "http://ufcstats.com"
FIGHTERS_URL = f"{BASE}/statistics/fighters"
HEADERS = {"User-Agent": "ufc-vibes-lab/1.0 (educational analytics project; polite scraper)"}

def _number(text: str, percent: bool = False) -> Optional[float]:
    text = text.strip().replace("%", "")
    if not text or text == "--":
        return None
    try:
        value = float(text)
        return value / 100.0 if percent else value
    except ValueError:
        return None

def list_fighters(session: requests.Session, limit: Optional[int] = None) -> List[Dict]:
    rows: List[Dict] = []
    for char in "abcdefghijklmnopqrstuvwxyz":
        response = session.get(
            FIGHTERS_URL,
            params={"char": char, "page": "all"},
            headers=HEADERS,
            timeout=20,
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for row in soup.select("tr.b-statistics__table-row")[2:]:
            cols = row.select("td")
            link = row.select_one("a")
            if not link or len(cols) < 10:
                continue

            first = cols[0].get_text(" ", strip=True)
            last = cols[1].get_text(" ", strip=True)
            nickname = cols[2].get_text(" ", strip=True)
            wins = _number(cols[7].get_text(strip=True))
            losses = _number(cols[8].get_text(strip=True))
            draws = _number(cols[9].get_text(strip=True))

            rows.append({
                "fighter": f"{first} {last}".strip(),
                "nickname": nickname,
                "detail_url": link["href"],
                "wins": int(wins or 0),
                "losses": int(losses or 0),
                "draws": int(draws or 0),
            })
            if limit and len(rows) >= limit:
                return rows
    return rows

def fighter_detail(session: requests.Session, url: str) -> Dict[str, Optional[float]]:
    response = session.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    text = " ".join(soup.stripped_strings)

    patterns = {
        "slpm": (r"SLpM:\s*([0-9.]+)", False),
        "str_acc": (r"Str\. Acc\.:\s*([0-9.]+)%", True),
        "sapm": (r"SApM:\s*([0-9.]+)", False),
        "str_def": (r"Str\. Def:\s*([0-9.]+)%", True),
        "td_avg": (r"TD Avg\.:\s*([0-9.]+)", False),
        "td_acc": (r"TD Acc\.:\s*([0-9.]+)%", True),
        "td_def": (r"TD Def\.:\s*([0-9.]+)%", True),
        "sub_avg": (r"Sub\. Avg\.:\s*([0-9.]+)", False),
    }

    out: Dict[str, Optional[float]] = {}
    for key, (pattern, percent) in patterns.items():
        match = re.search(pattern, text)
        out[key] = _number(match.group(1), percent=percent) if match else None
    return out

def scrape(limit: Optional[int] = 150, delay: float = 0.35) -> pd.DataFrame:
    with requests.Session() as session:
        fighters = list_fighters(session, limit=limit)
        records = []
        for i, fighter in enumerate(fighters, start=1):
            stats = fighter_detail(session, fighter["detail_url"])
            records.append({**fighter, **stats})
            if i < len(fighters):
                time.sleep(delay)
    return pd.DataFrame(records)
