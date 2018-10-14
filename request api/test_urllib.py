
import urllib, json
import urllib.request

url = "http://data.fixer.io/api/latest?access_key=c920f7e22e7695ac1784745f7613fecb"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

for rate in data["rates"]:
    print(rate + ": " + str(data["rates"][rate]))

##Go to fixer.io to create your own key##
# https://www.geeksforgeeks.org/get-post-requests-using-python/
