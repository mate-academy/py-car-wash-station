class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) \
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            clean_difference = self.clean_power - car.clean_mark
            price = (
                car.comfort_class
                * clean_difference
                * self.average_rating
                / self.distance_from_city_center
            )
            rounded_price = round(price, 1)
            return rounded_price
        else:
            return 0.0

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars_list: list[Car]) -> float:
        total_income = 0.0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        new_total = total_rating + rate
        new_count = self.count_of_ratings + 1
        new_average = new_total / new_count
        self.average_rating = round(new_average, 1)
        self.count_of_ratings = new_count
