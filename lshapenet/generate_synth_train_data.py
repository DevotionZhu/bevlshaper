# Import dependencies
import numpy as np

import cv2
import numpy as np

# Create blank image
def create_blank(width, height, rgb_color=(255, 255, 255)):
    image = np.zeros((height, width, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    return image

# Constants
MAP_WIDTH = 1000
SENSOR_POSITION = (round(MAP_WIDTH) / 2, 0)
NUMBER_OF_VEHICLES_MEAN, NUMBER_OF_VEHICLES_STD = 8.0, 5.0
VEHICLE_LENGTH_MEAN, VEHICLE_LENGTH_STD = 4.2, 0.8
VEHICLE_WIDTH_MEAN, VEHICLE_WIDTH_STD = 1.8, 0.3
VEHICLE_ANGLE_MEAN, VEHICLE_ANGLE_STD = 90.0, 0.8

# Init empty image
img = create_blank(MAP_WIDTH, MAP_WIDTH)

# Randomly manipulate number of vehicles
# TODO ADD NOISE
number_of_vehicles = int(max(1, np.round(np.random.uniform(NUMBER_OF_VEHICLES_MEAN, NUMBER_OF_VEHICLES_STD, 1)))[0])

# Create one vehicle per iteration
for i in range(number_of_vehicles):
    # Set first point and calculate all other vehicle parameters
    p1 = np.asarray([np.random.uniform(0.0, MAP_WIDTH, 1), np.random.uniform(0.0, MAP_WIDTH, 1)]
    vehicle_length = np.random.normal(VEHICLE_LENGTH_MEAN, VEHICLE_LENGTH_STD, 1)
    vehicle_width = np.random.normal(VEHICLE_WIDTH_MEAN, VEHICLE_WIDTH_STD, 1)
    vehicle_angle = np.random.normal(VEHICLE_ANGLE_MEAN, VEHICLE_ANGLE_STD, 1)

    # Calculate all other points
    p2 = [p1 + vehicle_length * np.cos(vehicle_angle), p1 + vehicle_length * np.sin(vehicle_angle)]
    p3 = [p1 + vehicle_width * np.sin(vehicle_angle), p1 + vehicle_width * np.cos(vehicle_angle)]
    p4 = [p2 + vehicle_width * np.sin(vehicle_angle), p2 + vehicle_width * np.cos(vehicle_angle)]

    # Draw rectangle
    cv2.rectangle(img, p1, p4, color=(255, 20, 20), thickness=3)

# Show results
cv2.imshow("Results", img)
cv2.waitKey(0)