from flask import Flask

def configure_blueprint(flask_app):
    from src.resources.resources import app_resources,endpoint1
    flask_app.register_blueprint(app_resources, url_prefix='/{}'.format((endpoint1)))

def create_flask_server():
    app = Flask(__name__)
    configure_blueprint(app)
    return app