planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
del planet_list[8]
print(planet_list)
print(rocky_planets)

spacecraft = [("Cassini", "Saturn", "Earth", "Venus", "Jupiter"), ("Voyager I", "Saturn", "Jupiter"), ("Mariner 4", "Mars"), ("Pioneer 10", "Jupiter")]

for planet in planet_list:
    planet_spacecraft = set()
    for craft in spacecraft:
        if planet in craft:
            planet_spacecraft.add(craft[0]) 
    joined_list = (', ').join(planet_spacecraft)
    print(f'{planet}: {joined_list}')

