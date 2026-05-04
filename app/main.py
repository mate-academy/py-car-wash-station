class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(
        self,
        single_car_object: Car,
    ) -> float:
        price = (
            single_car_object.comfort_class
            * (self.clean_power - single_car_object.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def serve_cars(
        self,
        list_objects_class_car: list[Car],
    ) -> float:
        income = 0.0

        for car_object in list_objects_class_car:
            if car_object.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car_object)
                self.wash_single_car(car_object)

        return round(income, 1)

    def wash_single_car(
        self,
        single_car_object: Car,
    ) -> None:
        if single_car_object.clean_mark < self.clean_power:
            single_car_object.clean_mark = self.clean_power

    def rate_service(
        self,
        number_rating: float,
    ) -> None:
        total_rating = (
            self.average_rating * self.count_of_ratings
            + number_rating
        )

        self.count_of_ratings += 1
        self.average_rating = round(
            total_rating / self.count_of_ratings,
            1,
        )
