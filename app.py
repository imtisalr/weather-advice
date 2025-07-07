from flask import Flask
from flask import request
import main.py

app = Flask(__name__)

@app.route("/")
def index():
    city = request.args.get("city")
    if city:
        suggestion = main.main(city)
    else:
        suggestion = "waiting for input"
    return ( """<h1>Today's Weather Suggestion</h1>
             <form action="" method="get">
                <input type="text" name="city">
                <input type="submit" value="Suggest!">
              </form>"""
              + "Suggestion: "
              + suggestion
    )


if __name__ == "__main__":
     app.run(host="127.0.0.1", port=8080, debug=True)