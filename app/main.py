class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> Car:
        """Calcula o preço de lavagem sem alterar o carro."""
        if car.clean_mark >= self.clean_power:
            return 0
        cleaning_needed = self.clean_power - car.clean_mark
        price = ((car.comfort_class * cleaning_needed * self.average_rating)
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> Car:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: Car) -> Car:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, mark: int) -> int:
        """Atualiza a avaliação média com nova nota."""
        total_score = self.average_rating * self.count_of_ratings
        total_score += mark
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
