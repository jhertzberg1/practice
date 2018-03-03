def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count}, cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.")


def bottles_of_wine(wine_bottles):
    print(f"And if anyone is thirsty there's wine {wine_bottles} bottles of wine too!")


def spam(nasty_meat):
    print(f"There's {nasty_meat} disgusting meat product too if you're insane...\n")

# print function cheese_and_crackers with arguements 20{cheese_count} and 30{boxes_of_crackers}
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
bottles_of_wine(5)
spam(42)

# first make variables with amount of cheese and crackers and then run function cheese_and_crackers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
wine_bottles = 10
yuck_meat = 69

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
bottles_of_wine(wine_bottles)
spam(yuck_meat)

# first argument does 10+20 which is amount of cheese, second does 5+6 which is amount of crackers
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
bottles_of_wine(4 + 11)
spam(98 + 2)

# use previous variable amount_of_cheese and amount_of_crackers with added 100(10 + 100) and 1000(50 + 1000)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
bottles_of_wine(wine_bottles + 25)
spam(yuck_meat + 1)
