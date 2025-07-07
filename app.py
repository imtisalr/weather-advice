from flask import Flask, render_template
from flask import request
import main

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    city = request.args.get("city")
    if city:
        suggestion = main.main(city)
    else:
        suggestion = "waiting for input"
    return render_template('index.html', suggestion=suggestion)
    # return ( """<h1>Today's Weather Suggestion</h1>
    #          <form action="" method="get">
    #             <input type="text" name="city">
    #             <input type="submit" value="Suggest!">
    #           </form>"""
    #           + "Suggestion: "
    #           + suggestion
    # )


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080, debug=True)