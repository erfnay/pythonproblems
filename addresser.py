#5 LINES BITCH
address = raw_input("Feed me an email address: ")
for i in range(1, len(address)):
    if (address[i].isdigit() == False and address[i] == address[i].upper()):
        address = address[:i] + " " + address[i:]
address = address.replace("-", " ").replace("@", " ").replace(".", " ").split()

print address
