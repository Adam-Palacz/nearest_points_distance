import numpy as np
import random
from numpy import linalg as LA


# getting the quantity of dimension from the user
def dimension_quantity():
    # input validation
    try:
        quantity = int(input("Input quantity of dimensions:"))
    except ValueError:
        print("Wrong number")
        return dimension_quantity()
    if quantity < 1:
        print("Number can't be smaller than 1")
        return dimension_quantity()
    return quantity


# getting the quantity of points from the user
def points_quantity():
    # input validation
    try:
        quantity = int(input("Input quantity of points:"))
    except ValueError:
        print("Wrong number")
        return points_quantity()
    if quantity < 1:
        print("Number can't be smaller than 1")
        return points_quantity()
    return quantity


# getting points x and y coordinates
def points_list(dimensions = dimension_quantity(), quantity=points_quantity()):
    coordinates = []

    for point in range(quantity):
        points = []
        for dimension in range(dimensions):

            # input validation
            try:
                coordinate = float(input(f"Input point {point + 1}_{dimension + 1} coordinate: "))
            except ValueError:
                print("Wrong number")
                return points_list()
            points.append(coordinate)
        point_tuple = tuple(points)
        # add coordinates as tuple to list
        coordinates.append(point_tuple)
    return coordinates


# calculation distances between points
def points_distance():
    # user points coordinates
    coordinates = points_list()
    # random start point
    point = random.choice(coordinates)
    # list for all distances between points
    distances_list = []

    while True:
        point_index = coordinates.index(point)
        # deleting the selected points from the coordinates list
        coordinates.pop(point_index)

        # change the selected point and the coordinates list of the rest points to NumPy array
        point_array = np.array(point)
        coordinates_array = np.array(coordinates)
        # list with the distances between the selected point and the rest points
        points_distance = [LA.norm(point_array - coordinates_array[i]) for i in range(len(coordinates))]

        # select minimum distance from the list
        min_distance = min(points_distance)
        # if there are more points at the same distance, we choose one at random
        min_distance_index = np.where(points_distance == min_distance)[0]
        if len(min_distance_index) > 1:
            min_distance_index = random.choice(min_distance_index)
        else:
            min_distance_index = min_distance_index[0]

        # add distance to list
        distances_list.append(min_distance)

        # if there is only one point left in the list, the loop breaks
        if len(coordinates) == 1:
            break

        # selecting the closest point as our next base point
        point = coordinates[min_distance_index]

    # final distance is the sum of all calculated distances
    final_distance = round(sum(distances_list), 2)
    return f"final distance: {final_distance}"


if __name__ == "__main__":
    print(points_distance())
