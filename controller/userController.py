from flask import Blueprint
from model.article import article
from model.userModel import userModel
from flask import request ,jsonify

obj=userModel()

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users')
def user_signup_controller():
    return obj.user_signup_model()


@user_controller.route('/users/getall')
def get_all_users():
    return obj.getUsers()


@user_controller.route('/users/adduser',methods=["POST"])
def addUser():
    # "request form help us to get data from server sidre to us"
    print()
    return obj.add_user(request.form)

@user_controller.route('/users/updateuser',methods=["PUT"])
def updateUser():
    return obj.update_user(request.form)

@user_controller.route('/users/deleteuser/<id>',methods=["DELETE"])
def deleteUser(id):
    return obj.delete_user(id)


@user_controller.route('/users/patchuser/<id>',methods=["PATCH"])
def patchUser(id):
    return obj.patch_user(request.form , id)


@user_controller.route('/users/getall/limit/<limit>/page/<page>',methods=["GET"])
def userPagination(limit ,page):
    return obj.pagination_user(limit ,page)


