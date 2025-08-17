import os, httpx
from bs4 import BeautifulSoup

UA = os.getenv("SCRAPER_USER_AGENT", "autoinfra-bot/1.0")

async def fetch_html(url: str) -> str:
    headers = {"User-Agent": UA}
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url, headers=headers)
        r.raise_for_status()
        return r.text

def parse_simple_tenders(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    items = []
    for h in soup.find_all(["h2","h3"]):
        title = h.get_text(strip=True)
        if title and any(k in title.lower() for k in ["tender", "infrastructure", "solar", "water", "hospital"]):
            items.append({"title": title})
    return items
