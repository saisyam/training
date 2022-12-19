import requests
from model import *
from loadenv import *

from sqlalchemy.sql import select
from top_repos import *
import time
user_id_Unique_list = []
user_id_duplicate_list = []
labels_id_Unique_list=[]
labels_id_duplicate_list =[]
issues_url_id_Unique_list =[]
issues_url_id_duplicate_list =[]



count=0
db_session = create_session()
issues = db_session.execute(select(Repository.issues_url))
for issue in issues:
    issue_n = issue.issues_url[:-9]
    #print(issue_n)
    responce = requests.get(issue_n)
    print(responce)
    
    if responce.status_code == 200:
        issues_url = responce.json()
        
        #print(issues_url)
        for i in range(len(issues_url)):
            if issues_url[i]['reactions'] is not None:
                    reactions = Reactions(
                                url = issues_url[i]['reactions']['url'],
                                total_count = issues_url[i]['reactions']['total_count'],
                                laugh = issues_url[i]['reactions']['laugh'],
                                hooray = issues_url[i]['reactions']['hooray'],
                                confused = issues_url[i]['reactions']['confused'],
                                heart=issues_url[i]['reactions']['heart'],
                                rocket=issues_url[i]['reactions']['rocket'],
                                eyes=issues_url[i]['reactions']['eyes']
                    )
                    db_session.add(reactions)
                    db_session.commit()
                    # print(reactions)
            else:
                reactions = Reactions()
                db_session.add(reactions)
                db_session.commit()
            

            #users
            if issues_url[i]['user']['id'] not in user_id_Unique_list:
                user_id_Unique_list.append(issues_url[i]['user']['id'])
                users=Users( 
                        login =issues_url[i]['user']['login'],
                        id=issues_url[i]['user']['id'],
                        node_id=issues_url[i]['user']['node_id'],
                        avatar_url=issues_url[i]['user']['avatar_url'],
                        gravatar_id=issues_url[i]['user']['gravatar_id'],
                        url=issues_url[i]['user']['url'],
                        html_url=issues_url[i]['user']['html_url'],
                        followers_url=issues_url[i]['user']['followers_url'],
                        following_url=issues_url[i]['user']['following_url'],
                        gists_url=issues_url[i]['user']['gists_url'],
                        starred_url=issues_url[i]['user']['starred_url'],
                        subscriptions_url=issues_url[i]['user']['subscriptions_url'],
                        organizations_url=issues_url[i]['user']['organizations_url'],
                        repos_url=issues_url[i]['user']['repos_url'],
                        events_url=issues_url[i]['user']['events_url'],
                        received_events_url=issues_url[i]['user']['received_events_url'],
                        type=issues_url[i]['user']['type'],
                        site_admin=issues_url[i]['user']['site_admin']
                )
                # print(users)
                db_session.add(users)
                db_session.commit()
            else:
              user_id_duplicate_list.append(issues_url[i]['user']['id'])
              db_session.commit()



            #assignee
            if issues_url[i]['assignee'] and not None:
                
                    assignee=Assignee( 
                            login =issues_url[i]['assignee']['login'],
                            assignee_id=issues_url[i]['assignee']['id'],
                            node_id=issues_url[i]['assignee']['node_id'],
                            avatar_url=issues_url[i]['assignee']['avatar_url'],
                            gravatar_id=issues_url[i]['assignee']['gravatar_id'],
                            url=issues_url[i]['assignee']['url'],
                            html_url=issues_url[i]['assignee']['html_url'],
                            followers_url=issues_url[i]['assignee']['followers_url'],
                            following_url=issues_url[i]['assignee']['following_url'],
                            gists_url=issues_url[i]['assignee']['gists_url'],
                            starred_url=issues_url[i]['assignee']['starred_url'],
                            subscriptions_url=issues_url[i]['assignee']['subscriptions_url'],
                            organizations_url=issues_url[i]['assignee']['organizations_url'],
                            repos_url=issues_url[i]['assignee']['repos_url'],
                            events_url=issues_url[i]['assignee']['events_url'],
                            received_events_url=issues_url[i]['assignee']['received_events_url'],
                            type=issues_url[i]['assignee']['type'],
                            site_admin=issues_url[i]['assignee']['site_admin']
                    )
                    # print(assignee)
                    db_session.add(assignee)
                    db_session.commit()
            else:
                    
                    assignee=Assignee()
                    db_session.add(assignee)
                    db_session.commit()


            #assignees
            if issues_url[i]['assignees'] and not None:
                for m in range(len(issues_url[i]['assignees'])):
                    assignees=Assignees( 
                            login =issues_url[i]['assignees'][m]['login'],
                            assignees_id=issues_url[i]['assignees'][m]['id'],
                            node_id=issues_url[i]['assignees'][m]['node_id'],
                            avatar_url=issues_url[i]['assignees'][m]['avatar_url'],
                            gravatar_id=issues_url[i]['assignees'][m]['gravatar_id'],
                            url=issues_url[i]['assignees'][m]['url'],
                            html_url=issues_url[i]['assignees'][m]['html_url'],
                            followers_url=issues_url[i]['assignees'][m]['followers_url'],
                            following_url=issues_url[i]['assignees'][m]['following_url'],
                            gists_url=issues_url[i]['assignees'][m]['gists_url'],
                            starred_url=issues_url[i]['assignees'][m]['starred_url'],
                            subscriptions_url=issues_url[i]['assignees'][m]['subscriptions_url'],
                            organizations_url=issues_url[i]['assignees'][m]['organizations_url'],
                            repos_url=issues_url[i]['assignees'][m]['repos_url'],
                            events_url=issues_url[i]['assignees'][m]['events_url'],
                            received_events_url=issues_url[i]['assignees'][m]['received_events_url'],
                            type=issues_url[i]['assignees'][m]['type'],
                            site_admin=issues_url[i]['assignees'][m]['site_admin']
                    )
                    # print(assignees)
                    db_session.add(assignees)
                    db_session.commit()
            else:
                    
                    assignees=Assignees()
                    db_session.add(assignees)
                    db_session.commit()
            


            #labels
            for j in range(len(issues_url[i]['labels'])):
                if issues_url[i]['labels'][j]['id'] not in labels_id_Unique_list:
                    labels_id_Unique_list.append(issues_url[i]['labels'][j]['id'])
                    labels = Labels(
                            id = issues_url[i]['labels'][j]['id'],
                            node_id = issues_url[i]['labels'][j]['node_id'],
                            url = issues_url[i]['labels'][j]['url'],
                            name = issues_url[i]['labels'][j]['name'],
                            color = issues_url[i]['labels'][j]['color'],
                            defult=issues_url[i]['labels'][j]['default'],
                            description=issues_url[i]['labels'][j]['description']
                    )
                    db_session.add(labels)
                    db_session.commit()
                    # print(labels)
                else:
                    labels_id_duplicate_list.append(issues_url[i]['labels'][j]['id'])
                    db_session.commit()
            
            #issues_url
            for k in range(len(issues_url[i]['labels'])):
                if issues_url[i]['id'] not in issues_url_id_Unique_list:
                    issues_url_id_Unique_list.append(issues_url[i]['id'])
                    issue_url=Issue_url(
                        id =issues_url[i]['id'],
                        url = issues_url[i]['url'],
                        repository_url =issues_url[i]['repository_url'],
                        labels_url =issues_url[i]['labels_url'],
                        comments_url =issues_url[i]['comments_url'],
                        events_url =issues_url[i]['events_url'],
                        html_url =issues_url[i]['html_url'],
                        node_id = issues_url[i]['node_id'],
                        number=issues_url[i]['number'],
                        title = issues_url[i]['title'],
                        state=issues_url[i]['state'],
                        locked=issues_url[i]['locked'],
                        # milestone=issues_url[i]['milestone'],
                        comments=issues_url[i]['comments'],
                        created_at=issues_url[i]['created_at'],
                        updated_at=issues_url[i]['updated_at'],
                        closed_at=issues_url[i]['closed_at'],
                        author_association=issues_url[i]['author_association'],
                        active_lock_reason=issues_url[i]['active_lock_reason'],
                        body=issues_url[i]['body'],
                        timeline_url=issues_url[i]['timeline_url'],
                        performed_via_github_app=issues_url[i]['performed_via_github_app'],
                        state_reason=issues_url[i]['state_reason'],
                        user_id =issues_url[i]['user']['id'],
                        reactions_id=reactions.id,
                        assignee_id = assignee.id,
                        assignees_id=assignees.id,
                        labels_id = issues_url[i]['labels'][k]['id']
                        
                    )
                    # print(issue_url)
                    db_session.add(issue_url)
                    db_session.commit()
                   
                else:
                    issues_url_id_duplicate_list.append(issues_url[i]['id'])
                    db_session.commit()
        count=count+1
        print(count)
        
    # else:
    #     db_session.refresh(issues)
    












     
        