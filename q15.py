cap = int(input("Sleigh Capacity: "))
volumes = input("Volumes: ")

volumes = volumes.split(' ')

total_vol = 0
for i in volumes:
    total_vol = total_vol + int(i)

if total_vol <= cap:
    print("Fits")
else:
    print("Does not fit")


### SL31GH5