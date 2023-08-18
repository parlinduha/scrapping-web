import requests
from bs4 import BeautifulSoup

# URL halaman web yang akan di-scrapping
url = 'https://www.interatlasmurni.com/'

# Mengambil konten HTML dari halaman web
response = requests.get(url)
html_content = response.text

# Menginisialisasi objek BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Mengambil elemen judul dari halaman web
title_element = soup.find('title')

# Mengambil teks dari elemen judul
title_text = title_element.text if title_element else 'Tidak ditemukan judul'

print('Judul halaman:', title_text)
