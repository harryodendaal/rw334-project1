from flask import Flask, request, render_template
app = Flask(__name__)

data = [
{
  'repo_name':'openvc/opencv',
  'description':'Open Source Computer Vision Library',
  'num_stars':52800,
  'language':'C++',
  'license':None,
  'last_updated':'2021-03-07T20:18:592',
  'has_issues':True
},
{
  'repo_name':'openvc/opencv',
  'description':'Open Source Computer Vision Library',
  'num_stars':300,
  'language':'python',
  'license':'BSD-3-Clause "New" or "Revised" License',
  'last_updated':'2021-03-07T20:18:592',
  'has_issues':True
}
]

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    if 'api' in request.form:
      print("we called api")
      return render_template('home.html', apiData=data)
    elif 'scrapper' in request.form:
      print('we called scrapper')
      return render_template('home.html')
    else:
      print(request.form)
    
  elif request.method == 'GET':
    return render_template('home.html')

if __name__ == '__main__':
   
  app.run(debug=True)

