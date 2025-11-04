bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([bmw, audi, mercedes])
print(income)  # 41.7

print(bmw.clean_mark)  # 8
print(audi.clean_mark)  # 9
print(mercedes.clean_mark)  # 8

ford = Car(2, 1, "Ford")
print(ws.calculate_washing_price(ford))  # 9.1

ws.rate_service(5)
print(ws.count_of_ratings)  # 12
print(ws.average_rating)    # 4.0
