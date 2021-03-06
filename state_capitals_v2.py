import random

capitals_dict={
    "Washington":"Olympia","Oregon":"Salem",
    "California":"Sacramento","Ohio":"Columbus",
    "Nebraska":"Lincoln","Colorado":"Denver",
    "Michigan":"Lansing","Massachusetts":"Boston",
    "Florida":"Tallahassee","Texas":"Austin",
    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",
    "Alaska":"Juneau","Utah":"Salt Lake City",
    "New Mexico":"Santa Fe","North Dakota":"Bismarck",
    "South Dakota":"Pierre","West Virginia":"Charleston",
    "Virginia":"Richmond","New Jersey":"Trenton",
    "Minnesota":"Saint Paul","Illinois":"Springfield",
    "Indiana":"Indianapolis","Kentucky":"Frankfort",
    "Tennessee":"Nashville","Georgia":"Atlanta",
    "Alabama":"Montgomery","Mississippi":"Jackson",
    "North Carolina":"Raleigh","South Carolina":"Columbia",
    "Maine":"Augusta","Vermont":"Montpelier",
    "New Hampshire":"Concord","Connecticut":"Hartford",
    "Rhode Island":"Providence","Wyoming":"Cheyenne",
    "Montana":"Helena","Kansas":"Topeka",
    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",
    "Maryland":"Annapolis","Missouri":"Jefferson City",
    "Arizona":"Phoenix","Nevada":"Carson City",
    "New York":"Albany","Wisconsin":"Madison",
    "Delaware":"Dover","Idaho":"Boise",
    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"
    }

states = list(capitals_dict.keys())
while True:
    state = random.choice(states)
    capital = capitals_dict[state]
    capital_guess = input("What is the capital of " + state + "? ")

    if capital_guess == "quit":
        break

    if capital_guess == capital:
        print("Correct! Nice job.")
    else:
        print("Incorrect. The capital of " + state + " is " + capital + ".")
print ("All done")

