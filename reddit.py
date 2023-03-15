import requests
import json 
import csv
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'Sea-surround-7383', 'password': 'Pequimbeijing12'}
auth = requests.auth.HTTPBasicAuth('wSdxmrU2CC2Kmqx0Nt7Nug', 'YyUVw0PbyI6ZX7QTyPcIwYJ-F7ebKA')
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth)
d = r.json()

#YyUVw0PbyI6ZX7QTyPcIwYJ-F7ebKA

token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
response = requests.get(base_url + '/api/v1/me', headers=headers)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])

data = []

#response = requests.get(base_url + '/r/portugal/search?q=bpi&restrict_sr=on.json', headers=headers) --> gets all bpi posts

#How to get the link id? Make a request to get all posts, extract the id, save on a list, loop through the list, pass it through the url and get all comments and save them
response = requests.get(base_url + '/r/portugal/comments/5xi8n2', headers=headers)

#/r/subreddit]/comments/Só_para_relembrar:_o_BPI_começou_hoje_a_cobrar_comissões_para_MBWay.json
if response.status_code == 200:
    data = response.json()
    comments = data[1]['data']['children']
    for comment in comments:
        body = comment['data']['body']
        print(body)
else:
    print("Failed to fetch data from the URL")

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for title in data:
            writer.writerow([title])

save_to_csv(data, 'reddit_bpi.csv')