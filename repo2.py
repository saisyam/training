# import psycopg2
# import json
import requests
# import os
# import time
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import *
#from urllib.request import Request, urlopen

from model import *
from model2 import *
#from repo import *
from db import *


db_session = create_session()
users=db_session.execute(select(Repository.commits_url))
#print(users)

for i in users:
    x=i.commits_url[:-6]
    responce=requests.get(x)
    print(responce.status_code)
    if responce.status_code==200:
        commits_url=responce.json()
       #print(commits_url)
  
        for j in range(len(commits_url)):
            
            parents=Parents(
                sha=commits_url[j]['sha'],
                url=commits_url[j]['url'],
                html_url=commits_url[j]['html_url']

            )
            db_session.add(parents)
            db_session.commit()
            print(parents)

            commit=Commit(
                message=commits_url[j]['commit']['message'],
                url=commits_url[j]['url'],
                comment_count=commits_url[j]['comment_count']

            )
            db_session.add(commit)
            db_session.commit()
            print(commit)


            commit_author=Commit_author(
                name= commits_url[j]['name'],
                email=commits_url[j]['email'],
                date=commits_url[j]['email']
            )    
            db_session.add(commit_author)
            db_session.commit()
            print(commit_author)

            commit_committer=Commit_committer(
                name= commits_url[j]['name'],
                email=commits_url[j]['email'],
                date=commits_url[j]['email']
	        )
            db_session.add(commit_committer)
            db_session.commit()
            print(commit_committer)

            commit_tree=Commit_tree(
                sha=commits_url[j]['sha'],
                url=commits_url[j]['url']
	            
            ) 
            db_session.add(commit_tree)
            db_session.commit()
            print(commit_tree)

            commit_verification=Commit_verification(
                verified=commits_url[j]['verified'],
                reason=commits_url[j]['reason'],
	            signature=commits_url[j]['signature'],
                payload=commits_url[j]['payload']
            )
            db_session.add(commit_verification)
            db_session.commit()
            print(commit_verification)

            author= Author(
                login =commits_url[j]['login'],
	            id =commits_url[j]['id'],
	            node_id  =commits_url[j]['node_id'],
	            avatar_url  =commits_url[j]['avatar_url'],
	            gravatar_id  =commits_url[j]['gravatar_id'],
	            url  =commits_url[j]['url'],
	            html_url  =commits_url[j]['html_url'],
	            followers_url  =commits_url[j]['followers_url'],
	            following_url =commits_url[j]['following_url'],
	            gists_url  =commits_url[j]['gists_url'],
	            starred_url  =commits_url[j]['starred_url'],
	            subscriptions_url  =commits_url[j]['subscriptions_url'],
	            organizations_url  =commits_url[j]['organizations_url'],
	            repos_url  =commits_url[j]['repos_url'],
	            events_url  =commits_url[j]['events_url'],
	            received_events_url  =commits_url[j]['received_events_url'],
	            type  =commits_url[j]['type'],
	            site_admin =commits_url[j]['site_admin']

            )
            db_session.add(author)
            db_session.commit()
            print(author)

            committer= Committer(
                login =commits_url[j]['login'],
	            id =commits_url[j]['id'],
	            node_id  =commits_url[j]['node_id'],
	            avatar_url  =commits_url[j]['avatar_url'],
	            gravatar_id  =commits_url[j]['gravatar_id'],
	            url  =commits_url[j]['url'],
	            html_url  =commits_url[j]['html_url'],
	            followers_url  =commits_url[j]['followers_url'],
	            following_url =commits_url[j]['following_url'],
	            gists_url  =commits_url[j]['gists_url'],
	            starred_url  =commits_url[j]['starred_url'],
	            subscriptions_url  =commits_url[j]['subscriptions_url'],
	            organizations_url  =commits_url[j]['organizations_url'],
	            repos_url  =commits_url[j]['repos_url'],
	            events_url  =commits_url[j]['events_url'],
	            received_events_url  =commits_url[j]['received_events_url'],
	            type  =commits_url[j]['type'],
	            site_admin =commits_url[j]['site_admin']

            )
            db_session.add(committer)
            db_session.commit()
            print(committer)


            main=Main(
                sha=commits_url[j]['sha'],
                node_id=commits_url[j]['node_id'],
                url=commits_url[j]['url'],
                html_url=commits_url[j]['html_url'],
                comments_url=commits_url[j]['comments_url'],
                parents_id=parents.id,
                commit_message=commit.message,
                commit_author_id=commit_author.id,
                commit_committer_id=commit_committer.id,
                commit_tree_id=commit_tree.id,
                commit_verification_id=commit_verification.id,
                author_id=author.id,
                committer_id=committer.id    
            )
            db_session.add(main)
            db_session.commit()
            print(main)
    else:
        print("Failed to get data")        