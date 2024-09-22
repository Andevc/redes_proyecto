from flask import Flask, render_template, request, make_response, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    
    font_type = request.cookies.get('font_type', 'Arial')
    font_color = request.cookies.get('font_color', 'black')
    visited_links = request.cookies.get('visited_links', '')

    # Convertir la lista de enlaces visitados de string a una lista
    visited_links = visited_links.split(',') if visited_links else []

    # Links disponibles
    links = ['https://google.com', 'https://github.com', 'https://ssainformatica.umsa.bo/', 'https://cvinformatica.umsa.bo/']

    return render_template('index.html', font_type=font_type, font_color=font_color, visited_links=visited_links, links=links)


@app.route('/set_preferences', methods=['POST'])
def set_preferences():
    # Obtener preferencias del usuario
    font_type = request.form.get('font_type', 'Arial')
    font_color = request.form.get('font_color', 'black')

    # Crear respuesta y guardar las cookies
    response = make_response(redirect(url_for('index')))
    expiration = datetime.now() + timedelta(days=1)
    

    response.set_cookie('font_type', font_type, expires=expiration)
    response.set_cookie('font_color', font_color, expires=expiration)
    
    return response

@app.route('/visit/<path:link>')
def visit_link(link):
    # Leer las cookies para obtener los enlaces visitados
    visited_links = request.cookies.get('visited_links', '')

    # Si el enlace aún no está en la lista, lo agregamos
    if link not in visited_links.split(','):
        visited_links = visited_links + ',' + link if visited_links else link

    # Guardar la cookie actualizada
    response = make_response(redirect(link))
    expiration = datetime.now() + timedelta(days=30)
    response.set_cookie('visited_links', visited_links, expires=expiration)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
