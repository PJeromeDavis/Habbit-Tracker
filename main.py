import requests
import datetime as dt


today = dt.datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "" #please provide your own token here
USERNAME = "" #please provide your own username here
#FOR CREATING A USER
parameters = {"token": TOKEN,"username": USERNAME,"agreeTermsOfService": "yes", "notMinor": "yes"}
response = requests.post(url="https://pixe.la/v1/users", json=parameters)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {"id":"(Provide your graph a graph id)", "name":"(Provide any name for your graph)", "unit":"mins", "type":"int", "color":"kuro", "timezone":"Asia/Tokyo"}
headers = {"X-USER-TOKEN":TOKEN}
#creating Graph
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


#CREATING A PIXEL
graph_create = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1", json={"date":today.strftime("%Y%m%d"), "quantity":"180"}, headers=headers)
print(graph_create.text)

#UPDATING A PIXEL
graph_update = requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}", json={"quantity":"90"}, headers=headers)
print(graph_update.text)


#FOR UPDATING A GRAPH
url_endpoint = f"https://pixe.la/v1/users/<username>/graphs/<graphID>"

#FOR VIEWING THE GRAPH
url_endpoint = "https://pixe.la/v1/users/<username>/graphs/<graphID>.html"  #paste this url in browser with your own username and graph id you provided
