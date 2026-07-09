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
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Calcula o custo usando a fórmula e retorna arredondado."""
        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float | None:
        """Lava um carro se clean_power > clean_mark.

        Atualiza clean_mark e retorna o custo.
        """
        if car.clean_mark < self.clean_power:
            cost = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return cost
        return None  # não contribui para a renda

    def serve_cars(self, cars: list[Car]) -> float:
        """Lava os carros elegíveis e retorna a renda total."""
        total_income = 0.0
        for car in cars:
            cost = self.wash_single_car(car)
            if cost is not None:
                total_income += cost
        return round(total_income, 1)

    def rate_service(self, new_rate: int) -> None:
        """Adiciona uma nova avaliação e atualiza a média."""
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + new_rate)
            / self.count_of_ratings,
            1
        )
