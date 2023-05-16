import math
import matplotlib.pyplot as plt
import numpy as np
import copy

def circles_covering_points(points, radius):
    clusters = []
    centers = []
    covered_points = []
    points_sorted_by_x = sorted(points, key=lambda x: x[0])
    uncovered_points = copy.deepcopy(points_sorted_by_x)
    print(points_sorted_by_x)
    print(uncovered_points)

    return centers


points = [(5,0), (1,0), (0,1), (1,1)]
radius = 2**(1/2)

centers = circles_covering_points(points, radius)

print("centers")
print(centers)
# fig, ax = plt.subplots()
# ax.set_xlim((-10, 10))
# ax.set_ylim((-10, 10))
# for point in points:
#     plt.plot(point[0],point[1],'ro')
# for center in centers:
#     circle2 = plt.Circle((center[0],center[1]), radius, color='b', fill=False)
#     ax.add_artist(circle2)

# ax.set_aspect('equal')
# # for circle in circles:
# #     ax.add_artist(circle)
# plt.show()
