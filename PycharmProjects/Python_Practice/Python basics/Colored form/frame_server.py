from flask import Flask, render_template, request
# from wtf import StringField

app = Flask(__name__)

def change():
	color = input()

@app.route("/", methods = ['POST', 'GET'])
def index():
	color = 'grey'
	if request.method == 'POST': 
		color = request.form['color']
	return render_template('form.html', color=color)

# @app.route("/red")
# def red_color():
#     return render_template('form.html')

if __name__ == '__main__':
    app.run(debug = True)