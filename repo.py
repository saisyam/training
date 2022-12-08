import requests
from model2 import *
from db import *
owner_id_Unique_list = []
owner_id_duplicate_list = []

for i in range(1,6):
    URI = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&page="+str(i)

    db_session = create_session()
    resp = requests.get(URI)
    if resp.status_code == 200:
        data = resp.json()
        items = data['items']
        
        def insert_owner(owner):
            if item['owner']['id'] not in owner_id_Unique_list:
                    owner_id_Unique_list.append(item['owner']['id'])
                    if item['owner']['id'] in owner_id_Unique_list:
                        owner=Owner(
                            login=owner['login'],
                            id = owner['id'],   
                            node_id = owner['node_id'],
                            avatar_url =owner['avatar_url'],
                            gravatar_id =owner['gravatar_id'],
                            url = owner['url'],
                            html_url = owner['html_url'],
                            followers_url =owner['followers_url'],
                            gists_url = owner['gists_url'],
                            starred_url = owner['starred_url'],
                            subscriptions_url = owner['subscriptions_url'],
                            events_url =owner['events_url'],
                            received_events_url = owner['received_events_url'],
                            type =owner['type'],
                            site_admin =owner['site_admin']
                        )
                        db_session.add(owner)
                        db_session.commit()
                        print(owner)
            else:
                    owner_id_duplicate_list.append(item['owner']['id'])
                    db_session.commit()

        
        for item in items:
                owner = item['owner']
                
                insert_owner(owner)
                
                try:
                    if item['license'] is not None and item['license']['key']is not None:
                        license = License(
                            key = item['license']['key'],
                            name = item['license']['name'],
                            spdx_id = item['license']['spdx_id'],
                            url = item['license']['url'],
                            node_id = item['license']['node_id'],
                    
                        )
                        db_session.add(license)
                        db_session.commit()
                        print(license)
                    else:
                        license=License()
                        db_session.add(license)
                        db_session.commit()
                except Exception as e:
                        print(str(e))

                repository = Repository(
                    id = item['id'],
                    name = item['name'],
                    node_id = item['node_id'],
                    full_name = item['full_name'],
                    private = item['private'],
                    size = item['size'],
                    owner_id = item['owner']['id'],
                    license_id = license.id

                )
                print(repository)
                db_session.add(repository)
                db_session.commit()

    else:
            print("Failed to get data")