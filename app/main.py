class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: int) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(
            self,
            cars: list) -> None:
        return self.calculate_washing_price(
            [car_to_wash for car_to_wash in cars
             if car_to_wash.clean_mark < self.clean_power])

    def calculate_washing_price(
            self,
            cars: list) -> None:
        result = 0
        if type(cars) is list:
            for car_to_wash in cars:
                if car_to_wash.clean_mark < self.clean_power:
                    result += round((car_to_wash.comfort_class
                                     * (self.clean_power
                                        - car_to_wash.clean_mark)
                                     * self.average_rating
                                     / self.distance_from_city_center), 1)
                self.wash_single_car(car_to_wash)
        return result

    def wash_single_car(
            self,
            cars: list) -> None:
        cars.clean_mark = self.clean_power

    def rate_service(
            self,
            rate: float) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
