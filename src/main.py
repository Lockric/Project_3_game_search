import requests
from heapsort import HeapSort
from mergesort import MergeSort
from igdb.wrapper import IGDBWrapper


ClientID = 'vmqipli3y2vhqnenur94vvzdk8eqhs'
ClientSecret = 'gphrec7hscngppx4heaoiukjsnkclc'
r = requests.post(f'https://id.twitch.tv/oauth2/token?client_id={ClientID}&client_secret={ClientSecret}&grant_type=client_credentials')

json_reponse = r.json()
access_token = json_reponse['access_token']
# print(access_token)
wrapper = IGDBWrapper(ClientID, access_token)
