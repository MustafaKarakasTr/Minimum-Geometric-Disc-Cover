import math
import matplotlib.pyplot as plt
import numpy as np
import copy

def distance_between_two_points(p1, p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def is_center_valid(center, radius, points_inside_disk):
    for point in points_inside_disk:
        if(distance_between_two_points(center, point) > radius):
            return False
    return True


def circles_covering_points(points, radius):
    clusters = []
    centers = []
    covered_points = []
    points_sorted_by_x = sorted(points, key=lambda x: x[0])
    # uncovered_points = copy.deepcopy(points_sorted_by_x)
    print(points_sorted_by_x)
    # print(uncovered_points)
    # for point in points_sorted_by_x:
    i=0
    # run till all the points are covered
    points_length = len(points)
    while(len(covered_points) != len(points)):
        # how to cover this point best way possible
        point = points_sorted_by_x[0]

        points_covered_by_disc = [point]
        best_center_found = point

        for j in range(1,len(points_sorted_by_x)):
            point_candidate = points_sorted_by_x[j]
            
            # last possible point is reached. next point's x value is too big to be in the same disc
            if(point_candidate[0] - point[0] > radius):
                break
            # find new center and record if the point_candidate can be covered by the same disc.
            # if the point_candidate can not be covered with the points_covered_by_disc, ignore it 
            else:
                candidate_points_covered_by_disc = copy.deepcopy(points_covered_by_disc)
                # save the candidate point
                candidate_points_covered_by_disc.append(point_candidate)
                min_x = min(candidate_points_covered_by_disc, key = lambda x: x[0])[0]
                max_x = max(candidate_points_covered_by_disc, key = lambda x: x[0])[0]

                min_y = min(candidate_points_covered_by_disc, key = lambda x: x[1])[1]
                max_y = max(candidate_points_covered_by_disc, key = lambda x: x[1])[1]
                print("min_x")
                print(candidate_points_covered_by_disc)
                print(min_x)
                print(max_x)
                print(min_y)
                print(max_y)
                
                candidate_center = [(max_x + min_x) / 2 , (max_y + min_y) / 2]
                print(candidate_center)
                if(is_center_valid(candidate_center, radius, candidate_points_covered_by_disc)):
                    points_covered_by_disc = candidate_points_covered_by_disc
                    best_center_found = candidate_center
                # else:
                    # center is not valid, it will try the next point
            

                
                print("radius az verdim girmicek")

        print("b")
        # save the best center
        centers.append(best_center_found)
        # save the covered points
        covered_points = covered_points + points_covered_by_disc
        for covered_point in points_covered_by_disc:
            points_sorted_by_x.remove(covered_point)
        # covered_points.append(points_sorted_by_x[i])
        i = i+1


    print(covered_points)
    return centers


points = [(5,0), (1,0), (0,1), (1,1)]
radius = 2**(1/2)

centers = circles_covering_points(points, radius)
# print(distance_between_two_points((1,0), (1,3)))
# print(is_center_valid((1,1), 4.9, [(4,5)]))
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
