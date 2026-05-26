from flask import Flask, render_template, request
from datetime import datetime

from wordpress import fetch_posts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():

    report = None

    if request.method == "POST":

        client_name = request.form["client"]

        month_input = int(request.form["month"])

        year_input = int(request.form["year"])

        posts = fetch_posts(client_name)

        total_blogs = len(posts)

        filtered_posts = []

        for post in posts:

            post_date = post["date"]

            dt = datetime.strptime(
                post_date,
                "%Y-%m-%dT%H:%M:%S"
            )

            if dt.month == month_input and dt.year == year_input:
                filtered_posts.append(post)

        filtered_count = len(filtered_posts)

        month_name = datetime(
            1900,
            month_input,
            1
        ).strftime('%B')

        report = {
            "client": client_name,
            "total": total_blogs,
            "month": month_name,
            "year": year_input,
            "count": filtered_count
        }

    return render_template(
        "index.html",
        report=report
    )

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)