## This one below was done by my group member not me
# def most_endangered(species_list):
#     lowest = species_list[0]["population"]
#     nameLowest = species_list[0]["name"]
#     for species in species_list:
#         if lowest > species["population"]:
#             lowest = species["population"]
#             nameLowest = species["name"]
#     return nameLowest

## This one below was done by my group member not me
# def count_endangered_species(endangered_species, observed_species):
   
#     count = 0
#     for species in observed_species:
#         if species in endangered_species:
#             count += 1
#     return count
    

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))




def navigate_research_station(station_layout, observations):
    distance = 0
    location = 0    # starts at index 0
    for letter in observations:
        i = station_layout.index(letter) # location we want to go to
        distance += abs(i - location)
        location = i

    return distance


# station_layout1 = "pqrstuvwxyzabcdefghijklmno"
# observations1 = "wildlife"

# station_layout2 = "abcdefghijklmnopqrstuvwxyz"
# observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))





def prioritize_observations(observed_species, priority_species):
    newList = []
    for species in priority_species:
        for other in observed_species:
            if species == other:
                newList.append(species)

    remaining = [observed for observed in observed_species if observed not in priority_species]
    newList.extend(sorted(remaining))

    return newList



observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 