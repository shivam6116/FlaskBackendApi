from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from controller.userController import user_controller
from controller.productController import productController
from controller.rolesController import roleController


app = Flask(__name__)


app.register_blueprint(user_controller)
app.register_blueprint(productController)
app.register_blueprint(roleController)


@app.route("/home")
def home():
    return "this is home page"


if __name__ == '__main__':
    app.run(debug=True)
