import commons
import math

time_dist_pair = commons.parse(True)

def find_edge(time, dist):
    upper = math.ceil((time + math.sqrt(time*time - 4*dist))/2)
    lower = math.floor((time - math.sqrt(time*time - 4*dist))/2)
    return upper-1, lower+1

ans = 1

for time, dist in time_dist_pair:
    upper ,lower = find_edge(time, dist)
    range = upper-lower+1
    ans *= range

print(ans)