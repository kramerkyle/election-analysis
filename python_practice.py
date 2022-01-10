# Tuples
# counties_tuple = ("Arapahoe","Denver","Jefferson")
# print(counties_tuple[1])
# print("")

# Dictionaries
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438

# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())
# print(counties_dict.get("Denver"))
# print(counties_dict["Arapahoe"])
# print("")

# voting_data=[]
# voting_data.append({"county":"Arapahoe","registered_voters":422829})
# voting_data.append({"county":"Denver","registered_voters":463353})
# voting_data.append({"county":"Jefferson","registered_voters":432438})
# print(voting_data)

# Decision Statements
# my_votes = float(input("How many votes did you get in the election? "))
# total_votes = float(input("What were the total votes in the election? "))
# percentage_votes = int((my_votes / total_votes) * 100)
# print("I received "+ str(percentage_votes) +"% of the total votes")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties:
    print(county)

