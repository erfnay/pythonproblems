# Finds intersections of 2 incrementing/decrementing lists

# splits inputs into more useable integer format
def split (list):
    list = list.split()
    return list

def convert (point):
    point = int(point)

    return point

# get inputs
inc = raw_input("Input an incrementing list: ")
dec = raw_input("Input a decrementing list: ")

# Splits the inputs into distinct points
inc = split (inc)
dec = split (dec)

i = 0
count = 0

# Loops maximum of 50 times to save time on determining no intersections
while True:
    if convert(inc[i]) < convert(dec[i]):
        i = int(round((i + len(dec)) / 2))


    elif convert(inc[i]) > convert(dec[i]):
        i = int(round((i / 2)))

    elif convert(inc[i]) == convert(dec[i]):
            print "Intersection at item", (i + 1)
            break

    count += 1

    if count >= 50:
        print "No intersection found"
        break
