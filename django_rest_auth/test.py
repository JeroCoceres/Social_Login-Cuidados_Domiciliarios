import smtplib
from email.mime.text import MIMEText

# Configuración de Mailtrap
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '5e44c87de8775b'
EMAIL_HOST_PASSWORD = '********b003'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
FROM_EMAIL = 'jeronimococeres@gmail.com'
TO_EMAIL = 'recipient@example.com'

def send_test_email():
    try:
        msg = MIMEText('This is a test email.')
        msg['Subject'] = 'Test Email'
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL

        print("Connecting to server...")
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            if EMAIL_USE_TLS:
                server.starttls()
            print("Logging in...")
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            print("Sending email...")
            server.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

send_test_email()
