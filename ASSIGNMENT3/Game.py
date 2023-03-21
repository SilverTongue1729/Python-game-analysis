from colorama import init
import sys

"""Custom Modules"""
from input import input_with_timeout
import Engine 
from CentralProcessingUnit import CentralProcessingUnit 
from Village import Village
import Infrastructure
import Army
from datetime import datetime
from time import sleep


# -----------------------------Starting--------------------------------------------------
init()
today = datetime.today()
name = f"{today.year}-{today.month}-{today.day}-{today.hour}-{today.minute}-{today.second}"
path = f"./Replays/ReplayFiles/{name}"
InputStorage = open(path,'wt')
print("clash of clans")
sleep(1)
Engine.Canvas.clear()


# -----------------------------Variable Initialization----------------------------------
Window = Engine.Canvas()
Village = Village("Sukhu",Window) 

TownHall = Infrastructure.TownHall([9,40])
TownHall.UpdateOnVillage(Village)

Huts_list = []
Huts_list.append(Infrastructure.Huts([7,37]))
Huts_list.append(Infrastructure.Huts([7,48]))
Huts_list.append(Infrastructure.Huts([12,37]))
Huts_list.append(Infrastructure.Huts([12,48]))
Huts_list.append(Infrastructure.Huts([5,5]))
for hut in Huts_list:
    hut.UpdateOnVillage(Village)

Walls_list = []
for row in range(5,16):
    for column in range(33,55):
        if(row == 5 or row == 15 or column == 33 or column == 54):
            Walls_list.append(Infrastructure.Walls([row,column]))
for wall in Walls_list:
    wall.UpdateOnVillage(Village)

Cannon_list = []
Cannon_list.append(Infrastructure.Cannon([9,37]))
Cannon_list.append(Infrastructure.Cannon([9,48]))
for cannon in Cannon_list:
    cannon.UpdateOnVillage(Village)

King = Army.King()
King.UpdateOnVillage(Village)
Window.UpdateCanvas(King.KingHealthBar(Village),[Village.StartingIndexOnCanvas[0]+Village.VillageRows,Village.StartingIndexOnCanvas[1]])

Barbarian_list = []

if(not Village.UpdateCanvas()):
    sys.exit("Boundary Condition exceeded")
IsEnd = False
Win = False

print(Village.VillageName) # Just for that cursor glitch
Window.RenderCanvas()


# ----------------------------------------GamePlay------------------------------------
while not IsEnd:
    Engine.Canvas.BringCursortoStart()
    ch = input_with_timeout(0.1)
    if ch is not None:
        InputStorage.write(ch)
    [IsEnd,Win] = CentralProcessingUnit.UpdatingVillage(ch,Village,TownHall,Huts_list,Walls_list,Cannon_list,King,Barbarian_list)
    Window.UpdateCanvas(King.KingHealthBar(Village),[Village.StartingIndexOnCanvas[0]+Village.VillageRows,Village.StartingIndexOnCanvas[1]])
    Window.RenderCanvas()


# ----------------------------------------Ending--------------------------------------- 
Window.BringCursortoEnd()
Engine.Canvas.clear()
if (Win):
    print("You have what it takes to be Clash of Clan master. VICTORY!")
else:
    print("You need to train harder. LOST!")
print("Thankyou for Playing")
