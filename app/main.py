class Car:

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
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

    def calculate_washing_price(self, car: Car) -> float:
        distance = self.distance_from_city_center
        arg_rate = self.average_rating
        power = self.clean_power
        clean_mark = car.clean_mark
        comfort_class = car.comfort_class
        result = (comfort_class * (power - clean_mark) * (arg_rate / distance))
        return round(result, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for element in cars:
            if element.clean_mark < self.clean_power:
                income += self.calculate_washing_price(element)
                self.wash_single_car(element)
        return round(income, 1)

    def rate_service(self, rate: float) -> None:
        avg_rate = self.average_rating
        count_of_rate = self.count_of_ratings
        avg_update = ((avg_rate * count_of_rate + rate) / (count_of_rate + 1))
        self.average_rating = round(avg_update, 1)
        self.count_of_ratings = self.count_of_ratings + 1
