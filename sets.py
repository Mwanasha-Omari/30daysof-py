it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Find the length of the set it_companies
print(len(A))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
 
it_companies.update(['Chrome','Tecno','Infinix'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)


# What is the difference between remove and discard

# Exercises: Level 2
#
#  Join A and B
lst=list(A)
lst=list(B)
print(lst)
all=A.union(B)
# Find A intersection B
A.intersection(B)
# Is A subset of B
A.issubset(B)
print("True")
# Join A with B and B with A
all=A.union(B)
all=B.union(A)