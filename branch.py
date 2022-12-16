from sqlalchemy import select
from model import *
from db import *
from repo import *
import time
sha_unique_list = []
sha_duplicate_list = []
count = 0

obj_branch = db_session.execute(select(Repository.branches_url))
#print(obj_branch)
for i in obj_branch:
    #print(i)
    branches = i.branches_url
    #print(branches)
    branch_url = branches[:-9]
    #print(branch_url)
    resp = requests.get(branch_url)
    if resp.status_code == 200:
        branch_data = resp.json()
        #print(branch_data)
        for data in range(len(branch_data)):
            if branch_data[data]['commit']['sha'] not in sha_unique_list:
                sha_unique_list.append(branch_data[data]['commit']['sha'])
                commit_branch_url = Commit_branch_url(
                    sha =branch_data[data]['commit']['sha'],
                    url = branch_data[data]['commit']['url']
                )
                db_session.add(commit_branch_url)
                db_session.commit()
                db_session.expunge_all()

            branch_url=Branch_url(
                name=branch_data[data]['name'],
                protected=branch_data[data]['protected'],
                commit_sha=commit_branch_url.sha
            )
            db_session.add(branch_url)
            db_session.commit()
            db_session.expunge_all()
            count += 1
    else:
        time.sleep(3600)
        continue
print(count)
    


