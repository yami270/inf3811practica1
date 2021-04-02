from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return 'este es un pequeño saludo'

if __name__ == '__main__':
	app.run(debug=True, port=5001)