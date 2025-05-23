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
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calcula o custo da lavagem de um carro, garantindo que o preço
        não seja negativo.
        """
        dirt_level = max(0, self.clean_power - car.clean_mark)
        if self.distance_from_city_center == 0:
            return 0.0  # Evita divisão por zero
        price = (
            car.comfort_class * dirt_level * self.average_rating
        ) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Atualiza o clean_mark do carro se ele estiver mais sujo que
        o clean_power da estação.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Lava todos os carros mais sujos que o clean_power da estação.
        Retorna o valor total ganho com os serviços.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        """
        Atualiza a média de avaliações da estação com uma nova nota.
        """
        total_score = self.average_rating * self.count_of_ratings
        total_score += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(
            total_score / self.count_of_ratings, 1
        )
