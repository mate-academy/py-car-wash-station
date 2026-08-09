class Car:
    """Przedstawia samochód i jego parametry"""

    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        try:
            comfort_class = int(comfort_class)
            clean_mark = int(clean_mark)
        except (TypeError, ValueError):
            raise ValueError(
                "Klasa komfortu i stopień czystości musi być cyfrą"
            )

        if not isinstance(brand, str):
            raise TypeError("Marka samochodu musi być tekstem")

        if not (1 <= comfort_class <= 7):
            raise ValueError("Podaj zakres od 1 do 7")

        if not (1 <= clean_mark <= 10):
            raise ValueError("Podaj zakres od 1 do 10")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """Dane techniczne i pomiarowe myjni"""

    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        try:
            distance_from_city_center = float(distance_from_city_center)
            clean_power = int(clean_power)
            average_rating = float(average_rating)
            count_of_ratings = int(count_of_ratings)
        except (TypeError, ValueError):
            raise ValueError("Wartość podaj w liczbach")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("Podaj wartość w zakresie 1.0 - 10.0")

        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("Podaj wartość w zakresie 1.0 - 5.0")

        self.distance_from_city_center = round(distance_from_city_center, 1)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """Myjnia samochodowa"""

        price_all_car = []
        for car in cars:
            if self.wash_single_car(car):
                price_one_car = self.calculate_washing_price(car)
                price_all_car.append(price_one_car)
                car.clean_mark = self.clean_power
        return round(sum(price_all_car), 1)

    def calculate_washing_price(self, car: Car) -> float:
        """Obliczanie kosztu mycia pojedynczego samochodu"""

        dirt_removed = self.clean_power
        base_cost = self.average_rating
        discount = self.distance_from_city_center

        return round(car.comfort_class
                     * (dirt_removed - car.clean_mark)
                     * base_cost
                     / discount, 1)

    def wash_single_car(self, car: Car) -> None | float:
        """Sprawdza pojazd i dopuszcza do mycia"""

        if self.clean_power > car.clean_mark:
            return car.clean_mark

    def rate_service(self, rate: int) -> tuple[int, float]:
        """Ocena myjni"""

        try:
            rate = int(rate)
        except (TypeError, ValueError):
            raise ValueError("Ocene podaj w liczbach")

        if not (1 <= rate <= 5):
            raise ValueError("Oceń w zakresie 1-5")

        self.average_rating = round(((
            self.average_rating * self.count_of_ratings)
            + rate) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
        return self.count_of_ratings, self.average_rating
