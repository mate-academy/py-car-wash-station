class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> int:
        pass

    def calculate_washing_price(self,
                                comfort_class: int,
                                clean_mark: int
                                ) -> int:
        pass

    def wash_single_car(self,
                        comfort_class: int,
                        clean_mark: int
                        ) -> int:
        pass

    def rate_service(self, rate: int) -> int:
        pass
