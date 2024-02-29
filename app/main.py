class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) \
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, brands: list) -> int:
        price = brands.comfort_class * (self.clean_power - brands.clean_mark) \
            * self.average_rating / self.distance_from_city_center
        return price

    def wash_single_car(self, brands: list) -> None:
        if self.clean_power > brands.clean_mark:
            brands.clean_mark = self.clean_power

    def serve_cars(self, brands: list) -> float:
        income = round(sum([self.calculate_washing_price(brand) for brand in
                       brands if brand.clean_mark < self.clean_power]), 1)
        [self.wash_single_car(brand) for brand in brands]
        return income

    def rate_service(self, mark: int) -> None:
        self.average_rating = round((self.average_rating
                                    * self.count_of_ratings + mark)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
