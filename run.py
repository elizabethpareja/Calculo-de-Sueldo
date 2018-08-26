from flask import render_template, request, session, redirect, url_for, Flask

host = "0.0.0.0"
port = 80
app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=["POST", "GET"])
@app.route('/index', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		sueldo = request.form["sueldo"]
		afp = request.form["afp"]
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True,host=host,port=port)