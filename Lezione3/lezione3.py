#4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, 
#instead of printing just the name of the pizza. For each pizza, 
#you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, 
#that states how much you like pizza. The output should consist of 
#three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
Kinds: list=["Margherita", "Diavola","Boscaiola"]
for favorite in Kinds:
    print(favorite)
    print(f"my favorite kinds of pizza {favorite}")
print("i like pizza")

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!
animals: list=["dog","cat","lion"]
sentence: list=["brown","black","yellow"]
for agg in zip(animals, sentence):
    print(agg[0], agg[1])
l=list(zip(animals, sentence))
print("Any of these animals would make a great pet",l)

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
number: list[21]
for number in range(21):
    print(number)

#-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
numbers: list=[]
for i in range(1, 1000001):
        #print(i)
        numbers.append(i)

#    4-5. Summing a Million: Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.  
numbers: list=[]
for i in range(1, 1000001):
        #print(i)
        numbers.append(i)
x = min(numbers)
y = max(numbers)
z = sum(numbers) 
print(z)

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.
for i in range(1, 20, 2):   
      print(i)

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
for i in range(3, 33, 3):
      print(i)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
for power in range(1, 10):
      print(power**3)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
Kinds: list=["Margherita", "Diavola", "Boscaiola", "Fiori", "Bianca"]
for favorite in Kinds:
    print(favorite)
    print(f"my favorite kinds of pizza {favorite}")
print("i like pizza")
print(f"{Kinds[:3]} the first three items in the list are") #:3= per i primi tre argomenti all'interno della lista
print(f"{Kinds[1:4]} three items from the middle of the list are")#: = con i 2 punti stiamo prndendo i valori compresi  da 1 (per esempio) a 4(perchè lultima posizione come nel range non la prende)
print(f"{Kinds[-3:]} the last three items in the list are")# -3= per gli ultimi tre argomenti della lista


 
