import math

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        """
        Initializes the Car object with its properties.

        Args:
            comfort_class: The comfort class of the car (1-7).
            clean_mark: The current cleanness mark of the car (1-10).
            brand: The brand of the car.
        """
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        """
        Initializes the CarWashStation object with its properties.

        Args:
            distance_from_city_center: Distance from the city center (1.0-10.0).
            clean_power: The cleanness mark the station can wash to.
            average_rating: The average rating of the station (1.0-5.0).
            count_of_ratings: The number of people who rated the station.
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the washing price for a single car.

        The price is calculated as: comfort_class * (clean_power - clean_mark) * average_rating / distance.

        Args:
            car: An instance of the Car class.

        Returns:
            The calculated washing price, rounded to 1 decimal place.
        """
        if self.clean_power <= car.clean_mark:
            return 0.0

        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car, updating its clean_mark if it's below the station's clean_power.

        Args:
            car: An instance of the Car class.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Washes a list of cars and returns the total income.
        Only cars with a clean_mark below the station's clean_power are washed.

        Args:
            cars: A list of Car instances.

        Returns:
            The total income from washing the cars, rounded to 1 decimal place.
        """
        total_income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        """
        Adds a new rating to the wash station and updates the average rating.

        Args:
            rate: A single new rating (integer).
        """
        current_total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_total_rating = current_total_rating + rate
        self.average_rating = round(new_total_rating / self.count_of_ratings, 1)


# Example usage from the problem description
if __name__ == '__main__':
    bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
    audi = Car(comfort_class=4, clean_mark=9, brand='Audi')
    mercedes = Car(7, 1, 'Mercedes')

    wash_station_1 = CarWashStation(
        distance_from_city_center=5,
        clean_power=6,
        average_rating=3.5,
        count_of_ratings=6
    )

    print("--- Example 1 ---")
    print(f"BMW cleanness before wash: {bmw.clean_mark}")  # 3
    print(f"Audi cleanness before wash: {audi.clean_mark}") # 9
    income_1 = wash_station_1.serve_cars([bmw, audi])
    print(f"Income from the station: {income_1}")  # 6.3
    print(f"BMW cleanness after wash: {bmw.clean_mark}")  # 6
    print(f"Audi cleanness after wash: {audi.clean_mark}") # 9
    print("-" * 20)

    print("--- Example 2 ---")
    bmw_2 = Car(comfort_class=3, clean_mark=3, brand='BMW')
    audi_2 = Car(comfort_class=4, clean_mark=2, brand='Audi')

    wash_station_2 = CarWashStation(
        distance_from_city_center=5,
        clean_power=6,
        average_rating=3.5,
        count_of_ratings=6
    )

    print(f"BMW cleanness before wash: {bmw_2.clean_mark}")  # 3
    print(f"Audi cleanness before wash: {audi_2.clean_mark}") # 2
    income_2 = wash_station_2.serve_cars([bmw_2, audi_2])
    print(f"Income from the station: {income_2}")  # 17.5
    print(f"BMW cleanness after wash: {bmw_2.clean_mark}")  # 6
    print(f"Audi cleanness after wash: {audi_2.clean_mark}") # 6
    print("-" * 20)

    print("--- Example 3 (rate_service) ---")
    wash_station_3 = CarWashStation(
        distance_from_city_center=6,
        clean_power=8,
        average_rating=3.9,
        count_of_ratings=11
    )

    print(f"Average rating before: {wash_station_3.average_rating}")    # 3.9
    print(f"Count of ratings before: {wash_station_3.count_of_ratings}")  # 11

    wash_station_3.rate_service(5)

    print(f"Average rating after: {wash_station_3.average_rating}")    # 4.0
    print(f"Count of ratings after: {wash_station_3.count_of_ratings}")  # 12
    print("-" * 20)

    print("--- Example 4 (complete) ---")
    bmw_4 = Car(3, 3, 'BMW')
    audi_4 = Car(4, 9, 'Audi')
    mercedes_4 = Car(7, 1, 'Mercedes')

    ws_4 = CarWashStation(6, 8, 3.9, 11)

    income_4 = ws_4.serve_cars([
        bmw_4,
        audi_4,
        mercedes_4
    ])

    print(f"Income: {income_4}")
    print(f"Is income correct? {income_4 == 41.7}")
    print(f"BMW cleanness: {bmw_4.clean_mark}")
    print(f"Audi cleanness: {audi_4.clean_mark}")
    print(f"Mercedes cleanness: {mercedes_4.clean_mark}")
    print("-" * 20)

    ford_4 = Car(2, 1, 'Ford')
    wash_cost_4 = ws_4.calculate_washing_price(ford_4)
    print(f"Ford wash cost: {wash_cost_4}")
    print(f"Is wash cost correct? {wash_cost_4 == 9.1}")
    print(f"Ford cleanness: {ford_4.clean_mark}")
    print("-" * 20)
    
    ws_4.rate_service(5)

    print(f"Count of ratings: {ws_4.count_of_ratings}")
    print(f"Average rating: {ws_4.average_rating}")
    print(f"Is ratings count correct? {ws_4.count_of_ratings == 12}")
    print(f"Is average rating correct? {ws_4.average_rating == 4.0}") 

