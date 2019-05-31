from flask import Flask, request, Response
import json



app = Flask(__name__)



@app.route("/see", methods=["GET"])
def see():
    items= {}
    items['hello'] = "World"
    return Response(json.dumps(items), status=200, mimetype='application/json')





if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0',port=5050)