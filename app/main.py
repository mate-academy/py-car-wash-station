class Car:
    def __init__(self, comfort_class, clean_mark, brand):
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
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark
        potential_income = (car.comfort_class
                            * clean_difference
                            * self.average_rating)

        washing_price = potential_income / self.distance_from_city_center
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: int) -> None:
        total_rating_points = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1

        new_average = (total_rating_points + new_rating) / self.count_of_ratings
        self.average_rating = round(new_average, 1)

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])
print(f"Income: {income}")
print(f"BMW Clean: {bmw.clean_mark}")

wash_station_2 = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)
wash_station_2.rate_service(5)
print(f"New Rating: {wash_station_2.average_rating}")
print(f"New Count: {wash_station_2.count_of_ratings}")