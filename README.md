# pyFax -- Python FAX Script


In 2024, some companies still require documents to be faxed to them. I wonder what percentage of households or businesses still own a fax machine. Despite the availability of email and other methods, they continue to prefer receiving documents via fax. So, let's create a fax script. Feel free to use this. - Isao


flask is the web framework.
pdf2image converts PDF files to images.
Pillow is used for handling images in Python.


Using Twillo Api

pip install requests twilio


Own server - 

curl -X POST -F "file=@/path/to/your/sample.pdf" -F "fax_number=1234567890" http://127.0.0.1:5000/send_fax
API END Point Server Asterisk