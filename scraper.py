import requests
from bs4 import BeautifulSoup
import re


def get_citations_needed_count():
  print("What page are you looking to see if citations are needed")
  query = input("> ")
  URL = "https://en.wikipedia.org/wiki/" + query
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")
  count_needed = 0
  for a in soup.find_all('a', href="/wiki/Wikipedia:Citation_needed"):
    count_needed += 1
  print(f"{URL} has {count_needed} different citation(s) needed")


def get_citations_needed_report():
  print("What page are you looking to see if citations are needed")
  query = input("> ")
  URL = "https://en.wikipedia.org/wiki/" + query
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  broth = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
  
  for p in broth:
    bones = p.parent.parent.parent
    bones = str(bones)
    regex = r"<[^<>]+>"
    meat =  re.sub(regex, '', bones)
    print(meat)


if __name__ == "__main__":
  import sys

  print(
    '''
    ********************************************
    **                                        **
    **  Welcome to the Wiki Citation Scraper  **
    **                                        **
    ********************************************
    **                                        **
    **   Please make a selection to continue  **
    **                    or                  **
    **          Type "quit" to quit           **
    **                                        **
    ********************************************
    '''
)
  def start():
    print(
    '''
    ********************************************
    **   Type in "count" to find the number   **
    **    of citations needed for an article  **
    **                    or                  **
    **  Type "content" to find what snippets  **
    **   of an article which need citations   **
    ********************************************
    ''')

    while True:
      selection = input("> ").lower()
      if selection == "quit":
        sys.exit()
      if selection == "count":
        get_citations_needed_count()
        print("Type in 'c' to continue or 'q' to quit")
        selection = input("> ")
        if selection == "c":
          start()
        if selection == "q":
          sys.exit()
      elif selection == "content":
        get_citations_needed_report()
        print("Type in 'c' to continue or 'q' to quit")
        selection = input("> ")
        if selection == "c":
          start()
        if selection == "q":
          sys.exit()
        start()
      else:
        print('please make a valid selection or "quit" to quit')

  start()