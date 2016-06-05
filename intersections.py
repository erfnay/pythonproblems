# Finds intersections of 2 incrementing/decrementing lists

# converts inputs into more useable integer format
def convert (list):
    list = list.split()
    for i in range (0, len(list)):
        list[i] = int(list[i])

    return list

# get inputs
inc = raw_input("Input an incrementing list: ")
dec = raw_input("Input a decrementing list: ")

# Converts strings into numbers
inc = convert (inc)
dec = convert (dec)

i = 0
count = 0

# Loops maximum of 50 times to save time on determining no intersections
while True:
    if inc[i] < dec[i]:
        i = int(round((i + len(dec)) / 2))


    elif inc[i] > dec[i]:
        i = int(round((i / 2)))

    elif inc[i] == dec[i]:
            print "Intersection at item", (i + 1)
            break

    count += 1

    if count >= 50:
        print "There is no intersection"
        break
