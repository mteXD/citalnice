from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/izobrazba")
def izobrazba():
	return render_template('izobrazba.html')

@app.route("/vestniki")
def vestniki():
	return render_template('vestniki.html')

@app.route("/zgodovina")
def zgodovina():
	return render_template('zgodovina.html')

if __name__ == "__main__":
	app.run(debug=True)