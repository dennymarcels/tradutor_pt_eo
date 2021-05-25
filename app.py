from flask import Flask, request, render_template
import commons

app = Flask(__name__)

@app.route('/')
def method():
    return render_template("index.html")

@app.route('/response')
def response():
   texto = request.args.get('jsdata')
   return render_template("traducao.html", traducao = commons.traduzir(texto))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)