from flask import Flask, render_template, request
from extractors.ps_expired import extract_ps_expired_paging

app = Flask("jobScrapper")

title = "PS Plus Game Catalog"

@app.route("/")
def index():
    return render_template("index.html", title=title)

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    before_games = extract_ps_expired_paging()
    games = []
    if keyword == "all":
        games = before_games
    else :
        for game in before_games:
            if game["ps_expired_flag"]:
                games.append(game)

    return render_template("search.html", games=games)

app.run("0.0.0.0")