from sqlalchemy import select
from model import *
from item_queries import *
from loadenv import *

def insert_into_commit_branch(commit):
    if dat[branch]['commit']['sha'] not in  sha_unique_list:
        sha_unique_list.append(commit['sha'])
        commit_branch_url=Commit_branch_url(
            sha=commit['sha'],
            url=commit['url']
        )
        db_session.add(commit_branch_url)
        db_session.commit()
        return True

def insert_into_branch(branch,commit):

    branch_url=Branch_url(    
        name=branch['name'],
        protected=branch['protected'],
        commit_sha=commit['sha']
    )
    db_session.add(branch_url)
    db_session.commit()
    return True

sha_unique_list=[]
sha_duplicate_list=[]
headers=authentication()
users = db_session.execute(select(Repository.branches_url))
for i in users:
    branches=i.branches_url
    x=branches[:-9]
    res = requests.get(x,headers=headers)
    if res.status_code == 200:
        dat=res.json()
        for branch in range(0,len(dat)):
            commit=dat[branch]['commit']
            insert_into_commit_branch(commit)
            branch=dat[branch]
            insert_into_branch(branch,commit)

