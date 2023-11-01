class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = round(distance_from_city_center, 1)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:

        clean_dif = self.clean_power - car.clean_mark
        car_clas = car.comfort_class
        rate = self.average_rating
        distance = self.distance_from_city_center

        income_for_car = (car_clas * clean_dif * rate) / distance

        return round(income_for_car, 1)

    def wash_single_car(self, car: Car) -> None:

        car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:

        rating_sum = ((self.average_rating * self.count_of_ratings) + mark)
        self.count_of_ratings += 1
        self.average_rating = round(rating_sum / self.count_of_ratings, 1)

    def serve_cars(self, list_of_cars: list) -> float:
        income = 0

        for car in [car for car in list_of_cars
                    if car.clean_mark < self.clean_power]:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return income


c = Car(1, 1, "1")
print(type(c))
