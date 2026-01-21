class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> int:

        total_cost = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                single_price = (
                    car.comfort_class
                    * (self.clean_power - car.clean_mark)
                    * self.average_rating
                    / self.distance_from_city_center
                )
                total_cost += single_price
                self.wash_single_car(car=car)

        return round(total_cost, 1)

    def calculate_washing_price(self, car: Car) -> float:

        return round(
            (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
            ), 1
        )

    def wash_single_car(self, car: Car) -> int:

        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rating: int) -> float:
        count_of_marks = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round(
            (count_of_marks + rating)
            / self.count_of_ratings, 1)

        return self.average_rating
