class Car:
    def __init__(self, comfort_class: int, clean_mark: float,
                 brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class має бути в межах від 1 до 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark має бути в межах від 1 до 10")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: int) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("distance має бути в межах від 1.0 до 10.0")
        if not (1.0 <= clean_power <= 10.0):
            raise ValueError("clean_power має бути в межах від 1.0 до 10.0")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating має бути в межах від 1.0 до 5.0")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings
        self.wash_price = None

    def serve_cars(self, cars: list) -> int:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += washing_price
        return round(total_income, 1)

    def calculate_washing_price(self, car: object) -> int:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: object) -> str:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            print("Автомобіль помитий до рівня:", self.clean_power)
        else:
            print("Автомобіль вже чистіший або на тому ж рівні.")

    def rate_service(self, new_rating: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            ((self.average_rating * (self.count_of_ratings - 1))
             + new_rating) / self.count_of_ratings, 1
        )
