class Car:
    def __init__(self, comfort_class: int | float,
                 clean_mark: int | float,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int | float,
                 clean_power: int | float,
                 average_rating: int | float,
                 count_of_ratings: int | float) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int | float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return total_income

    def calculate_washing_price(self, car: Car) -> int | float:
        income_from_car = car.comfort_class \
            * (self.clean_power - car.clean_mark) \
            * self.average_rating / self.distance_from_city_center
        return round(income_from_car, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int | float) -> None:
        av_rate = (self.count_of_ratings * self.average_rating + new_rate) \
            / (self.count_of_ratings + 1)
        self.average_rating = round(av_rate, 1)
        self.count_of_ratings += 1
