import requests
from model import *
from loadenv import *

owner_id_Unique_list = []
owner_id_duplicate_list = []

def insert_license_values(license):
    if license is not None and license['key']is not None:
        licenses = License(
            
            key = license['key'],
            name = license['name'],
            spdx_id = license['spdx_id'],
            url = license['url'],
            node_id = license['node_id']
        )
        db_session.add (licenses)
        db_session.commit()
        return True
    else:
        licenses=License()
        db_session.add(licenses)
        db_session.commit()
        return False

def insert_owner_values(owner):
    if owner['id'] not in owner_id_Unique_list and not None:
        owner_id_Unique_list.append(owner['id'])
        owners=Owner(
            login=owner['login'],
            id = owner['id'],   
            node_id = owner['node_id'],
            avatar_url =owner['avatar_url'],
            gravatar_id =owner['gravatar_id'],
            url = owner['url'],
            html_url = owner['html_url'],
            followers_url =owner['followers_url'],
            following_url = owner['following_url'],
            gists_url = owner['gists_url'],
            starred_url = owner['starred_url'],
            subscriptions_url = owner['subscriptions_url'],
            organizations_url = owner['organizations_url'],
            repos_url = owner['repos_url'],
            events_url =owner['events_url'],
            received_events_url = owner['received_events_url'],
            type =owner['type'],
            site_admin =owner['site_admin']
        )
        db_session.add(owners)
        db_session.commit()
        return True
    else:
        owner_id_duplicate_list.append(owner['id'])
        db_session.commit()
        return False

def insert_item_values(item,owner):
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
            # license_id = license['id'],
            owner_id = owner['id']
        )
    db_session.add(repository)
    db_session.commit()
    return True




for i in range(1,6):
    URI = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=5&page="+str(i)
    resp = requests.get(URI)
    if resp.status_code == 200:
        db_session = create_session()
        data = resp.json()
        items = data['items']
        for item in items:
            license = item['license']
            insert_license_values(license)
            owner=item['owner']
            insert_owner_values(owner)
            insert_item_values(item,owner)
        

    # owner_id = owner['id']
    # branch=item['branches_url']