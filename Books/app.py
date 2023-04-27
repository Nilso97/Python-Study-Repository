from flask import Flask, request, jsonify
import os, json

app = Flask(__name__)

dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(dir, 'data', 'books.json')

with open(file_path, 'r') as arquivo_json:
    books = json.load(arquivo_json)

# Adicionar um novo livro
@app.route('/livros', methods=['POST'])
def add_new_book():
    book = request.get_json()
    books.append(book)
    return jsonify(books)

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def list_all_books():
    return jsonify(books)
    
# Consultar livro através do (id)
@app.route('/livros/<int:id>', methods=['GET'])
def find_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# Editar livro através do (id)
@app.route('/livros/<int:id>', methods=['PUT'])
def update_book_by_id(id):
    edit_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(edit_book)
            return jsonify(books[index])

# Deletar livro através do (id)
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    for index, book in enumerate(books):
        if book.get('id') == id: 
            del books[index]
    return jsonify(books)

app.run(port=5000, debug=True, host='localhost')