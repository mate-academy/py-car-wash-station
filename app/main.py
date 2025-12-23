class Car:
    def __init__(
        self: 'Car',
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self: 'CarWashStation',
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(
        self: 'CarWashStation',
        car: Car
    ) -> float:
        difference = self.clean_power - car.clean_mark

        if difference <= 0:
            return 0.0

        cost = (
            car.comfort_class *
            difference *
            self.average_rating /
            self.distance_from_city_center
        )
        return round(cost, 1)

    def wash_single_car(
        self: 'CarWashStation',
        car: Car
    ) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(
        self: 'CarWashStation',
        cars_list: list
    ) -> float:
        income = 0.0

        for car in cars_list:
            price = self.calculate_washing_price(car)
            if price > 0:
                income += price
                self.wash_single_car(car)

        return round(income, 1)

    def rate_service(
        self: 'CarWashStation',
        rate_value: float
    ) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate_value
        self.count_of_ratings += 1

        self.average_rating = round(
            total_rating / self.count_of_ratings,
            1
        )
