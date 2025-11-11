import requests
import re
import os
import logging
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
URLS_TO_SCRAPE = [
    # --- Main Topics ---
    "https://rn.wikipedia.org/wiki/Uburundi",
    "https://rn.wikipedia.org/wiki/Ikirundi",
    "https://rn.wikipedia.org/wiki/Amateka_y%27Uburundi", # History of Burundi
    "https://rn.wikipedia.org/wiki/Imana",               # God
    "https://rn.wikipedia.org/wiki/Bibiliya",            # Bible
    "https://rn.wikipedia.org/wiki/Ivyakozwe_n%27Intumwa", # Book of Acts
    "https://rn.wikipedia.org/wiki/Yezu_Kristu",         # Jesus Christ
    "https://rn.wikipedia.org/wiki/Afrika",              # Africa
    
    # --- Provinces & Cities ---
    "https://rn.wikipedia.org/wiki/Bujumbura",
    "https://rn.wikipedia.org/wiki/Gitega",
    "https://rn.wikipedia.org/wiki/Intara_z%27Uburundi", # Provinces of Burundi
    "https://rn.wikipedia.org/wiki/Ngozi",
    "https://rn.wikipedia.org/wiki/Rumonge",
    "https://rn.wikipedia.org/wiki/Bururi",
    "https://rn.wikipedia.org/wiki/IProvense_ya_Mwaro",  # Mwaro Province
    "https://rn.wikipedia.org/wiki/Kirundo",
    "https://rn.wikipedia.org/wiki/Muyinga",
    "https://rn.wikipedia.org/wiki/Ruyigi",
    "https://rn.wikipedia.org/wiki/Cankuzo",
    "https://rn.wikipedia.org/wiki/Karuzi",
    "https://rn.wikipedia.org/wiki/Muramvya",
    "https://rn.wikipedia.org/wiki/Bubanza",
    "https://rn.wikipedia.org/wiki/Cibitoke",
    "https://rn.wikipedia.org/wiki/Kayanza",
    "https://rn.wikipedia.org/wiki/Makamba",
    "https://rn.wikipedia.org/wiki/Rutana",
    
    # --- Geography & Culture ---
    "https://rn.wikipedia.org/wiki/Ikiyaga_Tanganyika", # Lake Tanganyika
    "https://rn.wikipedia.org/wiki/Abakuru_b%27igihugu_c%27_Uburundi", # Heads of State
    "https://rn.wikipedia.org/wiki/Ubutunzi",          # Economy
    "https://rn.wikipedia.org/wiki/Indero",            # Education
    "https://rn.wikipedia.org/wiki/Uburimyi",          # Agriculture
    "https://rn.wikipedia.org/wiki/Amateke"            # Taro (food)
]

OUTPUT_FILENAME = "kirundi_prompts_scraped.txt"
MIN_WORDS = 4
MAX_WORDS = 25
# --------------------------

def normalize_and_clean(text):
    text = text.replace('ā', 'a').replace('á', 'a').replace('â', 'a')
    text = text.replace('ē', 'e').replace('é', 'e').replace('ê', 'e')
    text = text.replace('ī', 'i').replace('í', 'i').replace('î', 'i').replace('ĭ', 'i')
    text = text.replace('ō', 'o').replace('ó', 'o').replace('ô', 'o')
    text = text.replace('ū', 'u').replace('ú', 'u').replace('û', 'u').replace('ŭ', 'u')
    text = text.replace('Ntā', 'Nta').replace('nā', 'na')
    text = re.sub(r'^\s*Akarorero\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*Uturorero\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\([^\)]*ni ingereka[^\)]*\)', '', text, flags=re.IGNORECASE)
    text = text.replace('^', '').replace('*', '').replace(':', '')
    text = re.sub(r'\[.*?\]', '', text)
    text = text.strip().strip('()"')
    return text.strip()

def scrape_and_clean():
    all_clean_sentences = set()
    for url in URLS_TO_SCRAPE:
        try:
            logger.info(f"Scraping: {url}")
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status() 
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.find('div', {'id': 'mw-content-text'})
            if not content: continue
            full_text = " ".join(p.get_text() for p in content.find_all('p'))
            sentences = re.split(r'[.?!]', full_text)
            for sentence in sentences:
                s = normalize_and_clean(sentence)
                words = s.split()
                if len(words) >= MIN_WORDS and len(words) <= MAX_WORDS:
                    all_clean_sentences.add(s)
        except Exception as e:
            logger.error(f"Failed to process {url}: {e}")
    
    if not all_clean_sentences:
        logger.error("Error: No sentences were extracted.")
        return

    logger.info(f"Found {len(all_clean_sentences)} unique, clean sentences.")
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        for sentence in sorted(list(all_clean_sentences)):
            f.write(sentence + "\n")
    logger.info(f"✅ Successfully saved all sentences to '{OUTPUT_FILENAME}'")

if __name__ == "__main__":
    scrape_and_clean()