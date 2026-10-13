class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        # comfort class of a car, from 1 to 7
        self.comfort_class = comfort_class
        #
        # car cleanness mark, from very dirty - 1 to absolutely clean - 10
        self.clean_mark = clean_mark
        #
        # brand of the car
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        # how far station from the city center, from 1.0 to 10.0
        self.distance_from_city_center = distance_from_city_center
        #
        # `clean_mark` to which this car wash station washes
        self.clean_power = clean_power
        #
        # average rating of the station, from 1.0 to 5.0, rounded to 1 decimal
        self.average_rating = average_rating
        #
        # number of people who rated
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        # washes only cars with `clean_mark` < `clean_power` of wash station
        # and returns d(1) income of `CarWashStation` for serving this list
        #
        # initialize return
        ret_income = 0.0
        if not cars:
            return ret_income
        for car in cars:
            if car.clean_mark < self.clean_power:
                ret_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return ret_income

    def calculate_washing_price(self, car: Car) -> float:
        # method, that calculates cost for a single car wash,
        # cost is calculated as:
        # car's comfort class *
        # difference between wash station's clean power and car's clean mark *
        # car wash station rating /
        # car wash station distance to the center of the city,
        # returns number rounded to 1 decimal
        retval = round(
            (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
            )
            / self.distance_from_city_center,
            1
        )
        return retval

    def wash_single_car(self, car: Car) -> None:
        # method, that washes a single car, so it should
        # result with `clean_mark` equals wash station's `clean_power`,
        # if `wash_station.clean_power` is greater than `car.clean_mark`
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        # method that adds a single rate to the wash station's weighted
        # average and based on this single rate
        # `average_rating` and `count_of_ratings` should be changed:
        #
        # Calculate the cumulative point pool before updating the count
        total_points = self.average_rating * self.count_of_ratings
        #
        # Increment the total review headcount by 1
        self.count_of_ratings += 1
        #
        # Calculate the new average including the new score
        raw_average = (total_points + new_rating) / self.count_of_ratings
        #
        # Save the result back to the attribute, rounded to 1 decimal place
        self.average_rating = round(raw_average, 1)
