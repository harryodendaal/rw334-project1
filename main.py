from scraper import github_api, scrape_github
from flask import Flask, request, render_template
app = Flask(__name__)

# data = [
# {
#   'repo_name':'openvc/opencv',
#   'description':'Open Source Computer Vision Library',
#   'num_stars':52800,
#   'language':'C++',
#   'license':None,
#   'last_updated':'2021-03-07T20:18:592',
#   'has_issues':True
# },
# {
#   'repo_name':'openvc/opencv',
#   'description':'Open Source Computer Vision Library',
#   'num_stars':300,
#   'language':'python',
#   'license':'BSD-3-Clause "New" or "Revised" License',
#   'last_updated':'2021-03-07T20:18:592',
#   'has_issues':True
# }
# ]

@app.route('/', methods=['GET', 'POST'])
def home():
  
  if request.method == 'POST':
    form_data = request.form
    # print("this is the form data: f", form_data)
    search_data = form_data['search']
    # print("this is search data: ", search_data)
    if 'api' in request.form:
      # replace data with actual data
      Apidata = github_api(search_term=search_data)
      return render_template('home.html', apiData=Apidata)
    elif 'scrapper' in request.form:
      scrapedData = scrape_github(search_term=search_data)
      return render_template('home.html', scrapeData = scrapedData)
    
  elif request.method == 'GET':
    return render_template('home.html')

if __name__ == '__main__':
   
  app.run(debug=True)

