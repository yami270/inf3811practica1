from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Estudiante'):
	return render_template('index.html', name=name)

if __name__ == '__main__':
	app.run(debug=True, port=5001)