from restaurants import Restaurant, IcecreamStand


rest1 = Restaurant('Chong Li\'s dog chop','Chinese')
rest2 = Restaurant('Oves grill','Mosbricka')
rest3 = Restaurant('Pacos MexMix','Texican')

rest1.describe()
rest1.open_restaurant()
rest1.increment_number_served(10)
print("We have served " + str(rest1.number_served))
rest2.describe()
rest2.open_restaurant()
rest3.describe()
rest3.open_restaurant()

icestand1 = IcecreamStand('Cheech and Chongs icecream van','herbal')
icestand1.describe()
icestand1.get_flavours()
icestand1.open_restaurant()
