#  This is code for Kai's Restaurant
#  This was written by Mr. Russ
#




print("Welcome to Kai's Italian Bistro!")
print("Please Choose Your Dish")


customer_order = input("Z - Fettucini Alfredo   Y - Spaghetti  X - Lasagna   W - Pizza ")


#FOR - Loops that go on for a definiate amount of time
#WHILE - Loops that go on for an indefiniate amount of time




while True:
  if customer_order == "Z":
    print("Here is your Fettucini")
  elif customer_order == "Y":
    wantMeatballs = input("Do you want meatballs?")
    if wantMeatballs == "Yes":
      print("Great, here's your meatballs")
    else:
      print("No, that's too bad!")
    print("Enjoy Your Spaghetti")
  elif customer_order == "X":
    print("Here is your Lasagna")
  elif customer_order == "W":
    print("Here is your Pizza")
  else:
    print("We don't have that, please try again!")
