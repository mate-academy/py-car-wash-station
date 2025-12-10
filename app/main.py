class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        cleaning_capacity: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.cleaning_capacity = cleaning_capacity
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        capacity = self.cleaning_capacity
        calc_price = self.calculate_washing_price
        cars_to_wash = [car for car in cars if car.clean_mark < capacity]
        total_income = sum(calc_price(car) for car in cars_to_wash)
        for car in cars_to_wash:
            self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort_factor = car.comfort_class
        cleaning_difference = self.cleaning_capacity - car.clean_mark
        rating_factor = self.average_rating
        distance_factor = self.distance_from_city_center
        total_factors = comfort_factor * cleaning_difference * rating_factor
        washing_price = total_factors / distance_factor
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.cleaning_capacity

    def rate_service(self, new_rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
