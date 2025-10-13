
# Web Scraping Assignment using Python

# In this assignment, we will use "requests" and "BeautifulSoup" libraries to scrape data from websites. Each question is a small practice task.


import requests
from bs4 import BeautifulSoup

# ------------------- Question 1 -------------------
# Q1: Extract the first H1 heading and first paragraph from a webpage.
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Q1: H1 Text ->", soup.find("h1").text)
print("Q1: First Paragraph ->", soup.find("p").text)


# ------------------- Question 2 -------------------
# Q2: Print the title of a webpage.
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("\nQ2: Website Title ->", soup.title.text)


# ------------------- Question 3 -------------------
# Q3: Extract and print all links (anchor tags) from a webpage.
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("\nQ3: All Links ->")
for link in soup.find_all("a"):
    print(link.get("href"))


# ------------------- Question 4 -------------------
# Q4: Extract and print all paragraph texts from a webpage.
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("\nQ4: All Paragraphs ->")
for p in soup.find_all("p"):
    print(p.text)


# ------------------- Question 5 -------------------
# Q5: Use a for loop to extract the title and H1 of multiple websites.
import requests
from bs4 import BeautifulSoup

url = "https://httpbin.org/html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


if soup.title:
    print("Title:", soup.title.text)
else:
    print("No <title> tag found")

# H1 text
h1_tag = soup.find("h1")
if h1_tag:
    print("H1:", h1_tag.text)

# First Paragraph
p_tag = soup.find("p")
if p_tag:
    print("Paragraph:", p_tag.text)







# ------------------- Question 6 -------------------
# Q6: Use a while loop to print the titles of multiple websites.
urls = ["https://example.com", "https://httpbin.org/html"]
i = 0

while i < len(urls):
    response = requests.get(urls[i])
    soup = BeautifulSoup(response.text, "html.parser")
    print(f"\nQ6: Website {i+1}: {urls[i]}")
    if soup.title:
        print("Title:", soup.title.text.strip())
    else:
        print("No title found on this website.")
    i += 1


# ------------------- Question 7 -------------------
# Q7: Scrape a table from an alternative site and print its rows.
url = "https://www.contextures.com/xlSampleData01.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

print("\nQ7: Table Data ->")
for row in rows[:6]:  # first 5 rows only for short output
    cols = row.find_all(["td", "th"])
    data = [col.text.strip() for col in cols]
    print(data)


# # ------------------- Question 8 -------------------
# # Q8: Extract and print all image sources from a webpage.
# url = "https://www.python.org"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# print("\nQ8: Images on Website ->")
# for img in soup.find_all("img")[:5]:
#     print(img.get("src"))



# ------------------- Question 09 -------------------
# Q10: Extract the first paragraph from a Wikipedia article.
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

first_para = soup.find("p").text
print("\nQ10: Wikipedia First Paragraph ->\n", first_para)


# ------------------- Question 10 -------------------
# Q11: Scrape quotes and authors from "Quotes to Scrape" website.
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

print("\nQ11: Quotes from Website ->")
for i in range(min(len(quotes), 5)):   # first 5 quotes only
    print(f"Quote: {quotes[i].text} — {authors[i].text}")


