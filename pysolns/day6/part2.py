import commons
import math

time_dist_pair = commons.parse(True)

race_time = ""
race_dist = ""
for t, d in time_dist_pair:
    race_time += str(t)
    race_dist += str(d)

race_time = int(race_time)
race_dist = int(race_dist)

def find_edge(time, dist):
    upper = math.ceil((time + math.sqrt(time*time - 4*dist))/2)
    lower = math.floor((time - math.sqrt(time*time - 4*dist))/2)
    return upper-1, lower+1

upper, lower = find_edge(race_time, race_dist)
ans = upper - lower + 1

print(ans)