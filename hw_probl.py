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


first = {'fruit1': {'name': 'orange', 'city': 'SF', 'price': 5},
         'fruit2': {'name': 'orange', 'city': 'LA', 'price': 6},
         'fruit3': {'name': 'apple', 'city': 'NY', 'price': 2},
         'fruit4': {'name': 'apple', 'city': 'SF', 'price': 3}}

second = [('orange', 'SF', 5),
          ('orange', 'LA', 6),
          ('apple', 'NY', 2),
          ('apple', 'SF', 3)]



for key, values in first.items():
    for k, v in values.items():
        print k, v
