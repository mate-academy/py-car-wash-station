class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for i in cars:
            if i.clean_mark < self.clean_power:
                income += self.calculate_washing_price(i)
            self.wash_single_car(i)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        clean_power_difference = self.clean_power - car.clean_mark
        rating_ration = self.average_rating / self.distance_from_city_center
        return round(
            car.comfort_class * clean_power_difference * rating_ration, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        count_ration = self.average_rating * self.count_of_ratings + rate
        rating_ration = self.count_of_ratings + 1
        self.average_rating = round(
            count_ration / rating_ration, 1)
        self.count_of_ratings += 1
