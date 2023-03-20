from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename

# constante para evidenciar o projeto Flask
project = Flask(__name__ , template_folder='templates')
# costante do endereço para armazenar a imagem
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads") 

# ROTA PRINCIPAL
@project.route("/")
def index():
    return render_template('base.html')

# ROTA DE UPLOAD
@project.route('/uploads', methods=['POST'])
def upload():
    try:
        file = request.files['image']
        savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(savePath)
        return render_template('base.html')
    except Exception as error:
        print("Erro", error)

# ROTA PARA PEGAR A IMAGEM
@project.route('/image/<filename>')
def image(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + ".jpg")
    return send_file(file, mimetype="image/jpg")


if __name__ == "__main__":
    project.run(debug=True,port=1256)