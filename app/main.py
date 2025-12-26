class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, 
                 clean_power: int, 
                 average_rating: int, 
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        dirtiness = self.clean_power - car.clean_mark
        price = (car.comfort_class * dirtiness) * self.average_rating / self.distance_from_city_center
        return round(price, 1)
    
    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)
    
    def rate_service(self, new_rating: float) -> None:
        if not isinstance(new_rating, int):
          raise TypeError("Rating must be an integer.")
        if not (1 <= new_rating <= 10):
          raise ValueError("Rating must be between 1 and 10.")
        total_score = (self.average_rating * self.count_of_ratings + new_rating)
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
        