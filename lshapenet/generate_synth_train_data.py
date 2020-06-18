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
VEHICLE_ANGLE_MEAN, VEHICLE_ANGLE_STD = 0.0 * DEG_TO_RAD, 0.2

# Determine sensor position
sensor_position = (round(MAP_WIDTH) / 2, 0)

# Init empty image
img = create_blank(MAP_WIDTH * METER_TO_PIXEL, MAP_WIDTH * METER_TO_PIXEL)

# Randomly manipulate number of vehicles
# TODO ADD NOISE
# number_of_vehicles = int(max(1, np.round(np.random.uniform(NUMBER_OF_VEHICLES_MEAN, NUMBER_OF_VEHICLES_STD, 1))))
number_of_vehicles = 5

# Create one vehicle per iteration
for i in range(number_of_vehicles):
    # Set first point and calculate all other vehicle parameters
    vehicle_length = np.random.normal(VEHICLE_LENGTH_MEAN, VEHICLE_LENGTH_STD) * METER_TO_PIXEL
    vehicle_width = np.random.normal(VEHICLE_WIDTH_MEAN, VEHICLE_WIDTH_STD) * METER_TO_PIXEL
    vehicle_angle = np.random.normal(VEHICLE_ANGLE_MEAN, VEHICLE_ANGLE_STD)

    print("Vehicle length", vehicle_length, "| Vehicle width", vehicle_width, "| Vehicle angle", vehicle_angle * 1 / DEG_TO_RAD)

    # Calculate points
    points = np.asarray([[0, 0], [vehicle_length, 0], [0, vehicle_width], [vehicle_length, vehicle_width]])
    # Rotate rectangle
    rotmat = [[np.cos(vehicle_angle), -np.sin(vehicle_angle)], [np.sin(vehicle_angle), np.cos(vehicle_angle)]]
    points = np.transpose(rotmat @ np.transpose(points))
    # Move rectangle
    offset = np.random.uniform(0.0, MAP_WIDTH, (2)) * METER_TO_PIXEL
    offset = np.tile(offset, (4, 1))
    points = points + offset
    # Convert points
    points = np.around(points).astype(np.int32)

    # Draw rectangle
    for point in points:
        print(point)
        cv2.circle(img, tuple(point), radius=3, color=(20, 20, 255), thickness=-1)

# Show results
img = cv2.transpose(img)
cv2.imshow("Results", img)
cv2.waitKey(0)