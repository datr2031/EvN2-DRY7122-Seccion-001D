import urllib.parse
import requests
main_api = "https://www.mapquest.com/directions/from/cl/rm/9200000/to/ar/mz/mendoza”
orig = "Cerrillos, RM"
dest = "Mendoza, MZ"
key = "UmeMH4iEK6DBdkUdhGfrBB1IjgHCvKLt"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
