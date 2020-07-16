import os
import requests
import urllib.request
from urllib import parse 

print("Welcome to IsIsDown.py!")
print("Please write a URL or URLs you want to check. (seperated by comma)")

input_url = input()
final_list = []
i=0
#print(input_url)
url_list = input_url.split(",")
final_list.append(url_list[0].replace(" ",""))
final_list.append(url_list[1].replace(" ",""))

print(final_list[0])
print(final_list[1])

#URl 1#
stat0 = requests.get(final_list[0])
if( stat0.status_code == requests.codes.ok):
  print(final_list[0] +" is up")
else:
  print("That is Not vaild URL")


#URl 2#
stat1 = requests.get(final_list[1])
if( stat1.status_code == requests.codes.ok):
  print(final_list[1] +" is up")
else:
  print("That is Not vaild URL")


print("Do you want to start over? y/n")
answer = input()
if( answer == "y"):
  print("done, okay! ")
else:
  print("Please go ! ")



#print("")

#print("commit debug")