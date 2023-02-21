class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class  # from 1 to 7
        self.clean_mark = clean_mark  # from very dirty -1 to absolutely clean 10
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center  # from 1.0 to 10.0
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car, func=calculate_washing_price):
        if self.clean_power > car.clean_mark:
            price = func(self, car)
            car.clean_mark = self.clean_power
        return price

    def serve_cars(self, cars: Car, func=wash_single_car):
        income = 0
        for car in cars:
            income += func(self, car)
        return income


bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

print(bmw.clean_mark)  # 3

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

incom = wash_station.serve_cars([bmw, audi])

print(incom)