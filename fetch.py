import urllib, json

search_item_base_url = "https://pdbj.org/rest/newweb/search/pdb"
params = "rdate_after=2014-01-01&method=1&res_max=1.8&sortBy=8"

search_response = urllib.request.urlopen(search_item_base_url+"?"+params).read()
search_response = json.loads(search_response)

ids = [data["results"][i][0] for i in search_response]

# idsをループして、それぞれのIDに対してfetchを行う
fetch_file_base_url = "https://pdbj.org/rest/newweb/fetch/file"
for i in ids:
  # 一旦10回ループしたら終了する
  break if i == 10
  fetch_file_params = "format=pdb&id="+ids[i]
  fetch_file_response = urllib.request.urlopen(fetch_file_base_url+"?"+fetch_file_params).read()






