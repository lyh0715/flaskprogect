"""
auther: lyh
c_date: 2021/1/22 11:34
u_date: 2021/1/22 11:34
reversion: 1.0
file_name: demo4
"""
from flask import Flask, render_template

app = Flask(__name__)
book = {
    'name': '斗破苍穹',
    'auth': '天蚕土豆',
    'articles': [
        {
            'title': '陨落的天才',
            'content': '**',
            'id': 102
        },
        {
            'title': '第二章',
            'content': '**',
            'id': 103

        },
        {
            'title': '第三章',
            'content': '**',
            'id': 104
        },
    ]
}


@app.route('/')
def index():
    article = book['articles']
    return render_template('index.html', **locals())


@app.route('/<int:pk>')
def detail(pk):
    article = None
    for a in book['articles']:
        if a['id'] == pk:
            article = a
    return render_template('detail.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
