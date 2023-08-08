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

    def serve_cars(self, cars_list: list) -> int:
        income = 0
        for served_car in cars_list:
            if served_car.clean_mark < self.clean_power:
                washing_price = self.calculate_washing_price(served_car)
                income += washing_price
                self.wash_single_car(served_car)

        return income

    def calculate_washing_price(self, washed_car: Car) -> float:
        comfort_class = washed_car.comfort_class
        cleaning_operations = (self.clean_power - washed_car.clean_mark)
        relevance = (self.average_rating / self.distance_from_city_center)
        return round(comfort_class * cleaning_operations * relevance, 1)

    def wash_single_car(self, served_car: Car) -> None:
        served_car.clean_mark = self.clean_power

    def rate_service(self, customer_mark: int) -> None:
        total_points = self.average_rating * self.count_of_ratings
        total_points += customer_mark
        self.count_of_ratings += 1
        self.average_rating = round(total_points / self.count_of_ratings, 1)
