from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/send_fax', methods=['POST'])
def send_fax():
    pdf = request.files['file']
    fax_number = request.form['fax_number']
    
    # Save the PDF locally
    pdf.save('/tmp/fax_document.pdf')
    
    # Convert PDF to TIFF
    subprocess.run(['convert', '/tmp/fax_document.pdf', '/tmp/fax_document.tiff'])
    
    # Send the fax using Asterisk or another service
    result = subprocess.run(['asterisk', '-rx', f'sendfax /tmp/fax_document.tiff to {fax_number}'])
    
    if result.returncode == 0:
        return jsonify({'status': 'Fax sent successfully!'}), 200
    else:
        return jsonify({'status': 'Fax failed to send.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
