class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = [(position[i], speed[i]) for i in range(n)]

        cars.sort(key=lambda x: x[0])

        stack = []

        for car in cars[::-1]:
            if not stack:
                stack.append(car)
                continue
            
            car_behind = stack[-1]
            
            time_taken_to_reach = (target-car[0])/car[1]

            time_taken_to_reach_car_behind = (target-car_behind[0])/car_behind[1]

            if time_taken_to_reach_car_behind >= time_taken_to_reach:
                stack.pop()
                stack.append((car_behind[0], car_behind[1]))
            else:
                stack.append(car)
        
        return len(stack)
    
"""
cars = [(0, 1), (1, 2), (4, 1)]
target = 10

stack = 
"""