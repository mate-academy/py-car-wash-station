class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self):
        return f"Car(brand={self.brand}, comfort_class={self.comfort_class}, clean_mark={self.clean_mark})"


class CarWashStation:
    def __init__(self, station_id, location_id, avg_rating, num_ratings):
        self.station_id = station_id
        self.location_id = location_id
        self.avg_rating = avg_rating
        self.num_ratings = num_ratings
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def __repr__(self):
        return f"CarWashStation(id={self.station_id}, location={self.location_id}, rating={self.avg_rating})"
