import requests
import json


def fetch_planet_data():
    # find mass and get heaviest planet
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    heaviest_planet = ''
    max_volume = 0

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['name']
            mass = planet['mass']['massValue']
            if mass > max_volume:
                max_volume = mass
                heaviest_planet = name
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    print(f"Heaviest palnet: {heaviest_planet}")

fetch_planet_data()

        




# import requests

# def fetch_planet_data():
#     url = "https://api.le-systeme-solaire.net/rest/bodies/"
#     response = requests.get(url)
#     planets = response.json()['bodies']

#     planet_data = []

#     # Process each planet's info
#     for planet in planets:
#         if planet['isPlanet']:
#             name = planet['englishName']
#             mass = planet['mass']['massValue'] if planet['mass'] else 'Unknown'
#             orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 'Unknown'
#             planet_data.append({
#                 'name': name,
#                 'mass': mass,
#                 'orbit_period': orbit_period
#             })
#             print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

#     return planet_data

# def find_heaviest_planet(planets):
#     heaviest_planet = None
#     max_mass = float('-inf')

#     for planet in planets:
#         if planet['mass'] != 'Unknown' and planet['mass'] > max_mass:
#             max_mass = planet['mass']
#             heaviest_planet = planet

#     return heaviest_planet

# planets = fetch_planet_data()
# heaviest_planet = find_heaviest_planet(planets)

# if heaviest_planet:
#     print(f"The heaviest planet is: {heaviest_planet['name']} with a mass of {heaviest_planet['mass']} kg.")
# else:
#     print("Could not determine the heaviest planet.")
