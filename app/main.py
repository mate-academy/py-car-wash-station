class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income = self.calculate_washing_price(car)
                total_income += income
                self.wash_single_car(car)

        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        point_power_mark = self.clean_power - car.clean_mark
        point_rating_distance = self.average_rating / self.distance_from_city_center
        income = car.comfort_class * point_power_mark * point_rating_distance

        return round(income, 1)

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        if rate < 1 or rate > 5:
            raise ValueError("Rate must be between 1 and 5. From very good - 5 to absolutely bad - 1")

        total_rating = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=10,
    average_rating=3.5,
    count_of_ratings=6
)