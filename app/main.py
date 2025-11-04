class Car:
    """Representa um carro com nível de conforto e limpeza."""

    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """Simula uma estação de lava-rápido que calcula e executa lavagens."""

    def __init__(
        self,
        distance_from_city: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city = distance_from_city
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Calcula o preço de lavagem de um carro."""
        if car.clean_mark >= self.clean_power:
            return 0.0
        price = (
            (self.clean_power - car.clean_mark)
            * car.comfort_class
            * self.average_rating
            / self.distance_from_city
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Atualiza o nível de limpeza de um carro."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """Lava uma lista de carros e retorna o lucro total."""
        total_income = 0.0
        for car in cars:
            total_income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        """Adiciona uma nova avaliação ao serviço e recalcula a média."""
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
