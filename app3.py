from flask import Flask, request, send_file

from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Routes from app.py
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    image = request.files['image']
    picture = Image.open(image)
    img_io = BytesIO()
    picture.save(img_io, 'JPEG', optimize=True, quality=30)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')

# Routes from app2.py
@app.route('/second_page')
def second_page():
    return app.send_static_file('second.html')

@app.route('/compress2', methods=['POST'])
def compress2():
    image = request.files['image']
    picture = Image.open(image)
    img_io = BytesIO()
    picture.save(img_io, 'JPEG', optimize=True, quality=30)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')

if __name__ == '__main__':
    app.run(debug=True)

