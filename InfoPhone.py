import requests
from bs4 import BeautifulSoup
import urllib.parse
import pyfiglet

def google_dork(phone_number):
    dorks = [
        f'"{phone_number}"',
        f'filetype:pdf"{phone_number}"',
        f'filetype:doc"{phone_number}"',
        f'filetype:xls"{phone_number}"',
        f'site:facebook.com"{phone_number}"',
        f'site:linkedin.com"{phone_number}"',
        f'site:instgram.com"{phone_number}"',
        f'intext:"{phone_number}"',
        f'site:google.com"{phone_number}"',
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    results = []    
    for dork in dorks:
        query = urllib.parse.quote(dork)
        url = f'https://www.google.com/search?q={query}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for g in soup.find_all('div', class_='g'):
            result = {}
            result['title'] = g.find('h3').text if g.find('h3') else None
            result['link'] = g.find('a')['href'] if g.find('a') else None
            result['snippet'] = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else None
            results.append(result)
    
    return results
B = '\033[1;36m'
logo = pyfiglet.figlet_format(' JACKS ')
print(B+logo)


phone_number =input('\033[1;32m> Enter phone number: ')
print(B+'--------------------')
info = google_dork(phone_number)
for i, result in enumerate(info):
	   print(f"Result {i + 1}:")
	   print(f"Title: {result['title']}")
	   print(f"Link: {result['link']}")
	   print(f"Snippet: {result['snippet']}")
	   print("-" * 80)
