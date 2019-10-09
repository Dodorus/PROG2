from flask import Flask

app = Flask("Demo")

@app.route('/project/')
@app.route('/project/<name>')
def begruessung(name=False):
    if name:
         def hello_world():
		    return render_template('index.html', name="Startseite")
    elif:
        def hello_world2():
		    return render_template('index.html', name="Warenkorb")
	elif:
        def hello_world3():
		    return render_template('index.html', name="Warenkorb")

if __name__ == "__main__":
    app.run(debug=True, port=5000)