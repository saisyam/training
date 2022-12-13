from top_repos import *
from model import *
from loadenv import *
# wendy = db_session.query(License).filter_by(name='wendy').one() 


# def my_filter(query):
#     return query.filter_by(name='"MIT License"')

# name = my_filter(db_session.query(License))

# for i in range(1,6):
# URI = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&page=1"

# db_session = create_session()
# resp = requests.get(URI)
# if resp.status_code == 200:
#     data = resp.json()

result=db_session.query(License)
for row in result:
    print(row.key,row.name,row.spdx_id,row.url,row.node_id)
