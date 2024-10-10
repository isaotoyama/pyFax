from flask import Flask, request, jsonify
from pdf2image import convert_from_path
import os

app = Flask(__name__)

# Path to store temporary files
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/send_fax', methods=['POST'])
def send_fax():
    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    fax_number = request.form.get('fax_number')

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    # Save PDF file to the temporary directory
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(pdf_path)

    # Convert the PDF to a TIFF file for fax compatibility
    images = convert_from_path(pdf_path)
    tiff_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{os.path.splitext(file.filename)[0]}.tiff")
    images[0].save(tiff_path, 'TIFF')

    # (Placeholder) Here, you would add your code to send the TIFF file using Asterisk

    return jsonify({
        'message': 'PDF successfully converted to TIFF',
        'tiff_file': tiff_path,
        'fax_number': fax_number
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
