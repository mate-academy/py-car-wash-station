class Car:
    def __init__(self, comfort_class , clean_mark , brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center , clean_power , average_rating , count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


    def serve_cars(self,cars):
        total = 0.0
        for car in cars:
            price = self.calculate_washing_price(car)
            if car.clean_mark < self.clean_power:
                total += price
                self.wash_single_car(car)
        return round(total, 1)

    def calculate_washing_price(self, car):
        value = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return round(value, 1)


    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        service_avg = (self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        average_rating = round(service_avg, 1)
        return average_rating



bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=2, brand='Audi')

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])
print(income)       # 6.3
print(bmw.clean_mark)  # 6
print(audi.clean_mark) #
