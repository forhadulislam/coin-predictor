from flask import Flask, render_template
from libs.scrap import getCoins


app = Flask(__name__)

@app.route("/")
def main():
    coins = getCoins()
    return render_template('index.html', data= coins)

@app.route("/<int:post_id>")
def helloID(post_id):
    return render_template('index.html', post_id=post_id )

if __name__ == "__main__":
    app.run()