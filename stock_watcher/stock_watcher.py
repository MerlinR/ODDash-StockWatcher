from flask import Blueprint, Flask, current_app, render_template, request

api = Blueprint("stock_watcher", __name__)


@api.route("/", methods=["GET"])
def watcher():
    return render_template("stock_watcher/watcher.html")
