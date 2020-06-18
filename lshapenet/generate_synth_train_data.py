# Import dependencies
import cv2
import numpy as np

# Derive constants
DEG_TO_RAD = np.pi / 180

# Create blank image
def create_blank(width, height, rgb_color=(255, 255, 255)):
    image = np.zeros((height, width, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    return image

# Constants
MAP_WIDTH = 100
METER_TO_PIXEL = 10

NUMBER_OF_VEHICLES_MEAN, NUMBER_OF_VEHICLES_STD = 5.0, 0.0
VEHICLE_LENGTH_MEAN, VEHICLE_LENGTH_STD = 4.2, 0.2
VEHICLE_WIDTH_MEAN, VEHICLE_WIDTH_STD = 1.8, 0.3
VEHICLE_ANGLE_MEAN, VEHICLE_ANGLE_STD = 90.0 * DEG_TO_RAD, 0.05

# Determine sensor position
sensor_position = (round(MAP_WIDTH) / 2, 0)

# Init empty image
img = create_blank(MAP_WIDTH * METER_TO_PIXEL, MAP_WIDTH * METER_TO_PIXEL)

# Randomly manipulate number of vehicles
# TODO ADD NOISE
number_of_vehicles = int(max(1, np.round(np.random.uniform(NUMBER_OF_VEHICLES_MEAN, NUMBER_OF_VEHICLES_STD, 1))))

# Create one vehicle per iteration
for i in range(number_of_vehicles):
    # Set first point and calculate all other vehicle parameters
    p1 = np.around(np.random.uniform(0.0, MAP_WIDTH, (2))).astype(np.int32) * METER_TO_PIXEL
    vehicle_length = np.random.normal(VEHICLE_LENGTH_MEAN, VEHICLE_LENGTH_STD, 1) * METER_TO_PIXEL
    vehicle_width = np.random.normal(VEHICLE_WIDTH_MEAN, VEHICLE_WIDTH_STD, 1) * METER_TO_PIXEL
    vehicle_angle = np.random.normal(VEHICLE_ANGLE_MEAN, VEHICLE_ANGLE_STD, 1)

    # Calculate all other points
    p2 = p1 + np.around(np.asarray([vehicle_length * np.cos(vehicle_angle), vehicle_length * np.sin(vehicle_angle)])).astype(np.int32).reshape(2)
    p3 = p1 + np.around(np.asarray([vehicle_width * np.cos(vehicle_angle), vehicle_width * np.sin(vehicle_angle)])).astype(np.int32).reshape(2)
    p4 = p2 + np.around(np.asarray([vehicle_width * np.cos(vehicle_angle), vehicle_width * np.sin(vehicle_angle)])).astype(np.int32).reshape(2)

    # Draw rectangle
    cv2.rectangle(img, tuple(p1), tuple(p4), color=(255, 20, 20), thickness=2)

# Show results
img = cv2.transpose(img)
cv2.imshow("Results", img)
cv2.waitKey(0)