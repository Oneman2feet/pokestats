from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Markup
import extractor

app = Flask(__name__)

@app.route('/')
def main():
	return redirect("/magikarp")

@app.route('/<name>')
def search(name):
	name = name.replace(' ','_').title()
	content = extractor.getInfo(name)

	if (content==None):
		name = "Pokemon does not exist"
		return render_template('template.html',name=name
										  ,types=""
										  ,stats=""
										  ,locs=""
										  ,type=""
										  ,EVs=""
										  ,catchRate=""
										  ,evolutions=""
										  ,abilities="")

	return render_template('template.html',name=name
										  ,types=Markup(content[0])
										  ,stats=Markup(content[1])
										  ,locs=Markup(content[2])
										  ,type=Markup(content[3])
										  ,EVs=Markup(content[4])
										  ,catchRate=Markup(content[5])
										  ,evolutions=Markup(content[6])
										  ,abilities=Markup(content[7]))
  
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=1234, debug=True)
