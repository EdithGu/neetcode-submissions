class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        expeceted_spending_time = [0] * len(speed) 

        for i, (car_position, car_speed) in enumerate(cars):
            expected = (target-car_position) / car_speed
            expeceted_spending_time[i] = expected

        count_car_fleet = collections.deque() # store expected_spending_time in a monotonically increasing order
        for time in expeceted_spending_time:
            if not count_car_fleet or time > count_car_fleet[-1]:
                count_car_fleet.append(time)
            
        return len(count_car_fleet)

            