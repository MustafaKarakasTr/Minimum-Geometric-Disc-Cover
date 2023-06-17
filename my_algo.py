import math
import time
import matplotlib.pyplot as plt
import numpy as np
import copy
import random
# print(math.sqrt(1/2))
def distance_between_two_points(p1, p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def is_center_valid(center, radius, points_inside_disk):
    for point in points_inside_disk:
        if(distance_between_two_points(center, point) > radius):
            return False
    return True


def my_algo(points):
    temp_radius = 1
    clusters = []
    centers = []
    uncovered_points = sorted(points, key=lambda x: x[0])

    counter = 0

    # run till all the points are covered
    while(0 != len(uncovered_points)):
        # how to cover this point best way possible
        point = uncovered_points[0]

        points_covered_by_disc = [point]
        best_center_found = point

        for j in range(1,len(uncovered_points)):
            point_candidate = uncovered_points[j]
            # print("counter")
            # print(counter)
            counter = counter + 1

            # last possible point is reached. next point's x value is too big to be in the same disc
            if(point_candidate[0] - point[0] > temp_radius * 2):
                break
            # find new center and record if the point_candidate can be covered by the same disc.
            # if the point_candidate can not be covered with the points_covered_by_disc, ignore it 
            else:
                # candidate_points_covered_by_disc = copy.deepcopy(points_covered_by_disc)
                # save the candidate point
                points_covered_by_disc.append(point_candidate)
                min_x = min(points_covered_by_disc, key = lambda x: x[0])[0]
                max_x = max(points_covered_by_disc, key = lambda x: x[0])[0]

                min_y = min(points_covered_by_disc, key = lambda x: x[1])[1]
                max_y = max(points_covered_by_disc, key = lambda x: x[1])[1]
                
                candidate_center = [(max_x + min_x) / 2 , (max_y + min_y) / 2]

                if(is_center_valid(candidate_center, temp_radius, points_covered_by_disc)):
                    # points_covered_by_disc = points_covered_by_disc
                    best_center_found = candidate_center
                else:
                    points_covered_by_disc.pop()
                    # center is not valid, it will try the next point


        # save the best center
        centers.append(best_center_found)
        # save the covered points
        for covered_point in points_covered_by_disc:
            uncovered_points.remove(covered_point)

    return centers

##########################################################
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def GHS(P):
    H = set()
    Disk_Centers = set()
    sqrt_2 = math.sqrt(2)
    sqrt_0_5 = math.sqrt(1/2)
    for p in P:
        v = math.floor(p[0] / sqrt_2)
        h = math.floor(p[1] / sqrt_2)
        # print(v)
        # print(h)
        # print(H)

        if (v, h) in H:
            continue
        elif p[0] >= (sqrt_2 * (v + 1.5) - 1) and ((v + 1, h) in H) and (distance(p, (sqrt_2 * (v + 1) + sqrt_0_5, sqrt_2 * h + sqrt_0_5)) <= 1):
            continue
        elif p[0] <= (sqrt_2 * (v - 0.5) + 1) and ((v - 1, h) in H) and (distance(p, (sqrt_2 * (v - 1) + sqrt_0_5, sqrt_2 * h + sqrt_0_5)) <= 1):
            continue
        elif p[1] >= (sqrt_2 * (h + 1.5) - 1) and ((v, h + 1) in H) and (distance(p, (sqrt_2 * v + sqrt_0_5, sqrt_2 * (h + 1) + sqrt_0_5)) <= 1):
            continue
        elif p[1] <= (sqrt_2 * (h - 0.5) + 1) and ((v, h - 1) in H) and (distance(p, (sqrt_2 * v + sqrt_0_5, sqrt_2 * (h - 1) + sqrt_0_5)) <= 1):
            continue
        else:
            H.add((v, h))
            Disk_Centers.add((sqrt_2 * v + sqrt_0_5, sqrt_2 * h + sqrt_0_5))

    return Disk_Centers
##########################################################

number_of_test = 5

times_taken_by_ghs = []
number_of_discs_ghs = []
times_taken_by_my_algo = []
number_of_discs_my_algo = []

number_of_points_arr = [100,200,500,1000,1500,2000,2000,2500,2500,3000,3000,3500,3500]
for i in range(len(number_of_points_arr)):
    number_of_points = number_of_points_arr[i]
    points = []
    # points = [[-10, -9], [-1, 6], [4, -10], [9, 8]]
    for j in range(number_of_points):
        # x = random.randint(-10,10)
        # y = random.randint(-10,10)
        x = random.uniform(0.0, 50.0)
        y = random.uniform(0.0, 50.0)
        points.append([x,y])
    radius = 1.0
    
    print("points")
    print(points)

    # centers = GHS(points, radius)
    st = time.time()
    centers = GHS(points)#, radius)
    et = time.time()
    print("number_of_points:")
    print(number_of_points)
    print("")

    print("time taken by GHS: ")
    time_dif = et-st
    times_taken_by_ghs.append(time_dif)
    number_of_discs_ghs.append(len(centers))
    print(et-st)

    print("\nCenters:")
    print(centers)
    print("\n")

    st = time.time()
    my_centers = my_algo(points)#, radius)
    et = time.time()
    time_dif = et-st
    times_taken_by_my_algo.append(time_dif)
    number_of_discs_my_algo.append(len(my_centers))
    print("")

    print("time taken by my_algo: ")
    print(et-st)
    print("\nCenters:")
    print(my_centers)
    print("\n")


    # print("centers")
    # print(centers)
    # print("radius")
    # print(radius)

    fig, ax = plt.subplots()
    ax.set_title('Radius: {} Diameter: {}'.format(radius,radius * 2), fontsize=15)
    ax.set_xlim((-0.5, 51))
    ax.set_ylim((-0.5, 51))
    # ax.set_xlim((0, 2))
    # ax.set_ylim((0, 2))
    for point in points:
        plt.plot(point[0],point[1],'ro')
        
    for center in centers:
        circle2 = plt.Circle((center[0],center[1]), radius, color='b', fill=False)
        # plt.plot(center[0],center[1],'r*')
        # plt.text(center[0],center[1]-0.5,'({}, {})'.format(center[0], center[1]))
        ax.add_artist(circle2)

    ax.set_aspect('equal')
    # for circle in circles:
    #     ax.add_artist(circle)
    # plt.show()
    plt.savefig('test_cases/ghs_'+str(i)+'_'+str(number_of_points)+'.png')


    fig, ax = plt.subplots()
    ax.set_title('Radius: {} Diameter: {}'.format(radius,radius * 2), fontsize=15)
    ax.set_xlim((-0.5, 21))
    ax.set_ylim((-0.5, 21))
    for point in points:
        plt.plot(point[0],point[1],'ro')
    for center in my_centers:
        circle2 = plt.Circle((center[0],center[1]), radius, color='g', fill=False)
        # plt.plot(center[0],center[1],'r*')
        # plt.text(center[0],center[1]-0.5,'({}, {})'.format(center[0], center[1]))
        ax.add_artist(circle2)
    ax.set_aspect('equal')
    # for circle in circles:
    #     ax.add_artist(circle)
    # plt.show()
    plt.savefig('test_cases/my_algo_'+str(i)+'_'+str(number_of_points)+'.png')
    
    print("Results:")
    print("Number of points:")
    
    print(number_of_points_arr)

    print("number_of_discs_my_algo")
    print(number_of_discs_my_algo)

    print("number_of_discs_ghs")
    print(number_of_discs_ghs)

    print("Time taken my_algo:")
    print(times_taken_by_my_algo)
    
    print("Time taken GHS:")
    print(times_taken_by_ghs)



    # for point in points:
    #     plt.plot(point[0],point[1],'ro')
    #     plt.text(point[0],point[1]+0.5,'({}, {})'.format(point[0], point[1]))
    # plt.savefig('test_cases/my_plot'+str(i)+'_1.png')
    
    # for center in centers:
    #     plt.plot(center[0],center[1],'r*')
    #     plt.text(center[0],center[1]-0.5,'({}, {})'.format(center[0], center[1]))
    # plt.savefig('test_cases/my_plot'+str(i)+'_2.png')
    
    # for a in range(len(points)):
    #     for b in range(a+1, len(points)):
    #         length_between_two_points = distance_between_two_points(points[a], points[b])
    #         plt.plot([points[a][0],points[b][0]] ,[points[a][1],points[b][1]], marker = 'o')
    #         plt.text((points[a][0]+points[b][0])/2,(points[a][1]+points[b][1])/2+0.5,'{}'.format(round(length_between_two_points,2)))

    
    # plt.savefig('test_cases/my_plot'+str(i)+'_3.png')
