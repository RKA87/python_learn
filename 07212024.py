# Jul 21, 2024

# Taks 1:
# For the given employees give a salary hike of 10% and return a new dict. 

d= {"Ramesh" : 2500, "Rajesh": 1500, "Aish": 3000, "Gaur" : 2400}
hike_dict={}

for key,val in d.items():
    increased_value= val+((val*10)/100)
    hike_dict[key] = increased_value

print("Original Dictionary:",d)
print("After Hike:",hike_dict)

