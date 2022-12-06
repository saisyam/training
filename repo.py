import requests
from model import *
from db import *

URI = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&page=1"

db_session = create_session()
resp = requests.get(URI)
if resp.status_code == 200:
    data = resp.json()
    items = data['items']
    for item in items:
        license = License(
            key = item['license']['key'],
            name = item['license']['name'],
            spdx_id = item['license']['spdx_id'],
            url = item['license']['url'],
            node_id = item['license']['node_id']
        )
        db_session.add(license)
        db_session.commit()
        print(license)
        repository = Repository(
    id = item['id'],
    name = item['name'],
    node_id = item['node_id'],
    full_name = item['full_name'],
    private = item['private'],
    size = item['size'],
    license_id = license.id
    )
        print(repository)
        db_session.add(repository)
        db_session.commit()
else:
    print("Failed to get data")