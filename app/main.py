class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: int, count_of_ratings : int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        price = car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city_center)
        price = round(price, 1)
        return price

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            incom = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return incom
        else:
            return 0

    def serve_cars(self, cars: list[Car]):
        income = 0
        for car in cars:
            income += self.wash_single_car(car)
        return income



    def rate_service(self, rate):
        self.average_rating = round((self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=2, brand='Audi')

print(bmw.clean_mark)  # 3
print(audi.clean_mark) # 2

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

print(income)  # 17.5
