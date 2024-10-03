from flask import Flask

app = Flask(__name__)


@app.route('/shank')
def index():
    return 'I am Shashank'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
