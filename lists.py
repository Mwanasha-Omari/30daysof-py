
# Create an empty tuple

numbers=()


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

names=("Ali","Alima","Mary","Wanja","Anne","Mike")


# Join brothers and sisters tuples and assign it to siblings
sisters=("Alima","Mary","Wanja","Anne")
brothers=("Ali","Mike")
siblings=sisters+brothers
print(siblings)


# How many siblings do you have?

print(len(names))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family=("Mother","father")
names+=family
print(names)


# Exercises: Level 2


# Unpack siblings and parents from family_members
(parents, children, *family)=names
print(parents)
print(children)
print(family)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
vegetables=("Kales","Cabbage","Spinach","Brocolli")
animalproducts=("Milk","eggs","cheese","meat")
food_stuff_tp=vegetables+animalproducts
print(food_stuff_tp)


# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[3])

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[-3:])
print(food_stuff_tp[0:3])


# Check if an item exists in tuple:
 
if "Milk" in food_stuff_tp:
  print("true")
# Check if 'Estonia' is a nordic country
  nordiccountry=('Estonia','Iceland')
  if "Estonia" in nordiccountry:
    print("Estonia is a nordic country")

# Check if 'Iceland' is a nordic country
if "Iceland" in nordiccountry:
    print("Iceland is not a nordic country")

    
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    



# Sort the list and find the min and max age
ages.sort()
print(ages)

print("min=",min(ages))
print("max=",max(ages))

# Add the min age and the max age again to the list
ages.insert(1,22.8)
print(ages)
ages.insert(2,24.0)
print(ages)


# Find the median age (one middle item or two middle items divided by two)
print("The original list : " + str(ages)) 
ages.sort() 
mid = len(ages) // 2
res = (ages[mid] + ages[~mid]) / 2
print( str(res)) 
# Find the average age (sum of all items divided by their number )
    
average = sum(ages)/len(ages)

print(round(average,1))


# Find the range of the ages (max minus min)



# Compare the value of (min - average) and (max - average), use abs() method
    

