import requests
from model import *
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
                #print(license)
            else:
                license=License()
                db_session.add(license)
                db_session.commit()
            
            if item['owner']['id'] not in owner_id_Unique_list:
                owner_id_Unique_list.append(item['owner']['id'])
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
                #print(owner)
            else:
                owner_id_duplicate_list.append(item['owner']['id'])
                db_session.commit()



        
            repository = Repository(
                id = item['id'],
                node_id = item['node_id'],
                name = item['name'],
                full_name = item['full_name'],
                private = item['private'],
                html_url = item['html_url'],
                description = item['description'],
                fork = item['fork'],
                url = item['url'],
                forks_url = item['forks_url'],
                keys_url = item['keys_url'],
                collaborators_url = item['collaborators_url'],
                teams_url = item['teams_url'],
                hooks_url = item['hooks_url'],
                issue_events_url = item['issue_events_url'],
                events_url = item['events_url'],
                assignees_url = item['assignees_url'],
                branches_url = item['branches_url'],
                tags_url = item['tags_url'],
                blobs_url = item['blobs_url'],
                git_tags_url = item['git_tags_url'],
                git_refs_url = item['git_refs_url'],
                trees_url = item['trees_url'],
                statuses_url = item['statuses_url'],
                languages_url = item['languages_url'],
                stargazers_url = item['stargazers_url'],
                contributors_url = item['contributors_url'],
                subscribers_url = item['subscribers_url'],
                subscription_url = item['subscription_url'],
                commits_url = item['commits_url'],
                git_commits_url = item['git_commits_url'],
                comments_url = item['comments_url'],
                issue_comment_url = item['issue_comment_url'],
                contents_url = item['contents_url'],
                compare_url = item['compare_url'],
                merges_url = item['merges_url'],
                archive_url = item['archive_url'],
                downloads_url = item['downloads_url'],
                issues_url = item['issues_url'],
                pulls_url = item['pulls_url'],
                milestones_url = item['milestones_url'],
                notifications_url = item['notifications_url'],
                labels_url = item['labels_url'],
                releases_url = item['releases_url'],
                deployments_url = item['deployments_url'],
                created_at = item['created_at'],
                updated_at = item['updated_at'],
                pushed_at = item['pushed_at'],
                git_url = item['git_url'],
                ssh_url = item['ssh_url'],
                clone_url = item['clone_url'],
                svn_url = item['svn_url'],
                homepage = item['homepage'],
                size = item['size'],
                stargazers_count = item['stargazers_count'],
                watchers_count = item['watchers_count'],
                language = item['language'],
                has_issues = item['has_issues'],
                has_projects = item['has_projects'],
                has_downloads = item['has_downloads'],
                has_wiki = item['has_wiki'],
                has_discussions = item['has_discussions'],
                forks_count = item['forks_count'],
                mirror_url = item['mirror_url'],
                archived = item['archived'],
                disabled = item['disabled'],
                open_issues_count = item['open_issues_count'],
                allow_forking = item['allow_forking'],
                is_template = item['is_template'],
                web_commit_signoff_required = item['web_commit_signoff_required'],
                topics = item['topics'],
                visibility = item['visibility'],
                forks = item['forks'],
                open_issues = item['open_issues'],
                watchers = item['watchers'],
                default_branch = item['default_branch'],
                score = item['score'],
                license_id = license.id,
                owner_id = owner.id
            )

            db_session.add(repository)
            db_session.commit()
            #print(repository)
    # else:
    #     print("Failed to get data")
