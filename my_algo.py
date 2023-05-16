import math
import matplotlib.pyplot as plt
import numpy as np
import copy

# def distance(x1, y1, x2, y2):
#     return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# def circle_center(points):
#     if len(points) == 1:
#         return points[0]

#     x_coords, y_coords = zip(*points)
#     mean_x = sum(x_coords) / len(points)
#     mean_y = sum(y_coords) / len(points)

#     def distance_from_mean(p):
#         return distance(p[0], p[1], mean_x, mean_y)

#     max_distance = max(distance_from_mean(p) for p in points)
#     if max_distance <= radius:
#         return (mean_x, mean_y)

#     best_center = None
#     best_radius = float('inf')
#     for i in range(len(points)):
#         for j in range(i+1, len(points)):
#             p1 = points[i]
#             p2 = points[j]
#             center_x = (p1[0] + p2[0]) / 2
#             center_y = (p1[1] + p2[1]) / 2
#             center_distance = distance_from_mean((center_x, center_y))
#             if center_distance <= radius:
#                 circle_radius = distance(center_x, center_y, p1[0], p1[1])
#                 if circle_radius < best_radius:
#                     best_center = (center_x, center_y)
#                     best_radius = circle_radius

#     if best_center is not None:
#         return best_center

#     return (mean_x, mean_y)

def circles_covering_points(points, radius):
    clusters = []
    centers = []
    covered_points = []
    points_sorted_by_x = sorted(points, key=lambda x: x[0])
    uncovered_points = copy.deepcopy(points_sorted_by_x)
    print(points_sorted_by_x)
    print(uncovered_points)

    # for point in 
    # for point in points:
    #     assigned = False
    #     for cluster in clusters:
    #         if distance(point[0], point[1], cluster[0][0], cluster[0][1]) <= radius:
    #             cluster.append(point)
    #             assigned = True
    #             break
    #     if not assigned:
    #         clusters.append([point])

    # centers = []
    # for cluster in clusters:
    #     center = circle_center(cluster)
    #     centers.append(center)

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
