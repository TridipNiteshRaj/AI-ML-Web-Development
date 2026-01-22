#1- import the random mudule
import random

#2- create subjects
subject =[
    "sharukh khan",
    "virat kohli",
    "Nirmala Sitaraman",
    "A mumbai cat",
    "A group of monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi",
]

actions =[
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "cenlebrates",
]

places_or_things =[
    "at Red fort",
    "in mumbai local train",
    "a plote of samosa",
    "inside perliament",
    "at ganga ghat",
    "during IPL Match",
    "at India gate",
    "smart city of bihar patna",
]

def generate():
        subject1 = random.choice(subject)
        actions1 = random.choice(actions)
        places_or_things1 = random.choice(places_or_things)

        headline = f" BREACKING NEWS: {subject1} {actions1} {places_or_things1}"
        print("\n" + headline) 


#3- start the headlline generation loop
generate()

while True:
    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "yes": 
        generate()
    elif user_input == 'no':
         print("\nThanks for using the fake News Headline Generator.Have a fun day") 
         break
    else:
         print("Invalid input")

