import os

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

from inference import get_prediction
from commons import format_class_name


app = Flask(__name__)


def create_folder(path):
    """ create folder if absent """
    if os.path.isdir(path) == False:
        os.mkdir(path)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("redirection")
            return redirect(request.url)
        
        files = request.files.getlist("file")

        preds = {}

        for file in files:

            img_bytes = file.read()
            class_name ,class_id, img = get_prediction(image_bytes=img_bytes)
            preds[file.filename] = (class_name, class_id)
            res_path = ""

            if class_name == 'AbdomenCT':
                create_folder("./static/AbdomenCT")
                path = './static/AbdomenCT/'
                img.save(path + secure_filename(file.filename))

            elif class_name == 'Hand':
                create_folder("./static/Hand")
                path = './static/Hand/'
                img.save(path + secure_filename(file.filename))

            elif class_name == 'ChestCT':
                create_folder("./static/ChestCT")
                path = './static/ChestCT/'
                img.save(path + secure_filename(file.filename))

            elif class_name == 'CXR':
                create_folder("./static/CXR")
                path = './static/CXR/'
                img.save(path + secure_filename(file.filename))

            elif class_name == 'BreastMRI':
                create_folder("./static/BreastMRI")
                path = './static/BreastMRI/'
                img.save(path + secure_filename(file.filename))

            else:
                create_folder("./static/HeadCT")
                path = './static/HeadCT/'
                img.save(path + secure_filename(file.filename))

        return render_template('result.html', preds = preds, path = res_path)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
