#Her setter eg verdiene av alle de forskjellige prisene på menyen, og sitter de inni ordbøker slik at vi kan hente de ut lettere senere i programmet
coffeeMeny = {
   "Espresso": 2.50,
   "Americano": 3,
   "Latte": 2.50,
   "Cappuccino": 3,
   "Macchiato": 2.50,
   "Mocha": 3.50,
   "Flat White": 2.50,
}

sizeMeny = {
   "M": 0,
   "L": 1,
   "XL": 1.5,
}

takeAway = {
   "No": 0,
   "Yes": 1,
}


#Her lagde eg en kode som går gjennom hele tiden og sjekker om svaret brukeren tar inn er rett eller om vi har det på menyen eller ikke dersom det ikke er et produkt eller valg fra listen brukeren tar inn,
# ber vi brukeren prøve på nytt og skrive noe fra menyen vår.
def validerOrder(spørsmål, coffeMeny):
   while True:
      svar = input(spørsmål).title().strip()
      if svar in coffeMeny:
         return svar
      print(f"{svar} er ikke et gyldig valg. Prøv igjen med et annet alternativ fra listen.\n")


#Her bare passer den på å printe ut det brukeren valgte
def vis_meny(tittel, meny):
   print("")
   print("----------------------------")

   print(tittel)
   for valg in meny:
      print(f" > {valg}")

   print("")
   print("----------------------------")


#Her lager vi hele hovedprogrammet, og hva rekkefølge alt skal gå i for å få det til å funke.
def mainprogram():
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
   print("+                               +")
   print("+         The Coffee Shop       +")
   print("+              Welcome          +")
   print("+                               +")
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

   totalPrice = 0.0


#Her henter vi ut valgene brukeren kan ta utifra hva vi har tatt i menyen i starten, hva type kaffe, størrelse og take away eller ikke. Vi henter de ut og lar brukeren velge hvem av de brukeren ønsker, 
# deretter blir prisen for det brukeren valgte lagt til i totalsummen
   vis_meny("We serve these following coffee", coffeeMeny)
   chosenCoffee = validerOrder("What type of coffee would you like?: ", coffeeMeny)
   totalPrice += coffeeMeny[chosenCoffee]

   vis_meny("We serve these following sizes", sizeMeny)
   chosenSize = validerOrder("What size would you like?: ", sizeMeny)
   totalPrice += sizeMeny[chosenSize]

   vis_meny("We offer take out", takeAway)
   chosenTakeAway = validerOrder("Would you like to eat in or take away?: ", takeAway)
   totalPrice += takeAway[chosenTakeAway]


#Her printer vi ut det brukeren valgte for sin bestilling, der brukeren får en type kvitering på hva de bestilte, og så viser vi totalsummen på slutten.
   print("----------------------------")
   print("Final order")
   print(f" * Coffe: {chosenCoffee} ")
   print(f" * Size: {chosenSize} ")
   print(f" * Take away: {chosenTakeAway} ")

   print("")
   print("----------------------------")

   print(f"Your total is {totalPrice}£")

   print("----------------------------")

#Til slutten her kjører vi hele programmet vi nettop skrev med en enkel aktiveringskode
mainprogram()
