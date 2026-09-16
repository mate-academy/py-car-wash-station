class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            comfort_class: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0

        return (
            (self.clean_power - car.clean_mark)
            * car.comfort_class
            * (self.average_rating / self.comfort_class)
        )

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)

        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

        return price

    def serve_cars(self, cars: list) -> float:
        total_income = 0

        for car in cars:
            total_income += self.wash_single_car(car)

        return round(total_income, 2)

    def rate_service(self, mark: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + mark)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
