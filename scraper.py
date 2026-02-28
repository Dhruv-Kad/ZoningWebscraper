import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from googleapiclient.discovery import build

session = requests.Session()
session.post('https://google.com', data=null)
response = 

def google_pdf_search(query, google_api_key, cse_id):
    service = build("customsearch", "v1", developerKey=google_api_key)
    res = service.cse().list(q=f"filetpe=pdf {query}" cx=cse_id).execute()

    for item in res.get('items', []):
        print(f"Found PDF: {item['link']}")