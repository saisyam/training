# import requests
# from model import *
# from loadenv import *
# sha_unique_list=[]
# sha_duplicate_list=[]
# # for i in range(1,2):
# URI = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=10&page=1"

# db_session = create_session()
# resp = requests.get(URI)
# if resp.status_code == 200:
#     data = resp.json()
#     items = data['items']
    
#     for item in items:
#         branches=item['branches_url']
#         print(branches)
#         x=branches[:-9]
#         res=requests.get(x)
#         if resp.status_code == 200:
#             dat=res.json()
#             for branch in range(0,len(dat)):
#                 if dat[branch]['commit']['sha'] not in  sha_unique_list:
#                     sha_unique_list.append(dat[branch]['commit']['sha'])
#                     commit_branch_url=Commit_branch_url(
#                         sha=dat[branch]['commit']['sha'],
#                         url=dat[branch]['commit']['url']
#                     )
#                     db_session.add(commit_branch_url)
#                     db_session.commit()

#                 branch_url=Branch_url(    
#                     name=dat[branch]['name'],
#                     protected=dat[branch]['protected'],
#                     commit_sha=commit_branch_url.sha
#                 )
#                 db_session.add(branch_url)
#                 db_session.commit()
        
                    
   