import os
import json
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote

RARITY_MAP = {
    "#4B69FF": "1",
    "#8847FF": "2",
    "#D32CE6": "3",
    "#EB4B4B": "4",
    "#FFD700": "5"
}

def extract_price(price_div):
    price_spans = price_div.find_all("span")
    
    if len(price_spans) == 1:  # Constant price
        return {"type": "constant", "price": price_spans[0].text.strip()}
    elif len(price_spans) == 3:  # Dynamic price (min - max)
        return {
            "type": "dynamic",
            "min_price": price_spans[0].text.strip(),
            "max_price": price_spans[2].text.strip()
        }
    return None

def download_skin_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_tags = soup.find_all('div', class_="border-b-5 relative p-1 rounded-[5px]")

    skin_data = {}

    for div in div_tags:
        img = div.find("img")
        if not img:
            continue

        img_url = img.get('src')
        alt_text = img.get('alt')
        border_color = div.get("style")
        price_div = div.find("div", class_="absolute flex justify-between flex-wrap w-full bottom-0 right-0 text-green-400 pb-0.5 text-xs bg-black/20 px-1")

        if not img_url or not alt_text or not border_color or not price_div:
            continue

        match = re.search(r"border-color:\s*(#(?:[0-9a-fA-F]{3}){1,2})", border_color)
        if not match:
            continue

        rarity = RARITY_MAP.get(match.group(1).upper(), "Unknown")
        img_url = img_url.split("?url=")[1]
        img_url = unquote(img_url)
        img_url = img_url.split('&w=')[0]
        
        parts = alt_text.split('| ')
        if len(parts) != 2:
            continue
        
        weapon_name = parts[0].strip()
        skin_name = parts[1].strip()
        
        price_info = extract_price(price_div)
        if not price_info:
            continue
        
        if weapon_name not in skin_data:
            skin_data[weapon_name] = {}
        if rarity not in skin_data[weapon_name]:
            skin_data[weapon_name][rarity] = {}
        
        skin_data[weapon_name][rarity][skin_name] = price_info
    
    return skin_data

def get_all_cases():
    URL = "https://case.oki.gg/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img", alt=re.compile(r"Case"))

    case_links = []
    for img in img_tags:
        case_name = img["alt"].split(" - ")[0]
        case_url = f"https://case.oki.gg/crate/{case_name.replace(' ', '%20')}"
        case_links.append(case_url)
    
    return case_links

def main():
    save_path = "skins_data.json"
    all_skin_data = {}
    
    case_urls = get_all_cases()
    for case_url in case_urls:
        print(f"Processing case: {case_url}")
        case_data = download_skin_data(case_url)
        for weapon, rarity_data in case_data.items():
            if weapon not in all_skin_data:
                all_skin_data[weapon] = {}
            for rarity, skins in rarity_data.items():
                if rarity not in all_skin_data[weapon]:
                    all_skin_data[weapon][rarity] = {}
                all_skin_data[weapon][rarity].update(skins)
    
    with open(save_path, "w", encoding="utf-8") as json_file:
        json.dump(all_skin_data, json_file, indent=4, ensure_ascii=False)
    
    print(f"Saved skin data to {save_path}")

if __name__ == "__main__":
    main()
