import json
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def printStationList(UserGPSPosition, MaxDistFromUser):
    station_information = requests.get('https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json',
                                       headers={'Client-Identifier': 'HussainButt-Tester'})
    station_status = requests.get('https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json',
                                  headers={'Client-Identifier': 'HussainButt-Tester'})
    json_station_information = json.loads(station_information.text)
    json_station_status = json.loads(station_status.text)

    numberFound = 0
    for counter in range(0, len(json_station_information['data']['stations'])):
        stationPosition = (str(json_station_information['data']['stations'][counter]['lat']) + "," + str(
            json_station_information['data']['stations'][counter]['lon']))
        if int(geodesic(stationPosition, UserGPSPosition).meters) < int(MaxDistFromUser):
            numberFound = numberFound + 1

    print("Found " + str(numberFound) + " bike station (s) that are under " + str(MaxDistFromUser) + " meters from you.")
    if numberFound == 0:
        OslobysykkelGBFS()
    okContinue = input("Do you want to print the entire list of bike station (s) and status? (Y/N)\n")
    if okContinue == "Y" or okContinue == "y":
        for counter in range(0, len(json_station_information['data']['stations'])):
            stationPosition = (str(json_station_information['data']['stations'][counter]['lat']) + "," + str(
                json_station_information['data']['stations'][counter]['lon']))
            if int(geodesic(stationPosition, UserGPSPosition).meters) < int(MaxDistFromUser):
                numberFound = numberFound + 1
                print(" ")
                print("Stand name: " + json_station_information['data']['stations'][counter]['name'])
                print("Address: " + json_station_information['data']['stations'][counter]['address'])
                print("Distance from you: " + str(
                    round(((geodesic(stationPosition, UserGPSPosition).meters)), 2)) + " meters")
                print("Number of locks available: " + str(
                    json_station_status['data']['stations'][counter]['num_docks_available']))
                print(
                    "Number of available bicycles: " + str(
                        json_station_status['data']['stations'][counter]['num_bikes_available']))
    else:
        OslobysykkelGBFS()


def OslobysykkelGBFS():
    while True:
        print("\n#########################################################################")
        print("Oslo Bysykkel - shows locations and status of bike stations near you!")
        print("#########################################################################")

        UserGivenPosition = input("- Please enter your location (address or place): \n")
        geolocator = Nominatim(user_agent="TestOslobysykkel")
        location = geolocator.geocode(UserGivenPosition + " Oslo ")

        if location == None:
            print("Found no address that matched what you wrote! Please try again!")
            OslobysykkelGBFS()

        MaxDistFromUser = input("- How many meters (circumference) from " + location.address +" do you want to see bicycle stations: \n")

        try:
            int(MaxDistFromUser)
        except ValueError:
            try:
                float(MaxDistFromUser)
            except ValueError:
                print("Wrong number! Please try again!")
                OslobysykkelGBFS()

        UserGPSPosition = (location.latitude, location.longitude)
        print("\nFound the following address: " + location.address)
        print("With GPS coordinates:" + str(UserGPSPosition))
        print("You want to see a list of bike racks within a radius of " + MaxDistFromUser + " meters.")

        okContinue = input("\n- Does this look right?(Y/N)\n")

        if okContinue == "Y" or okContinue == "y":
            printStationList(UserGPSPosition, MaxDistFromUser)
        else:
            OslobysykkelGBFS()


OslobysykkelGBFS()
