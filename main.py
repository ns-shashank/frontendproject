from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def shashank():
  return render_template('home.html')  # Use the correct template name here

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)