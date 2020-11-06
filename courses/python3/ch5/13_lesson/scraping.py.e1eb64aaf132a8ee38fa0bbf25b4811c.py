import requests
from bs4 import BeautifulSoup as bs


url = "https://stackoverflow.com/questions/tagged/python"
response = requests.get(url)
html = bs(response.text, "html.parser")

for question in html.select(".question-summary"):
    title = question.select_one(".question-hyperlink")
    date = question.select_one(".relativetime")
    votes = question.select_one(".vote-count-post strong")

    print(f"[ {votes.text} ]", date.text, title.text, sep="\t")
