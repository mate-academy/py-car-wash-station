from decimal import Decimal, ROUND_HALF_UP


class Car:
    """Representa um carro com suas propriedades."""

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
    """Representa uma estação de lava-rápido e suas operações."""

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    @staticmethod
    def _q10_half_up(value: Decimal) -> Decimal:
        """Arredonda para 1 casa com HALF_UP (0.05 → 0.1)."""
        return value.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

    def _price_decimal(self, car: "Car") -> Decimal:
        """Preço individual como Decimal já arredondado a 0.1 (HALF_UP)."""
        cclass = Decimal(car.comfort_class)
        delta = Decimal(self.clean_power - car.clean_mark)
        rating = Decimal(str(self.average_rating))
        dist = Decimal(str(self.distance_from_city_center))
        raw = (cclass * delta * rating) / dist
        return self._q10_half_up(raw)

    def serve_cars(self, cars: list["Car"]) -> float:
        """
        Lava carros com clean_mark < clean_power e retorna o rendimento total.
        Soma preços individuais já arredondados com Decimal.
        """
        total = Decimal("0.0")
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self._price_decimal(car)
                total += price
                self.wash_single_car(car)
        return float(self._q10_half_up(total))

    def calculate_washing_price(self, car: "Car") -> float:
        """
        Custo de lavagem para um carro
        (retorna float, mas arredondado correto).
        """
        return float(self._price_decimal(car))

    def wash_single_car(self, car: "Car") -> None:
        """Atualiza a clean_mark para o poder de limpeza da estação."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        """Recalcula a média com uma nova avaliação."""
        current_total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_average_rating = (
            current_total_rating + new_rate
        ) / self.count_of_ratings
        self.average_rating = float(
            Decimal(str(new_average_rating)).quantize(
                Decimal("0.1"),
                rounding=ROUND_HALF_UP,
            )
        )
