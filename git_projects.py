import requests
from config import *

response = requests.get(URL)
data = response.json()

print(data)