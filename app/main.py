class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:

        # Валидация comfort_class
        if not 1 <= comfort_class <= 7:
            raise ValueError(
                "comfort_class должен быть целым числом от 1 до 7."
            )
        self.comfort_class = comfort_class

        # Валидация clean_mark
        if not 1 <= clean_mark <= 10:
            raise ValueError("clean_mark должен быть целым числом от 1 до 10.")
        self.clean_mark = clean_mark

        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:

        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError(
                "distance_from_city_center должно быть числом "
                "с плавающей точкой от 1.0 до 10.0."
            )
        self.distance_from_city_center = distance_from_city_center

        self.clean_power = clean_power

        # Валидация average_rating
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError(
                "average_rating должен быть числом с плавающей точкой "
                "от 1.0 до 5.0."
            )

        if round(average_rating, 1) != average_rating:
            raise ValueError(
                "average_rating должен быть округлен до 1 знака после запятой."
            )
        self.average_rating = average_rating

        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark
        cost = (car.comfort_class * difference * self.average_rating
                / self.distance_from_city_center)
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        total_ratings = self.average_rating * self.count_of_ratings
        total_ratings += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)
