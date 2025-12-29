class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self) -> str:
        return f"Car(comfort_class={self.comfort_class}, clean_mark={self.clean_mark}, brand={self.brand})"


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list[Car]) -> float:
        """this method serve a list of cars and return the total income from washing them"""
        total_income = 0.0
        for car in cars_list:
            if self.clean_power > car.clean_mark:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> None:
        """this method wash a single car and update its clean mark"""
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        """this method calculate the washing price for a single car"""
        cust = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
        ) / self.distance_from_city_center
        return round(cust, 1)

    def rate_service(self, mark: int) -> None:
        """this method update the average rating of the car wash station based on a new mark"""
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += mark
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
