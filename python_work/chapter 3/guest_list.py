guests = ['gerard way', 'anthony green', 'frank iero']

message_1 = f"Hi {guests[0]}, please come to my dinner party"
print(message_1)

message_2 = f"Hi {guests[1]}, please come to my dinner party"
print(message_2)

message_3 = f"Hi {guests[2]}, please come to my dinner party"
print(message_3)

print("frank iero can't make it guys im so sorry")
del guests[2]
guests.append('ryan ross')

message_4 = f"Hi {guests[2]}, please come to my dinner party"
print(message_1)
print(message_2)
print(message_4)

print('hey guys i found a new awesome table')

guests.insert(0, 'pete wentz')
guests.insert(2, 'm shadows')
guests.append('mikey way')

# renaming the values cause idk how else to make it work lol
new_message1 = f"Hi {guests[0]}, please come to my dinner party"
print(new_message1)

new_message2 = f"Hi {guests[1]}, please come im getting desperate"
print(new_message2)

new_message3 = f"Please {guests[2]} i need this"
print(new_message3)

new_message4 = f"{guests[3]} do you hate me be honest"
print(new_message4)

new_message5 = f"Hiii {guests[4]} dinner tonite? hahahahaha"
print(new_message5)

new_message6 = f"Im gonna kill myself {guests[5]}"
print(new_message6)

print('hey guys im so sorry i can literally only invite two people now')

guests.pop(0)
print('hey girl ur uninvited good luck w the mikey stuff')

guests.pop(2)
print('bye faggot')

guests.pop(2)
print('what happened with brendon? ur uninvited btw')

guests.pop(2)
print('dude theres a crazy guy making livejournal posts abt u. go deal with him u dont need to come')

print(f"hi {guests[0]} pookie ur still invited obviously")
print(f"{guests[1]} ur invited as long as u dont talk about israel")

print(f"{len(guests)}")