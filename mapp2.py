import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "UmeMH4iEK6DBdkUdhGfrBB1IjgHCvKLt"

while True:
   orig = input("Starting Location: ")
   dest = input("Destination: ")
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")

