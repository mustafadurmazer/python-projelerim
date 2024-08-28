import requests

get_url = f"https://jsonplaceholder.typicode.com/todos/10"

get_response = requests.get(get_url)
print(get_response.json())

#put
to_do_item_15 = {'userId': 2,'title':'put title', 'completed': False}
put_response = requests.put(get_url,json=to_do_item_15)
print(put_response.json())

#patch çok kullanılmaz
to_do_item_patch_15 = {"title" : "Patch Test"}
pathc_response = requests.patch(get_url,json=to_do_item_patch_15)
print(pathc_response.json())

#delete

delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)