# parsing the extracted JSON data (for flights)

import urllib.request
import urllib.error
import urllib.parse
import json

api_key = "9112a0bb1ced564618fd9d4022aedffb"
base_url = "https://api.aviationstack.com/v1/"

def fetch_live_flight_data(flight_icao):
    params = {
        "access_key":api_key,
        "flight_icao":flight_icao
    } # defining the parameters required by the API (according to the documentation)

    endpoint = "flights"
    url = f"{base_url}{endpoint}" # creating the url link for connection and request

    parsed_url = url + '?' + urllib.parse.urlencode(params)

    try:
        response = urllib.request.urlopen(parsed_url)
        data = response.read().decode()
        json_data = json.loads(data)

        # parsing the JSON attributes found in the response with proper optimized sequence.
        if "data" in json_data and len(json_data["data"]) > 0:
            flight = json_data["data"][0]

            flight_number = flight.get("flight", {}).get("iata", "Flight number not found!")
            airline = flight.get("airline", {}).get("name", "Airline not found!")
            departure_airport = flight.get("departure", {}).get("airport", "Departure airport not found!")
            departure_timezone = flight.get("departure", {}).get("timezone", "Timezone not found!")
            departure_gate_no = flight.get("departure", {}).get("gate", "Gate number not found!")
            departure_time = flight.get("departure", {}).get("estimated", "Departure time not found!")
            arrival_airport = flight.get("arrival", {}).get("airport", "Arrival airport not found!")
            arrival_timezone = flight.get("arrival", {}).get("timezone", "Timezone not found!")
            arrival_time  = flight.get("arrival", {}).get("estimated", "Arrival time not found!")
            flight_date = flight.get("flight_date", "Flight date not found!")
            flight_status = flight.get("flight_status", "Flight status not found!")

            print("----WELCOME TO THE WORLD LIVE FLIGHT DATA----")
            print(f"FLIGHT NUMBER: {flight_number}")
            print(f"AIRLINE: {airline}")
            print(f"DEPARTURE AIRPORT: {departure_airport}")
            print(f"DEPARTING COUNTRY TIMEZONE: {departure_timezone}")
            print(f"DEPARTING GATE NUMBER: {departure_gate_no}")
            print(f"DEPARTURE TIME: {departure_time}")
            print(f"ARRIVAL AIRPORT: {arrival_airport}")
            print(f"ARRIVAL COUNTRY TIMEZONE: {arrival_timezone}")
            print(f"ARRIVAL TIME: {arrival_time}")
            print(f"FLIGHT DATE: {flight_date}")
            print(f"FLIGHT STATUS: {flight_status}")

        else:
            print("Sorry! No data or response was found!")

    except urllib.error.URLError as e:
        print(f"A URL error occurred: {e.reason}")
    except json.JSONDecodeError:
        print("JSON data cant be parsed!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


flight_icao = input("Enter the flight ICAO code:").strip().upper()
fetch_live_flight_data(flight_icao)

# ICAO (International Civil Aviation Organization) assigns ICAO codes to arilines such ETD734, airports
# just like the IATA (International Air Transport Association)





