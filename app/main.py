class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> float:
        income_list = []
        for car in list_of_cars:
            if self.can_serve(car):
                washing_price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                income_list.append(washing_price)
        return round(sum(income_list), 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark

        raw_price = car.comfort_class * clean_difference * self.average_rating
        normalized_price = raw_price / self.distance_from_city_center

        return round(normalized_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.can_serve(car):
            car.clean_mark = self.clean_power

    def rate_service(self, user_rating: int) -> None:
        self.average_rating = self.calculate_average_rating(user_rating)
        self.count_of_ratings += 1

    def calculate_average_rating(self, user_rating: int) -> float:
        previous_total_score = self.average_rating * self.count_of_ratings
        new_total_score = previous_total_score + user_rating

        updated_rating_count = self.count_of_ratings + 1

        new_average_rating = new_total_score / updated_rating_count

        return round(new_average_rating, 1)

    def can_serve(self, car: Car) -> bool:
        if self.clean_power > car.clean_mark:
            return True
        return False
