class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars based in their positions
        data = [ ( position[i], speed[i]) for i in range(len(position))]
        sorted_data = sorted(data, key = lambda x: x[0], reverse = True)

        stack = []

        for i in range(len(position)):
            cur_fleet = sorted_data[i]
            if not stack:
                stack.append(cur_fleet)
                continue
            front_fleet =  stack[-1] #stack.peek()
            front_fleet_arrival_time = (target - front_fleet[0]) / front_fleet[1]
            cur_fleet_arrival_time = (target - cur_fleet[0]) / cur_fleet[1]

            if cur_fleet_arrival_time > front_fleet_arrival_time:
                stack.append(cur_fleet)
        return len(stack)