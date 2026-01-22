class Car:
    def __init__(self,
                 comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        total = 0
        for i in car_list:
            if self.clean_power > i.clean_mark:
                price = self.calculate_washing_price(i)
                self.wash_single_car(i)
                total += price
        return total

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        calc = 0
        calc = self.count_of_ratings * self.average_rating + rate
        self.count_of_ratings += 1
        calc /= self.count_of_ratings
        self.average_rating = round(calc, 1)
