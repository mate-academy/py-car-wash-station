class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, brand: Car) -> float:
        cost = (brand.comfort_class
                * (self.clean_power - brand.clean_mark)
                * self.average_rating / self.distance_from_city_center)
        return round(cost, 1)

    def wash_single_car(self, brand: Car) -> None:
        if self.clean_power > brand.clean_mark:
            brand.clean_mark = self.clean_power

    def serve_cars(self, brands_car: list) -> float:
        income = 0
        for brand in brands_car:
            if brand.clean_mark < self.clean_power:

                income += self.calculate_washing_price(brand)
                self.wash_single_car(brand)
        return round(income, 1)

    def rate_service(self, rate_service: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate_service)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
