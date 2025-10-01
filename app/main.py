class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class      # 1–7
        self.clean_mark = clean_mark            # 1–10
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center  # 1.0–10.0
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)              # 1.0–5.0
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate washing price for a single car"""
        price = (car.comfort_class *
                 (self.clean_power - car.clean_mark) *
                 self.average_rating /
                 self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        """Wash one car if possible, update its cleanness and return price earned"""
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power  # washed up to station's capacity
            return price
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        """Wash multiple cars and return total income"""
        total_income = 0.0
        for car in cars:
            total_income += self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: float) -> None:
        """Add a new rating and update average rating"""
        total_score = self.average_rating * self.count_of_ratings
        total_score += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
