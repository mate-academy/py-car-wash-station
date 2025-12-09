class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self) -> str:
        return (f"Car(brand='{self.brand}', comfort_class={self.comfort_class}, "
                f"clean_mark={self.clean_mark})")


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, 
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def __repr__(self) -> str:
        return (f"CarWashStation(clean_power={self.clean_power}, "
                f"rating={self.average_rating}, count={self.count_of_ratings})")

    def calculate_washing_price(self, car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / 
                 self.distance_from_city_center)
        
        return round(price, 1)

    def wash_single_car(self, car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        else:
            return 0.0

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0
        
        for car in cars:
            total_income += self.wash_single_car(car)
            
        return round(total_income, 1)

    def rate_service(self, rate: float) -> None:
        current_sum = self.average_rating * self.count_of_ratings
        new_sum = current_sum + rate
        
        self.count_of_ratings += 1
        
        self.average_rating = round(new_sum / self.count_of_ratings, 1)
