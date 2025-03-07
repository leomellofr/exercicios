pizzas = ['cheese', 'chicken', 'sausage']
friend_pizzas = pizzas[:]

pizzas.append('ribs')
friend_pizzas.append('broccoli')

print("My favorite pizzas are:")
for pizza in pizzas[:4]:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas[:4]:
    print(pizza)