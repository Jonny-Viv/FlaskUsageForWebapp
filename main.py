# importing the flask package
import flask

# initialiating a flask website object that originates from __name__
app = flask.Flask(__name__)

#this is a routing decorator that sends the result of the function to our webapp
@app.route("/")
def main():
  return "Hello Dear👋"
  
# this function redirects the user to google.com
@app.route("/google")
def google():
  return flask.redirect("https://google.com")

@app.route("/template")
def template():
  x = 3
  return flask.render_template("template.html", x=x)

@app.route("/variable/(var)")
def variable(var):
  return "The\"secret\"variable is{}".format(var)

@app.route("/squalculator",methods=["GET", "POST"])
def calculator():
  if flask.request.method == "GET":
    return flask.render_template("squalculator.html", result="na")

  if flask.request.method == "POST":
    value = flask.request.form["input"]
    squared_value = int(value)**2
    return flask.render_template("squalculator.html", result=squared_value)

app.run(host="0.0.0.0", port=3000, debug=True)