#9-1. Restaurant: Make a class called Restaurant. 
#The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name: str , cuisine_type: str) -> None:
        self.restaurant_name: str = restaurant_name
        self.cuisine_type: str= cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name , self.cuisine_type)
    def open_restaurant(self):
        print("the restaurant is open")
restaurant = Restaurant("dinzu", "giapponese")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

#9-2. Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for each instance.
restaurant1 = Restaurant("La romana", "casalinga")
restaurant2 = Restaurant("Sole" , "asiatica")
restaurant3 = Restaurant("MC" , "americana")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9-3. Users: Make a class called User.

#Create two attributes called first_name and last_name, and then create several other attributes
#that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name: str , last_name: str , password: str , pin: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.pin = pin
    def describe_user(self):
        print(self.first_name , self.last_name , self.password , self.pin)
    def greet_user(self):
        print(" Hi user!")
fice = User("hey", "bye" , "fc" , "1900")
polpo = User("ciao" , "addio" , "plp" , "1927")

#9-4. Number Served: Start with your program from Exercise 9-1. 
#Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. 
#Print the number of customers the restaurant has served, and then change this value and print it again. 
#Add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again. 
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business. 






#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
#Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors. 
#Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list[str], number_served: int = 0) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def print_favors(self) -> None:
        print(self.flavors)




#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. 
#Add a method to the Battery class called upgrade_battery(). 
#This method should check the battery size and set the capacity to 65 if it isn’t already. 
#Make an electric car with a default battery size, 
#call get_range() once, and then call get_range() a second time after upgrading the battery. 
#You should see an increase in the car’s range.
pass