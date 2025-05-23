class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class  # from 1 to 7
        self.clean_mark = clean_mark  # very dirty - 1, absolutely clean - 10
        self.brand = brand  # brand of the car


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,  # from 1.0 to 10.0
        clean_power: int,  # (cars with clean_mark < clean_power
                           # can be washed).
        average_rating: float,  # from 1.0 to 5.0, rounded to 1 decimal
        count_of_ratings: int,  # number of people who rated
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> float:
        if not (1.0 <= rating <= 5.0):
            return self.average_rating

        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (total_rating + rating) / self.count_of_ratings, 1)
        return self.average_rating


ford = Car(2, 1, "Ford")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")

print(ford.clean_mark)

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([ford, audi])

print(income)
print(ford.clean_mark)
