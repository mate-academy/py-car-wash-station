#commiting again beacuse flake8 didnt work couple weeks ago
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
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, number: int) -> None:
        sum_of_ratings = self.count_of_ratings * self.average_rating
        sum_of_ratings += number
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_ratings / self.count_of_ratings, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        res = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                one_car_price = self.calculate_washing_price(car)
                res += one_car_price
                self.wash_single_car(car)
        return round(res, 1)
