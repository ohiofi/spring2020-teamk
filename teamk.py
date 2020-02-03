import random
import time

roomArray = []
itemArray = ["painting", "bronze key", "key", "painting", "dead body", "key", "dead body"]

for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

roomArray[101] = "You start here, and find a painting to your right and something shiny to your south."
roomArray[102] = "You enter this room to find a special shiny gold key."
roomArray[201] = "You enter this room only to find out there is a painting, and nothing else."
roomArray[202] = "Your right is blocked off by a locked and blocked off door."
roomArray[203] = "You found a painting in this very petrifying hallway."
roomArray[301] = "You enter this room only to find out it is a dead end and there is a dead body!! :("
roomArray[303] = "You found another dead body!! What should you do?!?!"
roomArray[304] = "You found an oddly atrocious window and something shiny!"
roomArray[402] = "There is nothing in here? You should probably leave.."
roomArray[403] = "You also found nothing in here.. Except a dead body to your left.. You should probably leave immediately."
roomArray[404] = "You found another empty room, but you heard some screaming to your right."
roomArray[503] = "Ayy! You found the escape, congrats!! You made it out of this horrifying dungeon"
roomArray[504] = "You found a bronze key, you should probably use that somewhere."

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
      if userInput == "e" and doesRoomExist(location - 100) == True:
        location -= 100
      else:
        if userInput == "w" and doesRoomExist(location + 100) == True:
          location += 100
        else:
            if doesRoomExist == False:
              location += 0 # check fix this

  return location

def Main():
  location = 301
  print("Zombie Apocalypse")
  print("By Gargaar, Kevin, and Matthew")
  time.sleep(1)
  while True:
      print(roomArray[location])
      print("Please type: n, s, e, w, or quit")
      userInput = input()
      location = Move(userInput, location)
      if userInput == "quit":
        break
      


