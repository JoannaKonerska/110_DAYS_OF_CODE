PLACEHOLDER = "[name]"
# open my file with the names
with open("./Input/names/invited_names.txt") as names_file:
    # change the name file to the name list
    names = names_file.readlines()

# open the file with a starting letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    # read my starting letter file
    letter_contents = letter_file.read()
    # iterate through the list of names
    for name in names:
        # strip my names from the spaces
        stripped_name = name.strip()
        # replace the placeholder [name] with the stripped name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print the new letter, so we can see if it is okay
        print(new_letter)
        # write that new letter in the text file specified
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)