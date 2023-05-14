import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# Send a request to the website
url = 'https://ufpi.br/restaurante-universitario'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the URL of the PDF file
pdf_url = None
for link in soup.find_all('a'):
    if link.get('href').endswith('.pdf') and "Teresina" in link.string:
        pdf_url = f'https://ufpi.br{link["href"]}'
        break

if not pdf_url: exit()

# Download the PDF file
response = requests.get(pdf_url)
with open('document.pdf', 'wb') as f:
    f.write(response.content)

# Search for specific content in the PDF file

pdf_file = open('document.pdf', 'rb')
pdf_reader = PdfReader(pdf_file)
page = pdf_reader.pages[0]

text = page.extract_text()

parts = []
# Segunda
def visitor_body_segunda(text, cm, tm, font_dict, font_size):
    y = tm[5]
    x = tm[4]
    if y > 300 and y < 400 and x > 100 and x < 150:
        parts.append(text)

page.extract_text(visitor_text=visitor_body_segunda)
text_body = "".join(parts)
text_body = text_body.replace('\n', ' ').lower()
print("Segunda:", text_body)

parts = []

# Terça
def visitor_body_terca(text, cm, tm, font_dict, font_size):
    y = tm[5]
    x = tm[4]
    if y > 300 and y < 400 and x > 150 and x < 200:
        parts.append(text)

page.extract_text(visitor_text=visitor_body_terca)
text_body = "".join(parts)
text_body = text_body.replace('\n', ' ').lower()

print("Terça:",text_body)

parts = []

# Quarta
def visitor_body_quarta(text, cm, tm, font_dict, font_size):
    y = tm[5]
    x = tm[4]
    if y > 300 and y < 400 and x > 200 and x < 250:
        parts.append(text)

page.extract_text(visitor_text=visitor_body_quarta)
text_body = "".join(parts)
text_body = text_body.replace('\n', ' ').lower()

print("Quarta:", text_body)

parts = []

# Quinta
def visitor_body_quinta(text, cm, tm, font_dict, font_size):
    y = tm[5]
    x = tm[4]
    if y > 300 and y < 400 and x > 300 and x < 350:
        parts.append(text)

page.extract_text(visitor_text=visitor_body_quinta)
text_body = "".join(parts)
text_body = text_body.replace('\n', ' ').lower()

print("Quinta:", text_body)

parts = []

# Sexta
def visitor_body_sexta(text, cm, tm, font_dict, font_size):
    y = tm[5]
    x = tm[4]
    if y > 300 and y < 400 and x > 350 and x < 400:
        parts.append(text)

page.extract_text(visitor_text=visitor_body_sexta)
text_body = "".join(parts)
text_body = text_body.replace('\n', ' ').lower()

print("Sexta:", text_body)
