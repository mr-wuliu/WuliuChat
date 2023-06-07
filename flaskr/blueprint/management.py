from flask import (
    Blueprint, render_template, jsonify, request
)
from flaskr.models import Post, Config, User, Channel
from flaskr.extensions import db
from flaskr.models import User

bp =Blueprint('management', __name__)

@bp.route('/panel/dash')
def management_dash():
    return render_template('auth/manage_dash.html')

@bp.route('/panel/user')
def management_user():
    return render_template('auth/manage_user.html')

@bp.route('/data', methods=['GET'])
def getdata():
    if request.method == 'GET':
        print("收到请求")
        return jsonify({'month':['January', 'Februrary ', 'March', 'April', 'May', 'June'],'value':[100,200,300,500,600,1000]})
@bp.route('/user_info',methods=['GET'])
def getUserInfo():
    # TODO 权限管理
    import json

    if request.method == 'GET':
        print("收到请求, 返回用户信息")
        user_list = db.session.query(User.id, User.username, User.like).paginate(page=1, per_page=10, error_out=False).items
        results = [tuple(row) for row in user_list]
        return jsonify(results)
