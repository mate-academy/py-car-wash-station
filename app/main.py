class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating):
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


# Testes
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
wash_station = CarWashStation(5, 6, 3.5, 6)

print(wash_station.serve_cars([bmw, audi]))
print(bmw.clean_mark)
print(audi.clean_mark)

wash_station.rate_service(5)
print(wash_station.average_rating)
print(wash_station.count_of_ratings)
