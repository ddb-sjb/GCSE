age1 = int(input("Age 1: "))
age2 = int(input("Age 2: "))
age3 = int(input("Age 3: "))

budget = float(input("Total Budget: "))
totalage = age1+age2+age3

pres1 = budget * (age1/totalage)
pres2 = budget * (age2/totalage)
pres3 = budget * (age3/totalage)

print(f"£{pres1}")
print(f"£{pres2}")
print(f"£{pres3}")


###   BUDG3T5