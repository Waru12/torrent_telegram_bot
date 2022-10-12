import requests
import json

def shorten(url):
    linkRequest = {
        "destination": f"{url}"
        , "domain": {
            "id": "",
            "fullName": ""
        }
    }

    requestHeaders = {
        "Content-type": "application/json",
        "apikey": "18821a7effe9461aa79df1a49d7a1b31",
    }

    r = requests.post("https://api.rebrandly.com/v1/links",
                      data=json.dumps(linkRequest),
                      headers=requestHeaders)
    print(r.text)

    if r.status_code == requests.codes.ok:
        link = r.json()
        print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))
        return link["shortUrl"]
    else:
        return url

if __name__ == "__main__":
    shorten("https://google.com")
