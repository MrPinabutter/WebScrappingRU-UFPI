from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from flask_cors import CORS
from flask_caching import Cache

def create_app():
    cache = Cache(config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 5})
    app = Flask(__name__)
    cache.init_app(app)
    CORS(app)

    @app.route('/dias_da_semana', methods=['GET'])
    def get_dias_da_semana():
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

        if not pdf_url:
            return jsonify({'message': 'PDF file not found'}), 404

        # Download the PDF file
        response = requests.get(pdf_url)
        with open('document.pdf', 'wb') as f:
            f.write(response.content)

        # Search for specific content in the PDF file
        pdf_file = open('document.pdf', 'rb')
        pdf_reader = PdfReader(pdf_file)
        page = pdf_reader.pages[0]
        text = page.extract_text()

        # Segunda
        parts = []
        def visitor_body_segunda(text, cm, tm, font_dict, font_size):
            y = tm[5]
            x = tm[4]
            if y > 300 and y < 400 and x > 100 and x < 150:
                parts.append(text)

        page.extract_text(visitor_text=visitor_body_segunda)
        text_body_segunda = "".join(parts)
        text_body_segunda = text_body_segunda.replace('\n', ' ').lower()

        # Terça
        parts = []
        def visitor_body_terca(text, cm, tm, font_dict, font_size):
            y = tm[5]
            x = tm[4]
            if y > 300 and y < 400 and x > 150 and x < 200:
                parts.append(text)

        page.extract_text(visitor_text=visitor_body_terca)
        text_body_terca = "".join(parts)
        text_body_terca = text_body_terca.replace('\n', ' ').lower()

        # Quarta
        parts = []
        def visitor_body_quarta(text, cm, tm, font_dict, font_size):
            y = tm[5]
            x = tm[4]
            if y > 300 and y < 400 and x > 200 and x < 300:
                parts.append(text)

        page.extract_text(visitor_text=visitor_body_quarta)
        text_body_quarta = "".join(parts)
        text_body_quarta = text_body_quarta.replace('\n', ' ').lower()

        # Quinta
        parts = []
        def visitor_body_quinta(text, cm, tm, font_dict, font_size):
            y = tm[5]
            x = tm[4]
            if y > 300 and y < 400 and x > 300 and x < 350:
                parts.append(text)

        page.extract_text(visitor_text=visitor_body_quinta)
        text_body_quinta = "".join(parts)
        text_body_quinta = text_body_quinta.replace('\n', ' ').lower()

        # Sexta
        parts = []
        def visitor_body_sexta(text, cm, tm, font_dict, font_size):
            y = tm[5]
            x = tm[4]
            if y > 300 and y < 400 and x > 350 and x < 400:
                parts.append(text)

        page.extract_text(visitor_text=visitor_body_sexta)
        text_body_sexta = "".join(parts)
        text_body_sexta = text_body_sexta.replace('\n', ' ').lower()

        return jsonify({
            'segunda': text_body_segunda,
            'terca': text_body_terca,
            'quarta': text_body_quarta,
            'quinta': text_body_quinta,
            'sexta': text_body_sexta
        }), 200 

    
    return app