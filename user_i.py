import matplotlib.pyplot as plt
import mplcursors
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math
import copy

selected_algo = None
radius = 1

#######################################################################
def distance_between_two_points(p1, p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def is_center_valid(center, radius, points_inside_disk):
    for point in points_inside_disk:
        if(distance_between_two_points(center, point) > radius):
            return False
    return True
def my_algo(points):
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
                # candidate_points_covered_by_disc = copy.deepcopy(points_covered_by_disc)
                # save the candidate point
                points_covered_by_disc.append(point_candidate)
                min_x = min(points_covered_by_disc, key = lambda x: x[0])[0]
                max_x = max(points_covered_by_disc, key = lambda x: x[0])[0]

                min_y = min(points_covered_by_disc, key = lambda x: x[1])[1]
                max_y = max(points_covered_by_disc, key = lambda x: x[1])[1]
                
                candidate_center = [(max_x + min_x) / 2 , (max_y + min_y) / 2]

                if(is_center_valid(candidate_center, radius, points_covered_by_disc)):
                    # points_covered_by_disc = points_covered_by_disc
                    best_center_found = candidate_center
                else:
                    points_covered_by_disc.pop()
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
#############################################################################






# Create empty lists to store x and y coordinates
# x_coords = []
# y_coords = []

point_coordinates = []

# Define the plot limits
x_min, x_max = 0, 10  # Set your desired limits for the x-axis
y_min, y_max = 0, 10  # Set your desired limits for the y-axis

# Plot an empty figure
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Prompt the user to click on the plot to select points
print("Click on the plot to select points. Right-click or press Enter to finish input.")

def onclick(event):
    # Check if the user right-clicked or pressed Enter
    if event.button == 3 or event.key == 'enter':
        # Disconnect the click event
        plt.disconnect(cid)
        # Close the plot
        plt.close()
        return

    # Add the clicked coordinates to the lists
    # x_coords.append(event.xdata)
    # y_coords.append(event.ydata)
    if(event.xdata == None or event.ydata == None):
        return
    
    point_coordinates.append([event.xdata, event.ydata])
    # Plot the clicked point
    ax.scatter(event.xdata, event.ydata, color='red')
    plt.draw()



def drawCenters(centers):
    for center in centers:
        circle2 = plt.Circle((center[0],center[1]), radius, color='b', fill=False)
        # plt.plot(center[0],center[1],'r*')
        # plt.text(center[0],center[1]-0.5,'({}, {})'.format(center[0], center[1]))
        ax.add_artist(circle2)

def drawPoints(points):
    for point in points:
        ax.scatter(point[0], point[1], color='red')
    plt.draw()

# Function to handle button click event
def handle_button_click(algo):
    selected_algo = algo
    centers = selected_algo(point_coordinates)
    
    drawCenters(centers)
    label.config(text="Number of discs: " + str(len(centers)))
    
    print("centers")
    print(centers)
    
    plt.draw()
    # Get the text from the textbox
    # text = entry.get()
    
    # Display the text in the console
    # print("Entered text:", text)

def remove_elements():
    ax.cla()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    drawPoints(point_coordinates)

cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Create a Tkinter window
window = tk.Tk()
window.title("Matplotlib with Textbox")
# Create a canvas widget and display the plot
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Create a textbox widget
# entry = tk.Entry(window)
# entry.pack()

# Create a button widget
button = tk.Button(window, text="Brute Force Algorithm", command=lambda: handle_button_click(my_algo))
button2 = tk.Button(window, text="PTAS Algorithm", command=lambda:handle_button_click(GHS))

reset = tk.Button(window, text="Reset", command=lambda:remove_elements())
label = tk.Label(window, text="")


button.pack()
button2.pack()
reset.pack()
label.pack()
# Start the Tkinter event loop
window.mainloop()



plt.xlabel('X')
plt.ylabel('Y')
plt.title('User Input Points')
plt.grid(True)
mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f'({sel.target[0]:.2f}, {sel.target[1]:.2f})'))
# plt.show()

# Print the selected points
for i, (x, y) in enumerate(zip(point_coordinates[0], point_coordinates[1]), start=1):
    print(f"Point {i}: ({x}, {y})")




