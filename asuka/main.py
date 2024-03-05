from flask import Flask,render_template,request,redirect,jsonify
from flask_cors import CORS
from methods.get_title_and_favicon import get_title_and_favicon
app = Flask(__name__)
CORS(app)  # 启用 CORS 支持

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/url_information',methods=['GET'])
def url_information():
    url = request.args.get('url')  # 假设参数名为param1
    title,favicon=get_title_and_favicon(url)
    print(title)
    print(favicon)
    data = {
        'title':title,
        'favicon':favicon
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=42001)