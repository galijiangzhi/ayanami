from flask import Flask,render_template,request,redirect,jsonify
from flask_cors import CORS
from methods.get_title_and_favicon import get_title_and_favicon
from tools import db
import tianqi
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
@app.route('/get_data',methods=['GET'])
def get_data():
    id = request.args.get('id')
    id = 'default' if id=='' else id
    reque_data = "SELECT * FROM data WHERE id = '"+ str(id) +"';"
    print(reque_data)
    data=db.execute_query(reque_data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=42006)