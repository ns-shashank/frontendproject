from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'FrontEnd Engineer',
    'location': 'Remote',
    'salary': ''
}, {
    'id': 4,
    'title': 'BackEnd Engineer',
    'location': 'hydrabad, India',
    'salary': 'Rs. 12,00,000'
}]


@app.route('/')
def shashank():
  return render_template("index.html", jobs=JOBS, Company_name="Shashank")


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
