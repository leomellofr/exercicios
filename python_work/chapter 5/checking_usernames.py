current_users = ['Leo', 'Beck', 'Wilson', 'Matt', 'Will']
new_users = ['wilson', 'hannah', 'marcy', 'will', 'grace']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already in use.")
    else:
        print(f"{new_user} is available!")

