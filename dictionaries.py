#Dictionaries are classes for python with key and values as the object and object property
#Dictionaries are used to store data concerning  single entity or thing
#Dictionaries store related data
Book={ "Title":"The Shining",
        "Author":"Stephen King",
        "Genre":"Psychological Horror",
        "Protagonist":"Jack Torrance"}
print(Book.get("Title"))
JoelHawi={"Name": "Joel",
            "Age":"18",
            "Height":172,
            "Race":"African",
            "Gender":"Male"
            }
#Update function is used to change or add information to the dictionary
Book.update({"Year":1998})
JoelHawi.update({"Name":"Hawi"})
print(Book.get("Year"))
print(JoelHawi.get("Name"))
for x in Book:
    print(Book[x])#used to print the final values of a singular dictionary
Family={"Father":{"Name":"Zeus",
                    "Title":"King of Olympus"},
        "Mother":{"Name":"Hera",
                    "Title":"Queen of Olympus"},
        "Brother":{"Name":"Ares",
                    "Title":"God of war"},
        "Persona":{"Name":"Hephaustus",
                    "Title":"God of the forge"}}
print(Family["Father"]["Title"])

