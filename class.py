import psycopg2
import json
import requests
with open('./.env', 'r') as f:
    config = json.load(f)
database = config.get('database')
host = config.get('host')
user = config.get('user')
password = config.get('password')
port = config.get('port')
class Main:
    def insert_main(self,main):
        self.main = main
        if self.main is None:
            self.insert_qu= "insert into main(id,sha,node_id,url,html_url,comments_url,parents)values(%s,%s,%s,%s,%s,%s,%s)"
            self.insert_va= (None,None,None,None,None,None,None)
            cursor.execute(self.insert_qu,self.insert_va)
        else:
            cursor.execute("insert into main(id,shaa,node_id,url,html_url,comments_url,parents)values(%s,%s,%s,%s,%s,%s,%s)",(main['id'],main['sha'],main['node_id'],main['url'],main['html_url'],main['comments_url'],main['parents']))
            cursor.execute("select * from main")
            self.result = cursor.fetchall()
            for row in self.result:
                print(row[0],row[1],row[2],row[3],row[4],row[5])
    def insert_license(self,license):
        self.license = license
        if self.license is None :
            self.insert_qu= "insert into license(key,name,spdx_id,url,node_id)values(%s,%s,%s,%s,%s)"
            self.insert_va= (None,None,None,None,None)
            cursor.execute(self.insert_qu,self.insert_va)
        else:
            cursor.execute("insert into license(key,name,spdx_id,url,node_id) values(%s,%s,%s,%s,%s)",(license['key'],license['name'],license['spdx_id'],license['url'],license['node_id']))
            cursor.execute("select * from license")
            self.result = cursor.fetchall()
            for row in self.result:
                print(row[0],row[1],row[2],row[3],row[4],row[5])
                conn.commit()
    def insert_owner(self,owner):
        self.owner = owner
        cursor = conn.cursor()
        cursor.execute("insert into owner(login,owner_id,node_id,avatar_url,gravatar_id,url,html_url,followers_url,following_url,gists_url,starred_url,subscriptions_url,organizations_url,repos_url,events_url,received_events_url,type,site_admin) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(owner['login'],owner['id'],owner['node_id'],owner['avatar_url'],owner['gravatar_id'],owner['url'],owner['html_url'],owner['followers_url'],owner['following_url'],owner['gists_url'],owner['starred_url'],owner['subscriptions_url'],owner['organizations_url'],owner['repos_url'],owner['events_url'],owner['received_events_url'],owner['type'],owner['site_admin']))
        cursor.execute("select * from owner")
        self.result = cursor.fetchall()
        print(self.result)
        conn.commit()  
    def insert_repo(self,repos):
        self.repos = repos
        cursor = conn.cursor()
        cursor.execute("insert into repository(id,node_id,name,full_name,private,html_url,description,fork,url,forks_url,keys_url,collaborators_url,teams_url,hooks_url,issue_events_url,events_url,assignees_url,branches_url,tags_url,blobs_url,git_tags_url,git_refs_url,trees_url,statuses_url,languages_url,stargazers_url,contributors_url,subscribers_url,subscription_url,commits_url,git_commits_url,comments_url,issue_comment_url,contents_url,compare_url,merges_url,archive_url,downloads_url,issues_url,pulls_url,milestones_url,notifications_url,labels_url,releases_url,deployments_url,created_at,updated_at,pushed_at,git_url,ssh_url,clone_url,svn_url,homepage,size,stargazers_count,watchers_count,language,has_issues,has_projects,has_downloads,has_wiki,has_pages,has_discussions,forks_count,mirror_url,archived,disabled,open_issues_count,allow_forking,is_template,web_commit_signoff_required,topics,visibility,forks,open_issues,watchers,default_branch,score) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(repos['id'],repos['node_id'],repos['name'],repos['full_name'],repos['private'],repos['html_url'],repos['description'],repos['fork'],repos['url'],repos['forks_url'],repos['keys_url'],repos['collaborators_url'],repos['teams_url'],repos['hooks_url'],repos['issue_events_url'],repos['events_url'],repos['assignees_url'],repos['branches_url'],repos['tags_url'],repos['blobs_url'],repos['git_tags_url'],repos['git_refs_url'],repos['trees_url'],repos['statuses_url'],repos['languages_url'],repos['stargazers_url'],repos['contributors_url'],repos['subscribers_url'],repos['subscription_url'],repos['commits_url'],repos['git_commits_url'],repos['comments_url'],repos['issue_comment_url'],repos['contents_url'],repos['compare_url'],repos['merges_url'],repos['archive_url'],repos['downloads_url'],repos['issues_url'],repos['pulls_url'],repos['milestones_url'],repos['notifications_url'],repos['labels_url'],repos['releases_url'],repos['deployments_url'],repos['created_at'],repos['updated_at'],repos['pushed_at'],repos['git_url'],repos['ssh_url'],repos['clone_url'],repos['svn_url'],repos['homepage'],repos['size'],repos['stargazers_count'],repos['watchers_count'],repos['language'],repos['has_issues'],repos['has_projects'],repos['has_downloads'],repos['has_wiki'],repos['has_pages'],repos['has_discussions'],repos['forks_count'],repos['mirror_url'],repos['archived'],repos['disabled'],repos['open_issues_count'],repos['allow_forking'],repos['is_template'],repos['web_commit_signoff_required'],repos['topics'],repos['visibility'],repos['forks'],repos['open_issues'],repos['watchers'],repos['default_branch'],repos['score']))
        cursor.execute("select * from repository")
        self.result = cursor.fetchall()
        print(self.result)
        conn.commit()
        #conn.close()
obj  = Main()
#page=(input("enter page num:"))
for i in range(1,6):
    url = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&'page='"+str(i)
    responce = requests.get(url)
    if responce.status_code == 200:
        conn = psycopg2.connect(
        database = database,
        host = host,
        user = user,
        password = password,
        port = port)
    cursor = conn.cursor()
    print("connection Successful")
    data = responce.json()
    repos = data['items']
    for repo in repos:
        license = repo['license']
        owner = repo['owner']  
        obj.insert_license(license)
        obj.insert_owner(owner)
        obj.insert_repo(repo)