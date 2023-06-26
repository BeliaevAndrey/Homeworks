from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {
        'title': 'Welcome'
    }
    return render_template('index.html', **context)


@app.route('/boots/')
def boots_page():
    context = {
        'title': 'Boots',
        'item_cards': [
            {'image_path': '../static/img/boots.jpeg',
             'card_title': 'Doom boots',
             'description': 'Lorem ipsum dolor sit amet. 1'},
            {'image_path': '../static/img/boots.jpeg',
             'card_title': 'Doom boots',
             'description': 'Lorem ipsum dolor sit amet. 2'},
            {'image_path': '../static/img/boots.jpeg',
             'card_title': 'Doom boots',
             'description': 'Lorem ipsum dolor sit amet. 3'},
            {'image_path': '../static/img/boots.jpeg',
             'card_title': 'Doom boots',
             'description': 'Lorem ipsum dolor sit amet. 4'},
            {'image_path': '../static/img/boots.jpeg',
             'card_title': 'Doom boots',
             'description': 'Lorem ipsum dolor sit amet. 5'},
        ]
    }
    return render_template('boots.html', **context)


@app.route('/jackets/')
def jackets_page():
    context = {
        'title': 'Jackets',
        'item_cards': [
            {'image_path': '../static/img/jacket.jpg',
             'card_title': 'Doom jacket',
             'description': 'Lorem ipsum dolor sit amet. 1'},
            {'image_path': '../static/img/jacket.jpg',
             'card_title': 'Doom jacket',
             'description': 'Lorem ipsum dolor sit amet. 2'},
            {'image_path': '../static/img/jacket.jpg',
             'card_title': 'Doom jacket',
             'description': 'Lorem ipsum dolor sit amet. 3'},
            {'image_path': '../static/img/jacket.jpg',
             'card_title': 'Doom jacket',
             'description': 'Lorem ipsum dolor sit amet. 4'},
            {'image_path': '../static/img/jacket.jpg',
             'card_title': 'Doom jacket',
             'description': 'Lorem ipsum dolor sit amet. 5'},
            {'image_path': '../static/img/jacket.jpg',
             'card_title': 'Doom boots',
             'description': 'Lorem ipsum dolor sit amet. 6'},
        ]
    }
    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
