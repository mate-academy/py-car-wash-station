class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:

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
        """
        Приймає список автомобілів, миє лише ті, у яких
        clean_mark менший за clean_power мийки
        та повертає дохід, округлений до одного
        десяткового знака. Автомобілі, які помито,
        отримують новий clean_mark, рівний clean_power автомийки.
        """
        cars_for_washing = [
            car
            for car in cars
            if car.clean_mark < self.clean_power
        ]

        income = round(
            sum(
                [self.calculate_washing_price(car)
                 for car in cars_for_washing]
            ),
            1
        )

        for car in cars_for_washing:
            self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        """
        Обчислює вартість миття одного автомобіля
        """
        return (
            round(
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center,
                1
            )
        )

    def wash_single_car(self, car: Car) -> None:
        """
        Миє автомобіль, змінюючи його clean_mark на значення clean_power,
        якщо clean_power автомийки більший за clean_mark автомобіля.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        """
        Додає нову оцінку для мийки та оновлює
        середній рейтинг та кількість оцінок.
        """
        all_stars = self.count_of_ratings * self.average_rating + mark
        self.count_of_ratings += 1
        self.average_rating = round(all_stars / self.count_of_ratings, 1)
