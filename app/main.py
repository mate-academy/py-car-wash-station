class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car):
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
        ) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating):
        self.count_of_ratings += 1
        self.average_rating = round(
            ((self.average_rating * (self.count_of_ratings - 1)) + rating)
            / self.count_of_ratings, 1
        )


# Приклад використання:
bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")
mercedes = Car(comfort_class=7, clean_mark=1, brand="Mercedes")

ws = CarWashStation(
    distance_from_city_center=6, clean_power=8,
    average_rating=3.9, count_of_ratings=11
)

income = ws.serve_cars([bmw, audi, mercedes])

# Вивід інформації про дохід і стан машин
print(income)  # 41.7
print(bmw.clean_mark)  # 8
print(audi.clean_mark)  # 9
print(mercedes.clean_mark)  # 8

# Розрахунок вартості мийки для машини
ford = Car(comfort_class=2, clean_mark=1, brand="Ford")
wash_cost = ws.calculate_washing_price(ford)
print(wash_cost)  # 9.1
print(ford.clean_mark)  # 1

# Додаємо новий рейтинг
ws.rate_service(5)
print(ws.count_of_ratings)  # 12
print(ws.average_rating)  # 4.0
