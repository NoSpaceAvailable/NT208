import os
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

def download_skin_images(url, save_dir):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    div_tags = soup.find_all('div', class_="border-b-5 relative p-1 rounded-[5px]")

    for div in div_tags:
        img = div.find("img")
        if not img:
            continue

        img_url = img.get('src')
        alt_text = img.get('alt')
        border_color = div.get("style")
        
        if not img_url or not alt_text or not border_color:
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
        
        weapon_name = parts[0].strip().replace(' ', '_')
        skin_name = parts[1].strip().replace(' ', '_')

        weapon_folder = os.path.join(save_dir, weapon_name, rarity)
        os.makedirs(weapon_folder, exist_ok=True)

        img_filename = f"{skin_name}.png"
        img_path = os.path.join(weapon_folder, img_filename)
        
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
        print(f"Downloaded image: {img_path}")

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

save_directory = "./gun"

case_urls = get_all_cases()
for case_url in case_urls:
    print(f"Get gun from case: {case_url}")
    download_skin_images(case_url, save_directory)

