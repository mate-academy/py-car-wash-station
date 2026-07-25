class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        if not (1 <= comfort_class <= 7):
            raise (ValueError
                   ("A comfort_class értékének 1 és 7 között kell lennie!"))

        if not (1 <= clean_mark <= 10):
            raise (ValueError
                   ("A clean_mark értékének 1 és 10 között kell lennie!"))

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
    ):
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise (
                ValueError(
                    "A distance_from_city_center "
                    "1.0 és 10.0 között kell legyen!"
                )
            )
        if not (1.0 <= average_rating <= 5.0):
            raise (ValueError
                   ("Az average_rating 1.0 és 5.0 között kell legyen!"))

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Költség = autó komfort osztálya *
        (mosó clean_power - autó clean_mark)
        * mosó átlagos értékelése / mosó távolsága a várostól
        """
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car):
        """
        Ha a mosó ereje nagyobb, mint az autó tisztasága,
        akkor az autó tisztasága felülíródik a mosó clean_power értékére.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float):
        """
        Hozzáad egy új értékelést, és újraszámolja
        az átlagot és az értékelések számát.
        """
        total_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1

        self.average_rating = round(
            (total_score + new_rating) / self.count_of_ratings, 1
        )

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Kiszolgálja az autókat: amelyiket le lehet mosni, azt kimossa,
        kiszámolja az árát, és visszatér a teljes bevétellel.
        """
        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:

                price = self.calculate_washing_price(car)
                total_income += price

                self.wash_single_car(car)

        return round(total_income, 1)
