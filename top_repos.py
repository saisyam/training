import requests
from model import *
from loadenv import *
owner_id_Unique_list = []
owner_id_duplicate_list = []

for i in range(1,6):
    URI = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&page="+str(i)
    
    db_session = create_session()
    resp = requests.get(URI)
    if resp.status_code == 200:
        data = resp.json()
        items = data['items']
        for item in items:
            if item['license'] is not None and item['license']['key']is not None:
                license = License(
                    key = item['license']['key'],
                    name = item['license']['name'],
                    spdx_id = item['license']['spdx_id'],
                    url = item['license']['url'],
                    node_id = item['license']['node_id']
                )
                db_session.add(license)
                db_session.commit()
                # print(license)
            else:
                license=License()
                db_session.add(license)
                db_session.commit()
            if item['owner']['id'] not in owner_id_Unique_list:
                owner_id_Unique_list.append(item['owner']['id'])
                if item['owner']['id'] in owner_id_Unique_list and not None:
                    owner=Owner(
                        login=item['owner']['login'],
                        id = item['owner']['id'],   
                        node_id = item['owner']['node_id'],
                        avatar_url =item['owner']['avatar_url'],
                        gravatar_id =item['owner']['gravatar_id'],
                        url = item['owner']['url'],
                        html_url = item['owner']['html_url'],
                        followers_url =item['owner']['followers_url'],
                        following_url = item['owner']['following_url'],
                        gists_url = item['owner']['gists_url'],
                        starred_url = item['owner']['starred_url'],
                        subscriptions_url = item['owner']['subscriptions_url'],
                        organizations_url = item['owner']['organizations_url'],
                        repos_url = item['owner']['repos_url'],
                        events_url =item['owner']['events_url'],
                        received_events_url = item['owner']['received_events_url'],
                        type =item['owner']['type'],
                        site_admin =item['owner']['site_admin']
                    )
                    db_session.add(owner)
                    db_session.commit()
                    # print(owner)
             
            else:
                owner_id_duplicate_list.append(item['owner']['id'])
                db_session.commit()

            
            repository = Repository(
                id = item['id'],
                name = item['name'],
                node_id = item['node_id'],
                full_name = item['full_name'],
                private = item['private'],
                size = item['size'],
                license_id = license.id,
                owner_id=owner.id
            )
            # print(repository)
            db_session.add(repository)
            db_session.commit()
           
          
    else:
        print("Failed to get data")
