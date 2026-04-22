class Car:

    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if comfort_class >= 1 and comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            raise ValueError
        if clean_mark >= 1 and clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            raise ValueError
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        if distance_from_city_center >= 1 and distance_from_city_center <= 10:
            self.distance_from_city_center = distance_from_city_center
        else:
            raise ValueError
        if clean_power >= 1 and clean_power <= 10:
            self.clean_power = clean_power
        else:
            raise ValueError
        if average_rating >= 1 and average_rating <= 5:
            self.average_rating = average_rating
        else:
            raise ValueError
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        return round((car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center),
                     1)

    def rate_service(self, rate_service: int) -> None:
        if rate_service >= 1 and rate_service <= 5:
            self.average_rating = round(((self.average_rating
                                        * self.count_of_ratings + rate_service)
                                         / (self.count_of_ratings + 1)), 1)
            self.count_of_ratings += 1
        else:
            raise ValueError

    def serve_cars(self, cars_list: list[Car]) -> float:
        income: int = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income
