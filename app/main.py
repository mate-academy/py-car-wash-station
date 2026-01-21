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
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        filtered_cars = self.filter_cars(cars)
        price = 0

        for car in filtered_cars:
            price += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return price

    def filter_cars(self, cars: list[Car]) -> list[Car]:
        return [car for car in cars if car.clean_mark < self.clean_power]

    def calculate_washing_price(self, car: Car) -> float:
        power_diff = self.clean_power - car.clean_mark
        multiply = car.comfort_class * power_diff * self.average_rating

        return round(multiply / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        new_count_of_ratings = self.count_of_ratings + 1
        new_average_rating = self.get_average_rating(
            new_rate, new_count_of_ratings
        )

        self.count_of_ratings = new_count_of_ratings
        self.average_rating = new_average_rating

    def get_average_rating(self,
                           new_rate: int,
                           new_count_of_ratings: int) -> float:
        return round((self.average_rating * self.count_of_ratings + new_rate)
                     / new_count_of_ratings,
                     1)
