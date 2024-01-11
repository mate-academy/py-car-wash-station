class Car:

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        """Takes 3 arguments:
        `comfort_class` - comfort class of a car,  1 -> 7;
        `clean_mark` - car cleanness mark,  1 -> 10;
        `brand` - brand of the car.
        """
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        """Takes 4 arguments:
        `distance_from_city_center` - from 1.0 to 10.0
        `clean_power` to which this car wash station washes 1 -> 10
        `average_rating` - average rating of the station,
              1.0 -> 5.0, rounded to 1 decimal
        `count_of_ratings` - number of people who rated
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_to_serve: list) -> float:
        """Washes cars and collecting money"""

        income = 0
        for car in cars_to_serve:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate price for washing single car"""

        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Washes a single car"""

        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        """Adds a single rate and change average_rating and count_of_ratings"""

        new_average_rating = (self.average_rating
                              * self.count_of_ratings
                              + rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_average_rating, 1)
