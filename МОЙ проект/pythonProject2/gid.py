
temperature = int(input("Input temperature: "))


rainy = None
heavyRain = None


if temperature > 0:
   rainy = input("Is rainy: ") == "yes"

   if rainy:
       heavyRain = input("Is heavy rain: ") == "yes"


decision = "Не решил что брать. Останусь дома."
if (temperature) > 20 and (temperature < 30) :
   if rainy:
       decision = "Взять футболку шорты и дождевик"
   else:
       decision = "Взять футболку и шорты"
elif temperature > 0:
   if rainy:
       if heavyRain:
           decision = "Взять пальто, резиновые сапоги и зонт"
       else:
           decision = "Взять пальто и дождевик"
   else:
       decision = "Взять пальто"
else:
   decision = "Взять пуховик"


print(decision)