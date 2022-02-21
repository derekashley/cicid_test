from flask import Flask
import random
app = Flask(__name__)
api = Api(app)

@app.route('/helloworld', methods = ['POST'])
def helloworld():
  return str('Hello')

if __name__ == '__main__':
    app.run()  # run our Flask app
