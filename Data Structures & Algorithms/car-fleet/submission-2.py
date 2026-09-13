class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))

        cars.sort()
        mintime = 0
        fleets = 0
        while cars:
            temp = cars.pop()

            time = ((target-temp[0])/temp[1])

            if time > mintime:
                fleets += 1
                mintime = time
        
        return fleets;

        


