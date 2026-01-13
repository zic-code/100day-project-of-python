import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "jisoo123"
TOKEN = "djsdf3943431"
GRAPH_ID = "graph1"


user_params = {
    "token" :  TOKEN,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url = pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name":"Cycling Graph",
    "unit" : "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response= requests.post(url= graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint= f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"

# today = datetime.now()
today = datetime(year=2026, month=1,day=10).strftime("%Y%m%d")


pixel_data = {
    "date": today,
    "quantity": "8",
}
# print(today.strftime("%Y%m%d"))
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data,headers=headers)
# print(response.text)



before_yesterday= datetime(year=2026, month=1, day=9).strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{before_yesterday}"
pixel_update_data = {
    "quantity": "7",
}

# response = requests.put(url=pixel_update_endpoint, json= pixel_update_data,headers= headers)
# print(response.text)

#DELETE

pixel_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{today}"
response = requests.delete(url= pixel_delete_endpoint, headers= headers)
print(response.text)

