from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    # api들 등록 예시
    # from .users import user_controller
    # app.register_blueprint(user_controller.bp)

    from .gangnam import gagnam_controller

    app.register_blueprint(gagnam_controller.bp)

    return app
