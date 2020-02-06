import random
import time
import replit


roomArray = []
itemArray = []

for i in range(999):
  roomArray.append(False)
  itemArray.append(False)
#if item in room. print item in a new print row


roomArray[101] = "You start here, there are rooms around you, there is a room to the East and South of you."
roomArray[102] = "You walk into this room and there is a room to the East of you"
roomArray[201] = "You walk into this random room"
roomArray[202] = "Your right is blocked off by a locked and blocked off door."
roomArray[203] = "You enter the hallway, you can only go back or enter the room to the East."
roomArray[301] = "You enter the room, it's a dead end. You can only go West."
roomArray[303] = "This room looks like a normal room."
roomArray[304] = "You found an oddly atrocious window!"
roomArray[402] = "There is nothing in here? You should probably leave.."
roomArray[403] = "You enter another spooky room... You should probably leave immediately."
roomArray[404] = "You found another empty room and there is a door to the East."
roomArray[503] = "Ayy! You found the escape, congrats!! You made it out of this horrifying dungeon."
roomArray[504] = "This a deadend."

itemArray[102] = "You find a key laying on the ground."
itemArray[201] = "There's a stray painting hanging on the wall."
itemArray[203] = "The only thing interesting in this room is a single painting that seems to have been knocked onto the ground."
itemArray[301] = "You come across a dead body, this surpises you for some unknown reason."
itemArray[303] = "You cross paths with some dude's corpse."
itemArray[304] = "There is a key on the floor."
itemArray[504] = "You encounter a key, this one seems important."

def doesRoomExist(roomNumber):
  try:
    if roomArray[roomNumber] == False:
      print("You can’t go there")
      return False
    else:
      return True 
  except:
    print("You can't go there.")
    return False

def Move(userInput, location):
  if userInput == "n" and doesRoomExist(location - 1) == True:
    location -= 1
  else:
    if userInput == "s" and doesRoomExist(location + 1) == True:
      location += 1
    else:
      if userInput == "w" and doesRoomExist(location - 100) == True:
        location -= 100
      else:
        if userInput == "e" and doesRoomExist(location + 100) == True:
          location += 100
        else:
            if doesRoomExist == False:
              location += 0 #if the room doesnt exist don't move!!
              
  return location

def doesItemExist(location):
  try:
    if not itemArray[location] == False:
      print("Item: " + itemArray[location]) 
  except:
    return

def main():
  location = 101
  print("Zombie Apocalypse")
  print("By Gargaar, Kevin, and Matthew")
  time.sleep(1)
  while True:
      print(roomArray[location])
      doesItemExist(location)
      if not itemArray[location] == False:
        print("Please type: n, s, e, w, quit, or T")
      else:
        print("Please type: n, s, e, w, or quit")
      userInput = input()
      location = Move(userInput, location)
      if userInput == "T":
        print("You have taken this item")
      if userInput == "quit":
        replit.clear()
        break
      
