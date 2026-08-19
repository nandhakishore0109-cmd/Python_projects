# MINI PROJECT OF DICTIONARY_MANAGEMENT_WORDS......

# PROJECT - DICTIONARY OF WORDS
'''Create a program that manages a dictionary of word meanings. The program 
should allow users to perform the following actions:
1.Add a Word: Allow users to add new words along with their meanings to the 
dictionary.
2. Search for Meaning: Enable users to search for the meaning of a word in the 
dictionary.
3.Display All Words: Provide an option to display all words and their meanings 
currently stored in the dictionary.
4.Update Meaning: Implement a feature to update the meaning of an existing 
word in the dictionary. After updating, display the updated meaning.
5.Delete Word: Implement a feature to delete a word and its meaning from the 
dictionary. Confirm the deletion and handle cases where the word doesn't 
exist.
Ensure the program handles invalid inputs gracefully. Use a while loop to keep the 
program running until the user chooses to exit'''

dict = {}

while True:
    print("Dictionary management system" )
    print("1. Add a word")
    print("2. Meaning for word")
    print("3. Display all words")
    print("4. Update meaning")
    print("5. Delete word")
    print("6. Exit")

    choice = (input("Enter ur choice:"))

    if choice == "1":
        word = input("Enter a word:").lower()
        meaning = input("enter a meaning:")
        dict[word] = meaning
        print("word added succesfully:")

    elif choice == "2":
        word = input("Enter a word:").lower()
        if word in dict:
            print("meaning:", dict[word])
        else:
            print("word is not found in this dict")

    elif choice == "3":
        if dict:
            print("words and meaning")
            for word , meaning in dict.items():
                print(f"{word} : {meaning}")
        else:
            print("word not found in this dict")

    elif choice == "4":
        word = input("Enter a word to updated meaning:").lower()
        if word in dict:
            new_meaning = input("Enter a new meaning:")
            dict[word] = new_meaning
            print("your meaning updated sucessfully")
            print("updated meaning:", new_meaning)
        else:
            print("Given word is not found")    
        

    elif choice == "5":
        word = ("Enter a deleting word:")
        if word in dict:
            del dict[word]
            print("delected word:", delete)
        else:
            print("Given word is not found")

    elif choice == "6":
        print("exiting the program")
        break                       





