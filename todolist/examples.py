# create a list
myList = ["red", "green", "blue"]
# add to the list
myList.append("orange")
# print the list
print(myList)
# how to access an individual item
print(myList[len(myList)-1])
# how to remove an item from the list by index
myList.pop(1)
print(myList)
# how to make a menu
while True:
    print("Choose 1 for fun")
    print("Choose 2 for work")
    print("Choose 3 to quit")
    choice = input("What is your choice?")
    if choice == "1":
        print("You chose fun")
    elif choice == "2":
        print("You chose work")
    elif choice == "3":
        print("bye!!")
        break
    else:
        print("Not a valid choice")

# How to display the list and have the user select
# what to remove
list2 = ["red", "green", "blue", "orange", "purple"]
# print the list

while True:
    for i in range(0, len(list2)):
        print(str(i + 1) + ". " + list2[i])
    choice = input("Which item to remove or q to quit?")
    if choice == "q":
        break
    elif choice.isnumeric() and int(choice) <= len(list2):
        choice = int(choice)
        list2.pop(choice - 1)
    else:
        print("Not a valid choice")

