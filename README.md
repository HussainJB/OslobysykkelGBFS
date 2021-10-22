# OslobysykkelGBFS
Python application that retrieves Real-Time Data about Oslo City Bicycle based on your location. 
API offered in GBFS format (General Bikeshare Feed Specification) https://github.com/NABSA/gbfs/blob/master/gbfs.md

# Requirements and libraries
- Python -version 3.9.2
- Package json - JSON (JavaScript Object Notation) <http://json.org > is a subset of JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data interchange format.
- Package requests - Requests is an HTTP library, written in Python, for human beings. Full documentation is at <https://requests.readthedocs.io
- Package geopy - geopy is a Python client for several popular geocoding web services.

# Instructions for running application
This is a terminal based application that runs  with command: `py OslobysykkelGBFS.py`

# Use:
1. User is asked to enter location (address or place). Library Nominatim geocoder for OpenStreetMap data is used to locate and return a GPS coordinates. Documentation at: https://nominatim.org/release-docs/develop/api/Overview/
2. User is asked to enter how many meters (circumference) from location do you want to see bicycle stations. This number is used to calculate the geographical distance from the specified location to all bike stations. Only those within the specified radius are returned in a list to the user.
  

# Some run examples
1. Position Stortorvet. Bike station(s) that are less than 100 meters away from the user.
![Skjermskudd alfabetisk](https://github.com/HussainJB/OslobysykkelGBFS/blob/main/Test1.PNG)

2. Position Solli. Bike station(s) that are less than 200 meters away from the user.
![Skjermskudd alfabetisk](https://github.com/HussainJB/OslobysykkelGBFS/blob/main/Test2.PNG)

3. Implemented robust handling of entered data from user for both location/address and number of meters to bike station(s)
![Skjermskudd alfabetisk](https://github.com/HussainJB/OslobysykkelGBFS/blob/main/Test3.PNG)

4. Position Oslo S. Bike station(s) that are less than 500 meters away from the user. Gets hits at 19 bike stations.
![Skjermskudd alfabetisk](https://github.com/HussainJB/OslobysykkelGBFS/blob/main/Test4.PNG)

# Future improvements:
With the limited time (around 3 hours) spent developing, testing and pushing this code, there is potential for future improvements
1. Create a better graphical user interface.
2. Get GPS location from a GPS traceable device so that user does not have to enter location/address.
3. Implement map view with live status
