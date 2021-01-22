"""
auther: lyh
c_date: 2021/1/22 9:35
u_date: 2021/1/22 9:35
reversion: 1.0
file_name: demo2
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '欢迎来到flask首页'
@app.route('/<int:pk>')
def detail(pk):
    return f'欢迎来到flask详情页{pk}'

if __name__ == '__main__':
    app.run(host='192.168.11.3',port='6789',debug=True)