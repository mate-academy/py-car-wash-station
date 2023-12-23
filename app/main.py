class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int, average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_car: list) -> int:
        result = 0
        for i in list_car:
            if self.clean_power > i.clean_mark:
                result += self.calculate_washing_price(i)
                self.wash_single_car(i)
        return result

    def calculate_washing_price(self, car: str) -> int:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * (self.average_rating
                        / self.distance_from_city_center), 1)

    def wash_single_car(self, car: str) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, numer: int) -> None:
        result = self.average_rating * self.count_of_ratings
        result1 = result + numer
        self.count_of_ratings += 1
        self.average_rating = round(result1 / self.count_of_ratings, 1)
