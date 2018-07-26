def wordcount(filename):
     # count the words in the input file:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        print("The file " + filename + " has " + str(len(words)) + " words in it.")


filenames = ["prince.txt", "dracula.txt", "heart_of_darkness.txt"]
for filename in filenames:
    wordcount(filename)


