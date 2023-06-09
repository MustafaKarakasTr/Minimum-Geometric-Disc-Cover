import math

import matplotlib.pyplot as plt
import numpy as np
import copy
import random
print(math.sqrt(1/2))
def distance_between_two_points(p1, p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def is_center_valid(center, radius, points_inside_disk):
    for point in points_inside_disk:
        if(distance_between_two_points(center, point) > radius):
            return False
    return True


def my_algo(points, radius):
    clusters = []
    centers = []
    covered_points = []
    uncovered_points = sorted(points, key=lambda x: x[0])
    # run till all the points are covered
    while(0 != len(uncovered_points)):
        # how to cover this point best way possible
        point = uncovered_points[0]

        points_covered_by_disc = [point]
        best_center_found = point

        for j in range(1,len(uncovered_points)):
            point_candidate = uncovered_points[j]
            
            # last possible point is reached. next point's x value is too big to be in the same disc
            if(point_candidate[0] - point[0] > radius * 2):
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
                
                candidate_center = [(max_x + min_x) / 2 , (max_y + min_y) / 2]

                if(is_center_valid(candidate_center, radius, candidate_points_covered_by_disc)):
                    points_covered_by_disc = candidate_points_covered_by_disc
                    best_center_found = candidate_center
                # else:
                    # center is not valid, it will try the next point

        # save the best center
        centers.append(best_center_found)
        # save the covered points
        covered_points = covered_points + points_covered_by_disc
        for covered_point in points_covered_by_disc:
            uncovered_points.remove(covered_point)

    return centers

##########################################################
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def GHS(P):
    H = set()
    Disk_Centers = set()

    for p in P:
        v = math.floor(p[0] / math.sqrt(2))
        h = math.floor(p[1] / math.sqrt(2))
        print(v)
        print(h)
        print(H)

        if (v, h) in H:
            continue
        elif p[0] >= (math.sqrt(2) * (v + 1.5) - 1) and ((v + 1, h) in H) and (distance(p, (math.sqrt(2) * (v + 1) + math.sqrt(1/2), math.sqrt(2) * h + math.sqrt(1/2))) <= 1):
            continue
        elif p[0] <= (math.sqrt(2) * (v - 0.5) + 1) and ((v - 1, h) in H) and (distance(p, (math.sqrt(2) * (v - 1) + math.sqrt(1/2), math.sqrt(2) * h + math.sqrt(1/2))) <= 1):
            continue
        elif p[1] >= (math.sqrt(2) * (h + 1.5) - 1) and ((v, h + 1) in H) and (distance(p, (math.sqrt(2) * v + math.sqrt(1/2), math.sqrt(2) * (h + 1) + math.sqrt(1/2))) <= 1):
            continue
        elif p[1] <= (math.sqrt(2) * (h - 0.5) + 1) and ((v, h - 1) in H) and (distance(p, (math.sqrt(2) * v + math.sqrt(1/2), math.sqrt(2) * (h - 1) + math.sqrt(1/2))) <= 1):
            continue
        else:
            H.add((v, h))
            Disk_Centers.add((math.sqrt(2) * v + math.sqrt(1/2), math.sqrt(2) * h + math.sqrt(1/2)))

    return Disk_Centers
##########################################################

number_of_test = 5

for i in range(number_of_test):
    number_of_points = 15
    points = []
    # points = [[-10, -9], [-1, 6], [4, -10], [9, 8]]
    for j in range(number_of_points):
        # x = random.randint(-10,10)
        # y = random.randint(-10,10)
        x = random.uniform(0.0, 4.0)
        y = random.uniform(0.0, 4.0)
        points.append([x,y])
    radius = 1.0

    # centers = GHS(points, radius)
    centers = GHS(points)#, radius)
    my_centers = my_algo(points, radius)#, radius)


    print("centers")
    print(centers)
    print("radius")
    print(radius)

    fig, ax = plt.subplots()
    ax.set_title('Radius: {} Diameter: {}'.format(radius,radius * 2), fontsize=15)
    ax.set_xlim((-0.5, 4.5))
    ax.set_ylim((-0.5, 4.5))
    # ax.set_xlim((0, 2))
    # ax.set_ylim((0, 2))
    for point in points:
        plt.plot(point[0],point[1],'ro')
        
    for center in centers:
        circle2 = plt.Circle((center[0],center[1]), radius, color='b', fill=False)
        # plt.plot(center[0],center[1],'r*')
        # plt.text(center[0],center[1]-0.5,'({}, {})'.format(center[0], center[1]))
        ax.add_artist(circle2)

    for center in my_centers:
        circle2 = plt.Circle((center[0],center[1]), radius, color='g', fill=False)
        # plt.plot(center[0],center[1],'r*')
        # plt.text(center[0],center[1]-0.5,'({}, {})'.format(center[0], center[1]))
        ax.add_artist(circle2)
    ax.set_aspect('equal')
    # for circle in circles:
    #     ax.add_artist(circle)
    # plt.show()
    plt.savefig('test_cases/my_plot'+str(i)+'.png')

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
