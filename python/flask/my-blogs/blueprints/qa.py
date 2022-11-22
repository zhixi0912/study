from flask import Blueprint, render_template, request


bp = Blueprint("qa", __name__, url_prefix="/")

@bp.route("/")
def index():
    return render_template("qa.html")

@bp.route("/qa/public", methods=['GET', 'POST'])
def public_qa():
    if request.method == 'GET':
        return render_template("public_question.html")