class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class  # 1–7
        self.clean_mark = clean_mark  # 1–10
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: int | float,
            clean_power: int | float,
            average_rating: int | float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                # calculate cost
                dirtiness = self.clean_power - car.clean_mark
                cost = (car.comfort_class * dirtiness * self.average_rating
                        / self.distance_from_city_center)

                # wash the car
                self.wash_single_car(car)

                income += cost

        return round(income, 1)

    def calculate_washing_price(self, car: object) -> int | float:
        car_wash_cost = 0.0
        car_wash_cost = ((car.comfort_class
                         * (self.clean_power - car.clean_mark)
                         * self.average_rating)
                         / self.distance_from_city_center)
        return round(car_wash_cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round((self.count_of_ratings
                                    * self.average_rating + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
