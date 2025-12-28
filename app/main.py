class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be between 1 and 10")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("distance_from_city_center must be between 1.0 and 10.0")

        if clean_power < 1:
            raise ValueError("clean_power must be at least 1")

        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1.0 and 5.0")

        if count_of_ratings < 0:
            raise ValueError("count_of_ratings must be non-negative")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings


    def calculate_washing_price(self, car: Car) -> float:
        price = round(car.comfort_class * max((self.clean_power - car.clean_mark), 0) * self.average_rating / self.distance_from_city_center, 1)
        return price


    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            price = self.calculate_washing_price(car)
            if price > 0:
                income += price
                self.wash_single_car(car)
        return round(income, 1)
            
        


    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power


    def rate_service(self, new_rating: int) -> None:
        if not (1 <= new_rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        self.average_rating = round((self.average_rating * self.count_of_ratings + new_rating) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

