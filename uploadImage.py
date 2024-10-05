import os

from PackageInstaller import InstallPackages

try:
    from flask import Flask, render_template, request, send_file, redirect
except:
    InstallPackages()

from OptimizeImage import ImageOptimization

app = Flask(__name__, template_folder='Templates')

# Folder to store uploaded images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def home():
    return render_template('upload.html')


# Route to handle image upload and optimization
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, "test.jpg")
        file.save(filepath)

        processed_image_path = ImageOptimization.optimize_image(filepath)

        return send_file(processed_image_path, mimetype='image/jpeg')




if __name__ == '__main__':
    app.run(debug=True)
