# Messing with dictionaries
# Author: Fatima Oliveira

car = {
"make"                : "ford",
"model"               : "focus",
"year"                :  2009,
"owner"               : { # dict inside dict makes information easier to read
    "name"                : "Fatima",
    "owner-driver-number" :  386899,
    }
}

attr = "model" # attr is atribute
print(car[attr])
print(car["model"]) # this way is more simple and easy to read than above code
print(car["owner"])
print(car["owner"]["name"])
print ((car["owner"].get("names"))) # will show is there's anything inside names. Will show none because correct form is name
print (type(car["owner"].get("owner-driver-number"))) # will show the type of the dict
