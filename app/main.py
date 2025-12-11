"""
The washing cost will depend on car comfort class, car cleanness degree, wash
station average rating and wash station distance from the center of the city.

Create class `Car`, its `__init__` method takes and stores 3 arguments:

    1. `comfort_class` - comfort class of a car,
        from 1 to 7
    2. `clean_mark` - car cleanness mark,
        from very dirty - 1 to absolutely clean - 10
    3. `brand` - brand of the car

"""


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.brand = brand
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark


"""
Create class `CarWashStation`, its `__init__` method takes and stores 4
arguments:

    1. `distance_from_city_center` - how far station
        from the city center, from 1.0 to 10.0
    2. `clean_power` - `clean_mark` to which this car wash station washes (yes,
        not all stations can clean your car completely)
    3. `average_rating` - average rating of the station,
        from 1.0 to 5.0, rounded to 1 decimal
    4. `count_of_ratings` - number of people who rated
"""


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

    def serve_cars(self, list_of_cars: list) -> float:
        """
        Maintains the list of machines and returns the total cost of the car
        wash.
        """
        total_income = 0
        if isinstance(list_of_cars, Car):
            return self.wash_single_car(list_of_cars)
        for car in list_of_cars:
            total_income += self.wash_single_car(car)
        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the cost of a car wash for a specific machine.
        """
        result = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(result, 1)

    def wash_single_car(self, car: Car) -> float:
        """
        Maintains the list of machines and washes one machine if the station
        capacity is greater.
        """
        if self.clean_power > car.clean_mark:
            result = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return result
        return 0.0

    def rate_service(self, rating: float) -> None:
        """
        Updates the average rating of the station after a new rating.
        """
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
