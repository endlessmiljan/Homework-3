import json
data = [{
        "country": "GB",
        "spent": 100
    },
    {
        "country": "RU",
        "spent": 200
    }]
dictdata = {}
for x in data:
   dictdata.update({x["country"]: x["spent"]})
print(dictdata)