from flask import Blueprint, Flask, current_app, render_template, request
from yahoo_fin import stock_info

api = Blueprint("stock_watcher", __name__)


@api.route("/", methods=["GET"])
def watcher():
    stock = request.args.get("stock", default="", type=str)
    if not stock:
        return render_template("stock_watcher/watcher.html", price="Unknown Stock")
    price = round(stock_info.get_live_price(stock), 2)
    return render_template("stock_watcher/watcher.html", stock=stock, price=price)
