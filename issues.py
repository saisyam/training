from sqlalchemy import select
from model import *
from top_repos import *
from loadenv import *
import time
sha_unique_list=[]
sha_duplicate_list=[]
count=0
users = db_session.execute(select(Repository.branches_url))
for i in users:
    branches=i.branches_url
    x=branches[:-9]
    res = requests.get(x)
    if res.status_code == 200:
        dat=res.json()
        for branch in range(0,len(dat)):
                if dat[branch]['commit']['sha'] not in  sha_unique_list:
                    sha_unique_list.append(dat[branch]['commit']['sha'])
                    commit_branch_url=Commit_branch_url(
                        sha=dat[branch]['commit']['sha'],
                        url=dat[branch]['commit']['url']
                    )
                    db_session.add(commit_branch_url)
                    db_session.commit()

                branch_url=Branch_url(    
                    name=dat[branch]['name'],
                    protected=dat[branch]['protected'],
                    commit_sha=commit_branch_url.sha
                )
                db_session.add(branch_url)
                db_session.commit()
                count=count+1
    else:
        time.sleep(3600)
        continue
print(count)
    









# user=db_session.query(Owner).filter(Owner.login.in_(["transitive-bullshit"])).all()
# for i in user:
#     print(i.__dict__)