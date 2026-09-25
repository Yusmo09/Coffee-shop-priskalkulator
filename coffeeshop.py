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
coffee = input("What type of coffee would you like? ").title()

#Her velger eg prisen for alle kaffe typene
if coffee=="Espresso":
   price = price + 2.50

elif coffee=="Americano":
   price = price + 3

elif coffee=="Latte":
   price = price + 2.50

elif coffee == "Cappuccino":
   price = price + 3

elif coffee == "Macchiato":
   price = price + 2.50

elif coffee == "Mocha":
   price = price + 3.50

elif coffee == "Flat White":
   price = price + 2.50

#Her spør den hva størrelse kunden ønsker på drikken sin
print("----------------------------")
print("We have the following sizes")
print("Medium")
print("Large")
print("XL")
size = input("What size would you like: ")
if size == "Medium":
   size = size + 0

elif size == "Large":
   size = size + 1

elif size == "XL":
   size = size + 1.5

print("----------------------------")
takeAway = input("Would you like take away, yes or no?: ")
if takeAway == "no":
   price = price + 0

elif takeAway == "yes":
   price = price + 1
print("----------------------------")
total = price + size
print(f"Total Cost: £ {price} + {size} = {total}")