class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        if not 1 <= comfort_class <= 7:
            raise ValueError("comfort_class must be between 1 and 7")
        if not 1 <= clean_mark <= 10:
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
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = max(1.0, min(10.0, distance_from_city_center))
        self.clean_power = clean_power
        self.average_rating = round(max(1.0, min(5.0, average_rating)), 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                self.wash_single_car(car)
                price = self.calculate_washing_price(car)
                total_income += price
                print(f"Washing {car.brand}: Price = {price}, New Clean Mark = {car.clean_mark}")
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            price = (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
            )
            return round(price, 1)
        return 0.0

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1