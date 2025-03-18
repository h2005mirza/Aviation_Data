# creating a program using aviation_stack api to extract flight data

import urllib.request
import urllib.error
import urllib.parse
import json

api_key = "9112a0bb1ced564618fd9d4022aedffb"
base_url = "https://api.aviationstack.com/v1/"

def get_live_flight_data():
    params = {
        "access_key": api_key,

    }
    endpoint = "flights"
    url = f"{base_url}{endpoint}"

    parsed_url = url + '?' + urllib.parse.urlencode(params)

    try:
        response = urllib.request.urlopen(parsed_url)
        data = response.read().decode()
        json_data = json.loads(data)
        return json.dumps(json_data, indent=4)

    except urllib.error.URLError as e:
        print(f"A URL error occurred: {e.reason}")
    except json.JSONDecodeError:
        print("sorry, json data cant be parsed!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print(get_live_flight_data())






