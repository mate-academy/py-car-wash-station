class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center,
                 clean_power, average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        total = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return total

    def calculate_washing_price(self, car):
        return round(car.comfort_class * (
            self.clean_power - car.clean_mark
        ) * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return self.calculate_washing_price(car)

    def rate_service(self, grade: int):
        all_grades = self.count_of_ratings * self.average_rating + grade
        self.count_of_ratings += 1
        self.average_rating = round(all_grades / self.count_of_ratings, 1)
