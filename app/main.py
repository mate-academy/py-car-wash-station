class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = max(1, min(7, comfort_class))
        self.clean_mark = max(1, min(10, clean_mark))
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float,
            clean_power: int, average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = (
            max(1.0, min(10.0, distance_from_city_center))
        )
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = []
        cars_to_wash = [
            car for car in cars if car.clean_mark < self.clean_power
        ]
        for one_car_to_wash in cars_to_wash:
            income.append(self.calculate_washing_price(one_car_to_wash))
            self.wash_single_car(one_car_to_wash)
        return round(sum(income), 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_power_deficit = (self.clean_power - car.clean_mark)
        income_one_car = (
            (car.comfort_class * clean_power_deficit * self.average_rating)
            / self.distance_from_city_center
        )
        return income_one_car

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        rate = max(1.0, min(rate, 5.0))
        average_score = (
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1))
        self.average_rating = round(average_score, 1)
        self.count_of_ratings += 1
