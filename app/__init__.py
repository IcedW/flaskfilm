from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.controllers.film_controller import film_bp

    app.register_blueprint(film_bp)

    return app