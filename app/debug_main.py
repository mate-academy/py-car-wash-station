from app.main import Car, CarWashStation

# Налаштуйте автомобілі та мийку відповідно до тестів
cars = [
    Car(3, 3, "BMW"),
    Car(4, 5, "Audi"),
    Car(7, 1, "Mercedes")
]
wash_station = CarWashStation(6, 7, 3.9, 11)

# Запуск serve_cars
income = wash_station.serve_cars(cars)

print(f"Total income: {income}")
print(f"Cars after washing: {[car.clean_mark for car in cars]}")

# Тест rate_service
wash_station.rate_service(5)
print(f"Average rating after rate_service: {wash_station.average_rating}")
