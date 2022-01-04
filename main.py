from flask import Flask
from app import views
app = Flask(__name__)

# url
app.add_url_rule('/','index',views.index,methods=['GET'])
app.add_url_rule('/upload','upload',views.upload,methods=['POST'])
# run
if __name__ == '__main__':
    app.run(debug=True)