from scraper import github_api, scrape_github
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  
  if request.method == 'POST':
    form_data = request.form
    # print("this is the form data: f", form_data)
    search_data = form_data['search']
    num_pages = form_data['num_pages']
    # print("this is search data: ", search_data)
    if 'api' in request.form:
      # replace data with actual data
      Apidata = github_api(search_term=search_data, num_pages=num_pages)
      return render_template('home.html', apiData=Apidata)
    elif 'scrapper' in request.form:
      scrapedData = scrape_github(search_term=search_data, num_pages=num_pages)
      return render_template('home.html', scrapeData = scrapedData)
    
  elif request.method == 'GET':
    return render_template('home.html')

if __name__ == '__main__':
   
  app.run(debug=True)

