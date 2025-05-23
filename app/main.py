class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        """
        Representa um carro com classe de conforto, nível de limpeza e marca.
        """
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
        """
        Representa uma estação de lavagem de carros com seus atributos principais.
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calcula o custo da lavagem de um carro com base na sujeira, conforto e outros fatores.
        """
        dirt_level = self.clean_power - car.clean_mark
        if self.distance_from_city_center == 0:
            return 0.0  # evita divisão por zero
        price = (
            car.comfort_class * dirt_level * self.average_rating
        ) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Simula a lavagem do carro ajustando seu clean_mark ao clean_power da estação.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Lava todos os carros que estão mais sujos que o clean_power da estação.
        Retorna o total de dinheiro arrecadado.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        """
        Atualiza a média de avaliações com uma nova nota dada.
        """
        total_score = self.average_rating * self.count_of_ratings
        total_score += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
