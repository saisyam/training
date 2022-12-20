# import psycopg2
# import json
import requests
# import os
import time
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import *


from model import *
from model2 import *
from db import *


db_session = create_session()
users=db_session.execute(select(Repository.commits_url))
#print(users)
count=0

for i in users:
    x=i.commits_url[:-6]
    #print(x)
    count=count+1
    headers=authentication()
    responce=requests.get(x,headers=headers)
    print(responce.status_code)
    try:
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
                    comment_count=commits_url[j]['commit']['comment_count']

                )
                db_session.add(commit)
                db_session.commit()
                print(commit)


                commit_author=Commit_author(
                    name= commits_url[j]['commit']['author']['name'],
                    email=commits_url[j]['commit']['author']['email'],
                    date=commits_url[j]['commit']['author']['date']
                )    
                db_session.add(commit_author)
                db_session.commit()
                print(commit_author)

                commit_committer=Commit_committer(
                    name= commits_url[j]['commit']['committer']['name'],
                    email=commits_url[j]['commit']['committer']['email'],
                    date=commits_url[j]['commit']['committer']['date']
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
                    verified=commits_url[j]['commit']['verification']['verified'],
                    reason=commits_url[j]['commit']['verification']['reason'],
                    signature=commits_url[j]['commit']['verification']['signature'],
                    payload=commits_url[j]['commit']['verification']['payload']
                )
                db_session.add(commit_verification)
                db_session.commit()
                print(commit_verification)

                try:
                    if  commits_url[j]['author'] is not None:   
                        author= Author(
                            login =commits_url[j]['author']['login'],
                            id =commits_url[j]['author']['id'],
                            node_id  =commits_url[j]['author']['node_id'],
                            avatar_url  =commits_url[j]['author']['avatar_url'],
                            gravatar_id  =commits_url[j]['author']['gravatar_id'],
                            url  =commits_url[j]['author']['url'],
                            html_url  =commits_url[j]['author']['html_url'],
                            followers_url  =commits_url[j]['author']['followers_url'],
                            following_url =commits_url[j]['author']['following_url'],
                            gists_url  =commits_url[j]['author']['gists_url'],
                            starred_url  =commits_url[j]['author']['starred_url'],
                            subscriptions_url  =commits_url[j]['author']['subscriptions_url'],
                            organizations_url  =commits_url[j]['author']['organizations_url'],
                            repos_url  =commits_url[j]['author']['repos_url'],
                            events_url  =commits_url[j]['author']['events_url'],
                            received_events_url  =commits_url[j]['author']['received_events_url'],
                            type  =commits_url[j]['author']['type'],
                            site_admin =commits_url[j]['author']['site_admin']
                        )
                        db_session.add(author)
                        db_session.commit()
                        print(author)
                    else:
                        db_session.add(author)
                        db_session.commit()
                        print(author)
                except KeyError as e:
                    print(str(e))


                try:
                    if commits_url[j]['committer'] is not None:
                        committer= Committer(
                            login =commits_url[j]['committer']['login'],
                            id =commits_url[j]['committer']['id'],
                            node_id  =commits_url[j]['committer']['node_id'],
                            avatar_url  =commits_url[j]['committer']['avatar_url'],
                            gravatar_id  =commits_url[j]['committer']['gravatar_id'],
                            url  =commits_url[j]['committer']['url'],
                            html_url  =commits_url[j]['committer']['html_url'],
                            followers_url  =commits_url[j]['committer']['followers_url'],
                            following_url =commits_url[j]['committer']['following_url'],
                            gists_url  =commits_url[j]['committer']['gists_url'],
                            starred_url  =commits_url[j]['committer']['starred_url'],
                            subscriptions_url  =commits_url[j]['committer']['subscriptions_url'],
                            organizations_url  =commits_url[j]['committer']['organizations_url'],
                            repos_url  =commits_url[j]['committer']['repos_url'],
                            events_url  =commits_url[j]['committer']['events_url'],
                            received_events_url  =commits_url[j]['committer']['received_events_url'],
                            type  =commits_url[j]['committer']['type'],
                            site_admin =commits_url[j]['committer']['site_admin']

                        )
                        db_session.add(committer)
                        db_session.commit()
                        print(committer)    
                    else:
                        db_session.add(committer)
                        db_session.commit()
                        print(committer) 


                except KeyError as e:
                    print(str(e))

                main=Main(
                    sha=commits_url[j]['sha'],
                    node_id=commits_url[j]['node_id'],
                    url=commits_url[j]['url'],
                    html_url=commits_url[j]['html_url'],
                    comments_url=commits_url[j]['comments_url'],
                    parents_id=parents.id,
                    commit_id=commit.id,
                    commit_author_id=commit_author.id,
                    commit_committer_id=commit_committer.id,
                    commit_tree_id=commit_tree.id,
                    commit_verification_id=commit_verification.id,
                    author_id1=author.author_id,
                    committer_id1=committer.committer_id    
                )
                db_session.add(main)
                db_session.commit()
                print(main)
                


        print(count)    

    except requests.exceptions.HTTPError as err:
        print("Connection error"+str(err))    
