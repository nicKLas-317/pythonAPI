from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/about')
def about():
    return 'The about page'

books= [
    {
        'id': 1,
        'titre':'un-titre',
    },
    {
        'id': 2,
        'titre':'autre',
    },
    {
        'id': 3,
        'titre': 'troisieme',
    }
]

@app.route('/api/books', methods=['GET'])
def renderBooks():
    return str(books), 200

@app.route('/api/book/<int:id>', methods=['GET'])
def renderBook(id):
    found_values = []
    for book in books:
        if (book["id"] == id):
            found_values.append(book)
    return render_template('index.html', book=found_values), 200


@app.route('/api/book/<title>', methods=['GET'])
def renderBookTitle(title):
    found_values = []
    for dict in books:
        if (dict["titre"] == title):
            found_values.append(dict)
    return render_template('index.html', book=found_values), 200


if __name__ == '__api__':
    app.run(debug=True)