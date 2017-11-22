import csv
I = open('inventory.csv')

#Create ingredient class
class Ingredient(object):
    def __init__(self, price, amount, name):
        self.name = str(name)
        self.price = price
        self.amount = amount
        self.per_ml = (float(price) / float(amount)) / 100

#Class ingredients
nicotine = Ingredient(1900, 120, "Nicotine")
vegetable_glycerin = Ingredient(2800, 3785, "Vegetable Glycerin")
strawberry = Ingredient(3000, 1000, "Strawberry")
strawberry_ripe = Ingredient(2100, 500, "Strawberry Ripe")
watermelon = Ingredient(4750, 1000, "Watermelon")
koolada = Ingredient(900, 120, "Koolada")

#Create recipe
orig_recipe = {
nicotine : 0.02,
vegetable_glycerin : 0.77,
strawberry: 0.07,
strawberry_ripe: 0.05,
watermelon: 0.07,
koolada: 0.02
}

def batch_cost(recipe, batch_size):
    total = 0.0
    for ing in recipe:
        ing_amt = float(recipe[ing]) * float(batch_size)
        ing_cost = float(ing_amt) * float(ing.per_ml)
        total += ing_cost
    return total

def batch_price(batch_size):
    if batch_size <= 120:
        price = batch_size * 0.16
    if batch_size > 120 and batch_size <= 500:
        price = batch_size * 0.14
    if batch_size > 500:
        price = batch_size * 0.12
    return price

def batch_profit(recipe, batch_size):
    profit = batch_price(batch_size) - batch_cost(recipe, batch_size)
    return profit

def print_recipe(recipe):
    for ing in recipe:
        print (ing.name, ": %i" % (recipe[ing]* 100))

def print_inventory():
    reader = csv.reader(I)
    for row in reader:
        print (row)

def process_sale(recipe, batch_size):
    print (batch_price)
    print (batch_profit)
    reader = csv.reader(I)
    for ing in recipe:
        for row in reader:
            if ing = 




# print ("%.2f" % batch_price(120))
I.close()
