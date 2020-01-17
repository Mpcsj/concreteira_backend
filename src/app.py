from src.config.config_server import create_flask_server
from src.util.util_files import get_email_credentials
from flask_mail import Mail
app = create_flask_server()
email_credentials = get_email_credentials()
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = email_credentials['email'],
    MAIL_PASSWORD = email_credentials['password']
)
mail = Mail()
mail.init_app(app)
if __name__ == '__main__':
    app.run(host='localhost',port= 5000,debug = True)