class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if not isinstance(comfort_class, int):
            raise TypeError("comfort_class must be an int")
        if not isinstance(clean_mark, int):
            raise TypeError("clean_mark must be an int")
        if not isinstance(brand, str):
            raise TypeError("brand must be an str")
        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("comfort_class must be between 1 and 7")
        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("clean_mark must be between 1 and 10")

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
        if not isinstance(distance_from_city_center, (float, int)):
            raise TypeError("distance must be an float or int")
        if not isinstance(clean_power, int):
            raise TypeError("clean power must be an int")
        if not isinstance(average_rating, (float, int)):
            raise TypeError("rating must be an float or int")
        if not isinstance(count_of_ratings, int):
            raise TypeError("count must be an int")
        if clean_power < 1.0 or clean_power > 10:
            raise ValueError("clean power must be between 1.0 and 10")
        if distance_from_city_center < 1.0 or distance_from_city_center > 10.0:
            raise ValueError("distance must be between 1.0 and 10")
        if average_rating < 1.0 or average_rating > 5.0:
            raise ValueError("rating must be between 1.0 and 5.0")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark
        rate = self.average_rating / self.distance_from_city_center
        calculated_price = car.comfort_class * difference * rate
        return round(calculated_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        cash = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                calculated_price = self.calculate_washing_price(car)
                cash += calculated_price
                self.wash_single_car(car)
        return round(cash, 1)

    def rate_service(self, rating: float) -> None:
        old_avg = self.average_rating
        old_count = self.count_of_ratings
        total_before = old_avg * old_count
        total_after = total_before + rating
        new_count = old_count + 1
        new_avg = total_after / new_count
        new_avg = round(new_avg, 1)
        self.average_rating = new_avg
        self.count_of_ratings = new_count
