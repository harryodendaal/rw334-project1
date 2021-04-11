# scraping functions

import requests
from bs4 import BeautifulSoup

def scrape_github(search_term, num_pages=1):
  """Scrapes github reps fro mthe given search term

  Parameters
  ---------
  search_term : str
    The search term for the github repositories

  num_pages: int
    The number of pages to scrape

  Returns 
  -------
  scraped_info : list
    A list of dictionaries containing the necessary information
    from the scraped repos
  
  """
  if search_term.strip() == "":
    return []

  link = "https://github.com/search?o=desc&q=" + search_term + "&s=stars&type=Repositories"

  response = requests.get(link)

  dom = BeautifulSoup(response.content, 'html.parser')

  repos = dom.find_all('li', class_='repo-list-item')

  output = []

  for ele in repos:
    repo_name = ele.find('a', class_='v-align-middle').text if ele.find('a', class_='v-align-middle').text != None else None
    description = str(ele.find('p', class_="mb-1").text).strip() if ele.find('p', class_='mb-1').text != None else None
    tags_unprocessed = ele.find_all('a', class_='topic-tag')
    tags_processed = []
    for tag in tags_unprocessed:
      tags_processed.append(str(tag.text).strip())

    num_stars = str(ele.find('a', class_='Link--muted').text).strip() if ele.find('a', class_='Link--muted').text != None else None
    language = str(ele.find('span', itemprop='programmingLanguage').text).strip() if ele.find('span', itemprop='programmingLanguage') != None else None
    license_unprocessed = ele.find_all('div', class_='mr-3')

    license = None
    for div in license_unprocessed:
       license = str(div.text).strip() if 'license' in div.text else license
  
    last_updated = str(ele.find('relative-time')['datetime']) if ele.find('relative-time') != None else None
    # holy mackerel that sure is long and uglY? o well takes the singular/ first digit out of a sentence if there is  a sentence.
    num_issues = [int(s) for s in str(ele.find('a', class_='Link--muted f6').text).split() if s.isdigit()][0] if ele.find('a', class_='Link--muted f6') != None else None

    repo = {
      'repo_name':repo_name,
      'description':description,
      'tags':tags_processed if tags_processed != None else None,
      'num_stars':num_stars,
      'language':language,
      'license':license,
      'last_updated':last_updated,
      'num_issues': num_issues
    }

    output.append(repo)


  return output



def github_api(search_term, num_pages=1):
  """Searches for repositories with the given search term using
    the GitHub REST API

  Parameters
  ---------
  search_term : str
    The search term for the github repositories 
  num_pages : int 
    The number of pages required to query for repositories

  Returns
  -------
  repo_info : list 
   A list of dictionaries containing the necessary
   info from the repositories
  """

  if search_term.strip() == "":
    return []


  link = "https://api.github.com/search/repositories?q=" + search_term + "&sort=stars&order=desc&per_page=10"

  response = requests.get(link)
  repos = response.json()

  output = []

  for i in range(0, 10):
    # create dictionary
    #licence
    repo = {
      "repo_name": repos['items'][i]['full_name'] if repos['items'][i]['full_name'] != None else None,
      "description":repos['items'][i]['description'] if repos['items'][i]['description'] != None else None,
      "num_stars": int(repos['items'][i]['stargazers_count']) if repos['items'][i]['stargazers_count'] != None else None,
      "language":repos['items'][i]['language'] if repos['items'][i]['language'] != None else None,
      "license": repos['items'][i]['license']['name'] if repos['items'][i]['license'] != None and repos['items'][i]['license']['name'] != None and repos['items'][i]['license']['name'] != "Other" else None,
      "last_updated":repos['items'][i]['updated_at'] if repos['items'][i]['updated_at'] != None else None,
      "has_issues":True if repos['items'][i]['has_issues'] == True else False
    }
    # add to list
    output.append(repo)

  return output

