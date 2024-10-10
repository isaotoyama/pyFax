import os
from twilio.rest import Client

# Set your Twilio credentials (or another service's credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_FAX_NUMBER = 'your_twilio_fax_number_here'
TO_FAX_NUMBER = 'recipient_fax_number_here'

# PDF file to send
pdf_file_path = '/path/to/your/file.pdf'

# Create a Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Open the PDF file and convert it to a URL accessible for the fax service.
# Note: Twilio requires files to be accessible via a URL. You may need to upload it to a service like S3.
pdf_url = 'https://your-public-url.com/file.pdf'

try:
    # Send the fax
    fax = client.fax.faxes.create(
        from_=TWILIO_FAX_NUMBER,
        to=TO_FAX_NUMBER,
        media_url=pdf_url
    )

    print(f"Fax sent! Fax SID: {fax.sid}")
except Exception as e:
    print(f"Failed to send fax: {e}")
