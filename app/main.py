class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: int):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
class CarWashStation:
    def __init__(self, distance_from_city_center, clean_capacity, clean_mark, clean_power, average_rating, count_of_ratings):
        clean_capacity = clean_power - clean_mark
        self.distance_from_city_center = distance_from_city_center
        self.clean_mark = clean_mark
        self.clean_power = clean_power
        self.clean_capacity = clean_capacity
        self.average_rating = average_rating\
        self.count_of_ratings = count_of_ratings
    def serve_cars():
        if clean_mark < clean_power:
            result.append(clean_mark)
        else:
            continue
    def calculate_washing_price():
        price_of_washing = comfort_class * clean_capacity * average_rating / count_of_ratings 
    def wash_single_car():
        if clean_mark < clean_power:
            result.append(clean_mark)
        else:
            continue
