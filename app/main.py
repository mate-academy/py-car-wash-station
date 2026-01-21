class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: int) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: int, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_car: list[Car]) -> float:
        profit = 0
        for car in list_car:
            if car.clean_mark < self.clean_power:
                profit += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(profit, 1)

    def calculate_washing_price(self, car: Car) -> float:
        result = round(car.comfort_class
                       * (self.clean_power - car.clean_mark)
                       * (self.average_rating
                          / self.distance_from_city_center), 1)
        return result

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, evaluation: int) -> None:
        sum_current_rating = self.average_rating * self.count_of_ratings
        sum_rating_new = sum_current_rating + evaluation
        count_ratings_new = self.count_of_ratings + 1
        self.count_of_ratings = count_ratings_new
        self.average_rating = round(sum_rating_new / count_ratings_new, 1)
