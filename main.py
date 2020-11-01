import os
import re
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'

def analyze():
  file = open("uploads/file.txt", "r")
  lines = file.readlines()
  result = []
  total = 0
  counts = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
  }
  for x in range(len(lines)):
    if x>0:
      convertLine = re.sub('\t',' ',lines[x])
      value = convertLine.strip("\n").split(" ")[-1]
      counts[value[0]] = (counts[value[0]]) + 1
      total = total + 1
  for key in counts:
    result.append(float("{:.1f}".format(counts[key]/total*100)))
  return result


@app.route("/")
def home():
  return render_template("base.html", results=False)

@app.route("/", methods = ['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
      uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], 'file.txt'))
      data = analyze()
      return render_template("base.html", results={'data': data})

if __name__ == "__main__":
  app.run(host= '0.0.0.0')