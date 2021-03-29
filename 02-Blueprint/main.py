from flask import Flask, render_template
from admin.second import second_01

app = Flask(__name__)
app.register_blueprint(second_01, url_prefix="/admin")

@app.route("/test")
def test():
    return "<h1>Test</h1>"

if __name__== "__main__":
    app.run(debug=True)