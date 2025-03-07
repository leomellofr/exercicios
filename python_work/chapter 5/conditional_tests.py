boyfriend = 'beck'
print("Is boyfriend == 'beck'? I predict True.")
print(boyfriend == 'beck')

print("\nIs boyfriend == 'others'? I predict False.")
print(boyfriend == 'others')

favorite_cat = 'michael'
print("\nIs favorite_cat == 'michael'? I predict True.")
print(favorite_cat == 'michael')

print("\nIs favorite_cat == 'big cat'? I predict False.")
print(favorite_cat == 'big cat')

favorite_band = 'mcr'
print("\nIs favorite_band == 'mcr'? I predict True.")
print(favorite_band == 'mcr')

print("\nIs favorite_band == 'thursday'? I predict False.")
print(favorite_band == 'thursday')

best_album = 'bullets'
print("\nIs best_album == 'bullets'? I predict True.")
print(best_album == 'bullets')

print("\nIs best_album == 'danger days'? I predict False.")
print(best_album == 'danger days')

last_artist = 'suicidal tendencies'
print("\nIs last_artist == 'suicidal tendencies'? I predict True.")
print(last_artist == 'suicidal tendencies')

print("\nIs last_artist == 'misfits'? I predict False.")
print(last_artist == 'misfits')

username = 'leo'
if username == 'leo':
    print(f"\nHello, {username.title()}!")

username = 'beck'
if username != 'leo':
    print("Unrecognized user")

home = 'Araraquara'
print(home.lower() == 'araraquara')
print(home.lower() == 'matão')

age_1 = 19
age_2 = 21

print((age_1 >= 21) and (age_2 >= 21))
print((age_1 >= 21) or (age_2 >= 21))

print(age_1 > 18)
print(age_1 > 21)

print(age_2 < 25)
print(age_2 < 18)

print(age_1 <= 19)
print(age_2 <= 19)

places = ['araraquara', 'sorocaba', 'são paulo']
print('são paulo' in places)
print('matão' in places)

friends = ['ester', 'henrique', 'dedé']
person = 'bel'

if person not in friends:
    print(f"{person.title()} is not my friend")