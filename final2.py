import psycopg2
import requests
import os
from psycopg2.extensions import AsIs
import json

with open('./config.json', 'r') as f:
    config = json.load(f)
database = config.get('database')
host = config.get('host')
user = config.get('user')
password = config.get('password')
port = config.get('port')
conn = None
cursor = None


owner_id_Unique_list = []
owner_id_duplicate_list = []
license_id_unique_list = []
license_id_duplicate_list = []


for i in range(1,6):
    url = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&page="+str(i)
    responce = requests.get(url)

    try:
        if responce.status_code == 200:
            conn = psycopg2.connect(
                database = database,
                host = host,
                user = user,
                password = password,
                port = port)
            cursor = conn.cursor()
            

        def insert_owner_values(owner):
            if owner is not None and owner['id'] not in owner_id_Unique_list:
                owner_id_Unique_list.append(owner['id'])
                columns = owner.keys()
                values = [owner[column] for column in columns]
                insert_statement = 'insert into owner (%s) values %s ON CONFLICT (id) DO NOTHING'
                cursor.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))   
            else:
                owner_id_duplicate_list.append(owner['id'])
                return None
            conn.commit()

        def insert_license_values(license,owner):
            if license is None and owner['id'] is not None and owner['id'] not in license_id_unique_list:
                license_id_unique_list.append(owner['id'])
                insert_script = 'INSERT INTO license(key, name, spdx_id,url,node_id,id) VALUES(%s,%s,%s,%s,%s,%s)'
                insert_values = (None,None,None,None,None,owner['id'])
                cursor.execute(insert_script,insert_values)
            elif license is not None and owner['id'] is not None and owner['id'] not in license_id_unique_list:
                    license_id_unique_list.append(owner['id'])
                    insert_script = 'INSERT INTO license(key, name, spdx_id,url,node_id,id) VALUES(%s,%s,%s,%s,%s,%s)'
                    insert_values = (license['key'],license['name'],license['spdx_id'],license['url'],license['node_id'],owner['id'])
                    cursor.execute(insert_script,insert_values)
                    cursor.execute('SELECT * FROM license ')
                    cursor.execute('SELECT * FROM owner')
            else:
                license_id_duplicate_list.append(owner['id'])
                return None     
            conn.commit()
        
        def insert_item_values(repos,owner):
            insert_script = 'INSERT INTO item(id,node_id,name,full_name,private,html_url,description,fork,url,forks_url,keys_url,collaborators_url,teams_url,hooks_url,issue_events_url,events_url,assignees_url,branches_url,tags_url,blobs_url,git_tags_url,git_refs_url,trees_url,statuses_url,languages_url,stargazers_url,contributors_url,subscribers_url,subscription_url,commits_url,git_commits_url,comments_url,issue_comment_url,contents_url,compare_url,merges_url,archive_url,downloads_url,issues_url,pulls_url,milestones_url,notifications_url,labels_url,releases_url,deployments_url,created_at,updated_at,pushed_at,git_url,ssh_url,clone_url,svn_url,homepage,size,stargazers_count,watchers_count,language,has_issues,has_projects,has_downloads,has_wiki,has_pages,has_discussions,forks_count,mirror_url,archived,disabled,open_issues_count,allow_forking,is_template,web_commit_signoff_required,topics,visibility,forks,open_issues,watchers,default_branch,score,owner_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)ON CONFLICT (id) DO NOTHING'
            insert_values= (repos['id'],repos['node_id'],repos['name'],repos['full_name'],repos['private'],repos['html_url'],repos['description'],repos['fork'],repos['url'],repos['forks_url'],repos['keys_url'],repos['collaborators_url'],repos['teams_url'],repos['hooks_url'],repos['issue_events_url'],repos['events_url'],repos['assignees_url'],repos['branches_url'],repos['tags_url'],repos['blobs_url'],repos['git_tags_url'],repos['git_refs_url'],repos['trees_url'],repos['statuses_url'],repos['languages_url'],repos['stargazers_url'],repos['contributors_url'],repos['subscribers_url'],repos['subscription_url'],repos['commits_url'],repos['git_commits_url'],repos['comments_url'],repos['issue_comment_url'],repos['contents_url'],repos['compare_url'],repos['merges_url'],repos['archive_url'],repos['downloads_url'],repos['issues_url'],repos['pulls_url'],repos['milestones_url'],repos['notifications_url'],repos['labels_url'],repos['releases_url'],repos['deployments_url'],repos['created_at'],repos['updated_at'],repos['pushed_at'],repos['git_url'],repos['ssh_url'],repos['clone_url'],repos['svn_url'],repos['homepage'],repos['size'],repos['stargazers_count'],repos['watchers_count'],repos['language'],repos['has_issues'],repos['has_projects'],repos['has_downloads'],repos['has_wiki'],repos['has_pages'],repos['has_discussions'],repos['forks_count'],repos['mirror_url'],repos['archived'],repos['disabled'],repos['open_issues_count'],repos['allow_forking'],repos['is_template'],repos['web_commit_signoff_required'],repos['topics'],repos['visibility'],repos['forks'],repos['open_issues'],repos['watchers'],repos['default_branch'],repos['score'],owner['id'])
            cursor.execute(insert_script,insert_values)
            cursor.execute("SELECT * FROM item")
            conn.commit()

        data = responce.json()
        repos = data['items']
        for repo in repos:
            owner = repo['owner']
            license = repo['license']
            owner_id = owner['id']
            insert_owner_values(owner)
            insert_license_values(license,owner)
            insert_item_values(repo,owner)

    except requests.exceptions.ConnectionError:
        print("Connecton Error status_code{}".fornat(responce.status_code))
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close() 






















