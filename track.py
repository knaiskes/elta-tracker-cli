from bs4 import BeautifulSoup
import requests

url = "https://www.elta.gr/en-us/personal/tracktrace.aspx?qc="

print("Enter your tracking number: ")
tracking_number = input()

url = url + tracking_number 

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

rows = []

table = soup.find("table", {"class": "tg"})

try:
    for row in table.find_all("tr"):
        rows.append(row.text)

    for r in reversed(rows[2: -1]):
        print(r)
except IndexError:
    print("There are not any tracking information at the moment")
    print("Check your tracking number or try again later!")
