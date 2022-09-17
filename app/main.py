class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income_new = 0
        for brand in cars:
            if brand.clean_mark < self.clean_power:
                income_new += self.calculate_washing_price(brand)
        return round(income_new)

    def calculate_washing_price(self, brand):
        income = (brand.comfort_class
                  * (self.clean_power - brand.clean_mark)
                  * self.average_rating
                  / self.distance_from_city_center)
        return round(income)

    def wash_single_car(self, brand):
        if brand.clean_mark < self.clean_power:
            brand.clean_mark = self.clean_power
        return brand.clean_mark

    def rate_service(self, rate: int):
        new_average_rating = ((self.average_rating
                              * self.count_of_ratings
                              + rate)
                              / (self.count_of_ratings + 1))
        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings = self.count_of_ratings + 1
        return self.average_rating, self.count_of_ratings
