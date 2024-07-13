cart = {
    "Apples" : 30, 
    "Pears" : 21, 
    "Oranges" : 30, 
    "Mangoes" : 40, 
    "Berries" : 20, 
    "Oranges" : 60
    }

#get the respective key value outupt

print(cart.get("Apples"))

print("cart[apples]",cart["Apples"])

#get only keys
print(cart.keys())

#get only values
print(cart.values())

#get key & value pair - items
x=(cart.items())

#add new key into dictionary
cart["Fruits_Owner"] = "Rakesh"
print(cart) #Now final output of cart

#modify the exist key, value
cart["Apples"] = 50
print(cart)

cart.update({"Apples": 75})
print("Dictionary Update:", cart)

#check if the required key exists
if "Apples" in cart:
    print("Key Exist")

#remove respective key and its value
cart.pop("Fruits_Owner")
print(cart)

#removes the last inserted item in dictionary "cart"
cart.popitem()
print("After removed last item:", cart) 

# use "del" keyword removes the item with specified key
del cart["Apples"]
print("After deleted:", cart)

#using for loops

for x in cart:
    print(x) #this prints only keys in a dictionary

for x in cart.keys():
    print(x) #this prints only keys in a dictionary

#get values or itmes
for x in cart:
    print(cart[x]) #this prints only values

for x in cart.values():
    print(x) #this prints only values

for x,y in cart.items():
    print("Key:", x, "Value:", y) #this prints keys & values

#Nested dictinoary and adding a new Key & Value
myfamily = {
  "child1" : {"name" : "Emil","year" : 2004 },
  "child2" : {"name" : "Tobias","year" : 2007},
  "child3" : {"name" : "Linus","year" : 2011}
}
details = {"name" : "new_girl", "year" : 2024}

x=myfamily["child4"]=details

print(myfamily)

#Dictionary will call other dictionary & values
child1 = {"name" : "Emil", "year" : 2004}
child2 = {"name" : "Tobias", "year" : 2007}
child3 = {"name" : "Linus","year" : 2011}

myfamily1 = {"key1" : child1,"key2" : child2,"key3" : child3}


myfamily = {"key1":{"name" : "Emil", "year" : 2004}, "key2":{"name" : "Tobias", "year" : 2007}, "key3":{"name" : "Linus","year" : 2011}}

print(myfamily["key1"]["name"], myfamily["key1"]["year"]) #access item in nested dictionary

print(myfamily["key2"]["name"], myfamily["key2"]["year"])

print(myfamily["key3"]["name"], myfamily["key3"]["year"])

for key,val in myfamily1.items():
    print(key)
    for y in val:
        print(y + ":" , val[y])