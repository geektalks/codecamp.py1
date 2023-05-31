from flask import Flask, render_template, jsonify

app = Flask(__name__)

COURSE= [
  {'ID':1,'Name': 'Python','Duration': '3 Months','Mode':'Online'},
  {'ID':2,'Name': 'Java','Duration': '3 Months','Mode':'Online'},
  {'ID':3,'Name': 'Web Development','Duration': '1 Month',},
  {'ID':4,'Name': 'Flutter','Duration': '4 Months','Mode':'Online'}
]


@app.route("/")
def hello_world():
  return render_template('home.html',course=COURSE, course_provider='CODE')


@app.route("/api/course")
def list_course():
  return jsonify(COURSE)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
