[1mdiff --git a/README.md b/README.md[m
[1mindex 906a089..21be5de 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -2,16 +2,16 @@[m
 [m
 Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.[m
 [m
[31m-You own a car washing station. Washing cost calculation [m
[32m+[m[32mYou own a car washing station. Washing cost calculation[m
 takes a lot of time, and you decide to automate this[m
[31m-calculation. The washing cost will depend on car comfort [m
[32m+[m[32mcalculation. The washing cost will depend on car comfort[m
 class, car cleanness degree, wash station average rating[m
 and wash station distance from the center of the city.[m
 [m
 Create class `Car`, its `__init__` method takes and stores[m
 3 arguments:[m
 1. `comfort_class` - comfort class of a car, from 1 to 7[m
[31m-2. `clean_mark` - car cleanness mark, from very [m
[32m+[m[32m2. `clean_mark` - car cleanness mark, from very[m
 dirty - 1 to absolutely clean - 10[m
 3. `brand` - brand of the car[m
 [m
[36m@@ -25,10 +25,10 @@[m [mwashes (yes, not all stations can clean your car completely)[m
 from 1.0 to 5.0, rounded to 1 decimal[m
 4. `count_of_ratings` - number of people who rated[m
 [m
[31m-`CarWashStation` should have such methods: [m
[32m+[m[32m`CarWashStation` should have such methods:[m
 1. `serve_cars` - method, that takes a list of `Car`'s, washes only[m
 cars with `clean_mark` < `clean_power` of wash station[m
[31m-and returns income of `CarWashStation` for serving this list of Car's, [m
[32m+[m[32mand returns income of `CarWashStation` for serving this list of Car's,[m
 rounded to 1 decimal:[m
 [m
 ```python[m
[36m@@ -78,15 +78,15 @@[m [mprint(bmw.clean_mark)  # 6[m
 print(audi.clean_mark) # 6[m
 ```[m
 [m
[31m-2. `calculate_washing_price` - method, that calculates cost for a [m
[32m+[m[32m2. `calculate_washing_price` - method, that calculates cost for a[m
 single car wash,[m
 cost is calculated as: car's comfort class * difference between[m
[31m-wash station's clean power and car's clean mark * car wash station [m
[31m-rating / car wash station [m
[31m-distance to the center of the city, returns number rounded [m
[32m+[m[32mwash station's clean power and car's clean mark * car wash station[m
[32m+[m[32mrating / car wash station[m
[32m+[m[32mdistance to the center of the city, returns number rounded[m
 to 1 decimal;[m
[31m-3. `wash_single_car` - method, that washes a single car, so it should [m
[31m-have `clean_mark` equals wash station's `clean_power`, if [m
[32m+[m[32m3. `wash_single_car` - method, that washes a single car, so it should[m
[32m+[m[32mhave `clean_mark` equals wash station's `clean_power`, if[m
 `wash_station.clean_power` is greater than `car.clean_mark`;[m
 4. `rate_service` - method that adds a single rate to the wash station, and based on this single rate[m
 `average_rating` and `count_of_ratings` should be changed:[m
[36m@@ -127,16 +127,16 @@[m [mincome = ws.serve_cars([[m
 income == 41.7[m
 [m
 bmw.clean_mark == 8[m
[31m-audi.clean_mark == 9  [m
[32m+[m[32maudi.clean_mark == 9[m
 mercedes.clean_mark == 8[m
 # audi wasn't washed[m
 # all other cars are washed to '8'[m
 [m
 ford = Car(2, 1, 'Ford')[m
[31m-wash_cost = ws.calculate_washing_price(ford)  [m
[32m+[m[32mwash_cost = ws.calculate_washing_price(ford)[m
 # only calculating cost, not washing[m
 wash_cost == 9.1[m
[31m-ford.clean_mark == 1 [m
[32m+[m[32mford.clean_mark == 1[m
 [m
 ws.rate_service(5)[m
 [m
