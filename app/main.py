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
            distance_from_city_center: int | float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> int:
        income = 0
        for car in car_list:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, mark: Car) -> int | float:
        if mark.clean_mark >= self.clean_power:
            return 0
        price = mark.comfort_class * (self.clean_power - mark.clean_mark)
        price = price * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, mark: Car) -> None:
        if mark.clean_mark < self.clean_power:
            mark.clean_mark = self.clean_power

    def rate_service(self, evaluation: int) -> None:
        rating = (self.average_rating * self.count_of_ratings + evaluation)
        self.count_of_ratings += 1
        self.average_rating = round(rating / self.count_of_ratings, 1)
