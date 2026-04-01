class Car:
    def __init__(self, comfort_class, clean_mark, brand) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
    pass


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings)-> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0

        price =(
                car.comfort_class *
                (self.clean_power - car.clean_mark) *
                self.average_rating /
                self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars) -> float:
        total_income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, new_rate) -> None:
        total_score = self.average_rating * self.count_of_ratings
        total_score += new_rate

        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
