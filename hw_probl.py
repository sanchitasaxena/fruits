##### GIVEN #####
# fruit name    #         
# city name     #
# price         #
##### GIVEN #####


#Q1: What DS would you use?

# First try, I'm using a dictionary of dictionaries because the keys will be great ways
# to look up values for the fruit name, city, and price.
# Second try, I'll be using a list of tuples because I can iterate by using indices
#

#Q2: For that DS, find the...
#    1) cheapest fruit (name)
#    2) cheapest fruit (city)
#    3) which city has the most fruits (type of)
#    4) wich is the most abundant fruit in the US
#Q2: Now use the other DS too!


fruit_dicts = [{'name': 'orange', 'city': 'SF', 'price': 5},
                {'name': 'orange', 'city': 'LA', 'price': 6},
                {'name': 'apple', 'city': 'NY', 'price': 2},
                {'name': 'apple', 'city': 'SF', 'price': 3}]

fruit_tuple = [('orange', 'SF', 5),
               ('orange', 'LA', 6),
               ('apple', 'NY', 2),
               ('apple', 'SF', 3)]


#create a list that will hold the price key values and their
#corrusponding fruit names as a tuple

# Using the first DS
def cheapest_fruit_name(fruit_dicts):

    cheapest_fruit = fruit_dicts[0]
    for fruit in fruit_dicts:
        if fruit['price'] < cheapest_fruit['price']:
            cheapest_fruit = fruit

    return cheapest_fruit['name']

    ################### FIRST ATTEMPT #####################
    # #creating an empty list to pair the fruit and their price in a tuple
    # fruit_prices = []
    # #iterating over the length of the dictionary and defining name, price
    # for i in range(len(first)):
    #     name = first[i]['name']
    #     price = first[i]['price']
    #     #adding the name and price into a list
    #     fruit_prices.append((name, price))


    # #finding the min price so creating a list of prices first
    # prices = []
    # for item in fruit_price:
    #     fruit_name = item[0]
    #     value = item[1]
    #     prices.append(value)
    #     cheapest = min(prices) #WHAT IT DOESN'T RELATE TO THE DAMN FRUIT NAME!!!!




def cheapest_fruit_city(fruit_dicts):

    cheapest_fruit = fruit_dicts[0]
    for fruit in fruit_dicts:
        if fruit['price'] < cheapest_fruit['price']:
            cheapest_fruit = fruit

    return cheapest_fruit['city']



def city_with_most_fruits_type(fruit_dicts):

    # the city with the most fruit, and what kinds of fruits
    # output I want {'SF': ['apple','orange']}
    cities = {}
    types_of_fruits = []

    for fruit in fruit_dicts:
        key = fruit['city']
        value = fruit['name']
        types_of_fruits.append(value)

        if key not in cities:
            cities[key] = []

        cities[key].append(value)

    max_fruits_length = 0

    for city, value in cities.items():
        if len(value) > max_fruits_length:
            max_fruits_length = len(value)
            max_fruits_city = city
            max_fruits = value

    return (max_fruits_city, max_fruits)


print city_with_most_fruits_type(fruit_dicts)





    # def most_abundant_fruit():
    # have no idea how to even start this one

############################## Using the second DS ##############################