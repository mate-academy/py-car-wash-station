class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


    def serve_cars(self, car_list):
        filter_list = [car for car in car_list if car.clean_mark > self.clean_power]
        result = []
        for car in filter_list:
            result.append(self.calculate_washing_price(car))
        return sum(result)

    
    def calculate_washing_price(self, car): 
        result = (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center)
        return round(result, 1) 
        
    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
    
    def rate_service(self, new_rating):
        self.count_of_ratings += 1
        total_rating = self.average_rating * (self.count_of_ratings - 1)
        self.average_rating = round((total_rating + new_rating) / self.count_of_ratings, 1)


bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

car_station = CarWashStation(6, 8, 3.9, 11)

print(car_station.serve_cars([bmw, audi, mercedes]))
print(car_station.average_rating)
car_station.rate_service(5)
print(car_station.average_rating)