
file = open('places.txt', 'r')
Places = file.readlines()
print(len(Places))
n=0
for place in Places:
    if n <=952:
        print("- [{}](location)".format(place.strip()))
    elif n<= 1940:
        print("- location: [{}](location)".format(place.strip()))

    elif n<=2865:
        print("- i want to travel to [{}](location)".format(place.strip()))

    elif n<=3809:
        print("- the place i want to travel is [{}](location)".format(place.strip()))
    n+=1

