class Car:

    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list[Car]) -> float:
        price = 0

        for car in list_cars:
            if self.clean_power > car.clean_mark:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(price, 1)

    def calculate_washing_price(self, car: Car) -> float:

        res = round(car.comfort_class * (self.clean_power - car.clean_mark)
                    * self.average_rating / self.distance_from_city_center, 1)
        return res

    def wash_single_car(self, car: Car) -> None:

        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, sing_rate: int) -> None:
        sum_of_rate = self.count_of_ratings * self.average_rating + sing_rate

        self.count_of_ratings += 1
        self.average_rating = round(sum_of_rate / self.count_of_ratings, 1)
