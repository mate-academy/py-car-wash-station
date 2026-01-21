from __future__ import annotations


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
            self,
            # CORREÇÃO 1: Parâmetros alterados para corresponder ao script de teste
            comfort_class: int,
            clear_power: int,  # Nome alterado de 'clean_power' para 'clear_power'
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        # CORREÇÃO 2: Atributos armazenados de acordo com os novos parâmetros
        self.comfort_class: int = comfort_class
        self.clear_power: int = clear_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        """Washes the car only if its clean_mark is below clear_power."""
        # CORREÇÃO 3: Usando self.clear_power
        if car.clean_mark < self.clear_power:
            car.clean_mark = self.clear_power

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate the wash price WITHOUT modifying the car.

        CORREÇÃO 4: Nova Fórmula (apenas se for elegível):
            car.comfort_class * self.average_rating
        """
        # CORREÇÃO 5: Usando self.clear_power
        if car.clean_mark >= self.clear_power:
            return 0.0

        # CORREÇÃO 6: Implementando a nova fórmula
        return float(self.comfort_class * self.average_rating)

    def serve_cars(self, cars: list[Car]) -> float:
        """Wash eligible cars, calculating total income and updating clean_mark."""
        total_income: float = 0.0

        for car in cars:
            # O preço DEVE ser computado ANTES da lavagem, conforme o script de teste.
            price = self.calculate_washing_price(car)
            total_income += price

            # Lava o carro (alterando clean_mark)
            self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, mark: int) -> None:
        """Add one new customer's rating and update the average_rating."""
        total_before = self.average_rating * self.count_of_ratings
        new_total = total_before + mark
        self.count_of_ratings += 1
        self.average_rating = round(
            new_total / self.count_of_ratings,
            1
        )