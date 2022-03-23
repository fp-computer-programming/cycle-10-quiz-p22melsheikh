# MEE 03/23/22

price = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

#1
def average_sum (table):
    cost = 0 # cost for returning/adding the other numbers
    average = 0 # average so we can return it
    if type(table) == list:
        for price in table:
            cost += price
        average = cost / len(table) # Divide by the len for average
    else:
        print("The prices list is not not really a list!")
    
    return average

print(average_sum(price))

#2
def reduce (table):
    new_prices = [] # table/list so we can just apppend it 
    if type(table) == list:
        for price in table:
            new_prices.append(price-5)
    else:
        print("it is not a list")

    return new_prices
print(reduce(price))

#3
def money(price,sales):
    cost = 0 # return/use it/modify it
    counter = 0 # find it's value
    if type(price) == list and type(sales) == list: # checking 
        if len(price) == len(sales): #checking
            for price in price:
                print(sales[counter],"it was  was sold for","$"+str(price)) 
                counter += 1 
                cost += price 
        else:
            print("they are not the same length")
    else:
        print("one of them is not a list")
    return "the total cost is "+"$"+str(cost)+"." 
print(money(price,sales))

#4
def cost_more(table):
    new_prices = [] # new table/list 
    if type(table) == list:
        for price in table:
            if price > 40: # else if statements to check requirments
                new_prices.append(price-10)
            else:
                new_prices.append(price)
    else:
        print("it is not a list!")
    return new_prices
cost_more(price)

#5
def item_cost(price,items):
    table = [] 
    tablecounter = 0 
    counter = 0 # used to find the index in the list
    if type(price) == list and type(items) == list:
        for price in price:
            table.append(items[tablecounter][counter]+" "+"$"+str(price)) # it will go for the first list inside of the items list
            counter += 1 

            if counter >= len(items[tablecounter]): # add + 1 to the table counter to find the next table inside of the items table/list
                tablecounter += 1
                counter = 0
    else:
        print("one of them is not a list")
    return table
print(item_cost(price,items))











