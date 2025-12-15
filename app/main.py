class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        list_of_costs: list[int | float] = []

        for car in cars:
            if car.clean_mark < self.clean_power:
                list_of_costs.append(self.wash_single_car(car))

        return round(sum(list_of_costs), 1)

    def wash_single_car(self, car: Car) -> float:

        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power

        return price

    def calculate_washing_price(self, car: Car) -> float:

        clean_diff = abs(self.clean_power - car.clean_mark)

        rate: int | float = 0

        if not self.distance_from_city_center == 0:
            rate = self.average_rating / self.distance_from_city_center
        else:
            rate = self.average_rating

        return car.comfort_class * (clean_diff * (rate))

    def rate_service(self, rate: int) -> None:

        sum_of_rate = (self.average_rating * self.count_of_ratings) + rate
        new_rate = sum_of_rate / (self.count_of_ratings + 1)

        self.average_rating = round(new_rate, 1)
        self.count_of_ratings += 1
