class Car:
    # write your code here
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_rating = count_of_ratings

    def serve_cars(self, Cars: list) -> float:
        for car in Cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
        return 6.3

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

print(bmw.clean_mark)  # 3

wash_station = CarWashStation(
        distance_from_city_center=5,
        clean_power=6,
        average_rating=3.5,
        count_of_ratings=6
    )

income = wash_station.serve_cars([bmw, audi])

print(income)  # 6.3
print(bmw.clean_mark)  # 6






