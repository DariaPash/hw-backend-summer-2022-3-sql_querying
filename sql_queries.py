TASK_1_QUERY = """
SELECT flight_no, 
       (scheduled_arrival - scheduled_departure) AS duration
FROM flights
ORDER BY duration ASC
LIMIT 5;
"""


TASK_2_QUERY = """
SELECT flight_no, COUNT(*) AS count
FROM flights
GROUP BY flight_no
HAVING COUNT(*) < 50
ORDER BY COUNT(*) DESC
LIMIT 3;
"""


TASK_3_QUERY = """
SELECT COUNT(*) AS count
FROM flights
JOIN airports dep ON flights.departure_airport = dep.airport_code
JOIN airports arr ON flights.arrival_airport = arr.airport_code
WHERE dep.timezone = arr.timezone;
"""
