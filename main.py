class Car:

  def drive(self):
    print("Zoom Zoom Zoom")

  def reverse(self):
    print("Backing Up!")

  #Constructor Method - Parameters
  def __init__(self,whatColor,makeInput,howManyPassengers,hasRims,hasSpoilers):
    self.color = whatColor
    self.make = makeInput
    self.passengers = howManyPassengers
    self.rims = hasRims
    self.spoilers = hasSpoilers

  def turn(self):
    print("We're turning")

  def honk_horn(self):
    print("Honk Honk")

colesCar = Car("blue","Dodge",4,True,False)

print(colesCar.color)
print(colesCar.rims)

colesCar.honk_horn()
colesCar.drive()
colesCar.turn()

'''

OBJECT-ORIENTED PROGRAMMING

WHAT DO YOU NEED TO BUILD A CAR?
Transmission
Engine
Tires
Wheels
Shocks
sSeats
Body
Lights
car mirrors.

HOW CAN YOU CUSTOMIZE A CAR?
Spoilers
Rims
rack and pinion
colors.s
Make/Model
Window Tints
lights
engine Size
Turbo
HORn

WHAT CAN A CAR DO?
Drive - Forward / Backward
Turn - Left / Right
Parallel Park
Speed Up / Slow Down
Stop
Add Fuel / Use Fuel

'''




