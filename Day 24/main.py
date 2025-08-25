#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
placeholder = "[name]"
#read
letter_file = open("./Input/Letters/starting_letter.txt")
letter = letter_file.read()
names_file= open("./Input/Names/invited_names.txt")
for name in names_file.readlines():
    guest = name.strip()
    invite= letter.replace(placeholder,guest)
    print(invite)
    with open(f"./Output/ReadyToSend/Letter_for_{guest}","w") as rts:
        rts.write(invite)
