import requests

url = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=1&page=1"
response = requests.get(url)
data = response.json()

print(data)