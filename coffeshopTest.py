coffeeMeny = {
   "Espresso": 2.50,
   "Americano": 3,
   "Latte": 2.50,
   "Cappuccino": 3,
   "Macchiato": 2.50,
   "Mocha": 3.50,
   "Flat White": 2.50,
}

def validerOrder(spørsmål, coffeMeny):
   while True:
      svar = input(spørsmål).title().strip()
      if svar in coffeMeny:
         return svar
      print(f"{svar} er ikke et gyldig valg. Prøv igjen med et annet alternativ fra listen.\n")

#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

#Når koden starter blir prisen resettet til 0 og så spør programmet hva kaffe personen ønsker
price = 0
size = 0
eatIn = 0
coffeeMeny = input("What type of coffee would you like? ").title()

#Her velger eg prisen for alle kaffe typene


#Her spør den hva størrelse kunden ønsker på drikken sin
print("----------------------------")
print("We have the following sizes")
print("M")
print("L")
print("XL")
volume = input("What size would you like: ")
if volume == "M":
   size = size

elif volume == "L":
   size = size + 1

elif volume == "XL":
   size = size + 1.5

print("----------------------------")
takeAway = input("Would you like take away, yes or no?: ")
if takeAway == "no":
   eatIn = eatIn + 0

elif takeAway == "yes":
   eatIn = eatIn + 1
print("----------------------------")
total = price + size + eatIn
print(f"Total Cost: £{price} + £{size} + £{eatIn} = £{total}")