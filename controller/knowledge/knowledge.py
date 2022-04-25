from flask import Blueprint, render_template, request

knowledge = Blueprint('knowledge', __name__)


# 增删改查问答对
@knowledge.route("/listView", methods=['GET', 'POST'])
def listView():
    return render_template('/knowledge/listView.html')
