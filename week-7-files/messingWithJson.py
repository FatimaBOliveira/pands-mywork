# Messing with Json
# Program that loads info from JSON files
# Auhtor: Fatima Oliveira

import json

electricBill = {
    'name' : 'Andrew',
    'amount' : '99999'
}

with open("storeData.json", "w") as f:
    json.dump(electricBill, f) # writes the dictionary object to the file as a JSON object