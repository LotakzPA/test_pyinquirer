with open('file.csv', 'r') as csvfile:
    spamreader = csvfile.read().split(', ')
    print(spamreader)

    with open('text.txt', 'w') as file:
        for name in spamreader:
            file.write(name + " ")

    with open('text2.txt', 'w') as file:
        for name in spamreader:
            file.write(name + "\n")

