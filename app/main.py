class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, cars):
        return round(cars.comfort_class * (
            abs(cars.clean_mark - self.clean_power)
        ) * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, cars):
        if cars.clean_mark < self.clean_power:
            cars.clean_mark = self.clean_power

    def rate_service(self, rate):
        self.average_rating = round(
            (
                self.average_rating * self.count_of_ratings + rate
            ) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return round(self.average_rating, 1)


bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

print(bmw.brand)
print(bmw.__dict__)
print(ws.__dict__)
