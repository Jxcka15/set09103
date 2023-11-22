from flask import Flask
from extensions import db
from views import views  # make sure 'views' is accessible as a module or package

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create tables

    app.register_blueprint(views, url_prefix="/")  # Register the blueprint, with optional prefix

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)

