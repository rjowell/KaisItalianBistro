class Car:

  maxFuel = 34
  currentFuel = 8
  lowFuel = 3

  def drive(self):
    if self.currentFuel == 0:
      print("You can't drive, you need to refuel!")
    else:
      if self.currentFuel <= self.lowFuel:
        print("Your fuel is getting low!")
      self.currentFuel -= 1
      print("Zoom Zoom Zoom")
      print(self.currentFuel)

  def reverse(self):
    if self.currentFuel == 0:
      print("You can't drive, you need to refuel!")
    else:
      if self.currentFuel <= self.lowFuel:
        print("Your fuel is getting low!")
      self.currentFuel -= 1
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

  def howMuchFuelDoIHave(self):
    return self.currentFuel

  def refuel(self,howMuchFuel):
    if self.currentFuel + howMuchFuel > self.maxFuel:
      return False
    else:
      self.currentFuel += howMuchFuel
      return True


  def honk_horn(self):
    print("Honk Honk")

  def willItStart(self):
    if self.currentFuel >= 2:
      return True
    else:
      return False

colesCar = Car("blue","Dodge",4,True,False)

colesCar.drive()
colesCar.drive()
colesCar.drive()
print(colesCar.howMuchFuelDoIHave())
colesCar.drive()
colesCar.drive()
colesCar.drive()
colesCar.refuel(20)
colesCar.drive()
print(colesCar.howMuchFuelDoIHave())


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




