import math

def calculate_angle(sensor, focal_length):
    return 2 * math.atan(sensor / (2 * focal_length))


def calculate_angles(focal_length, sensor_width, sensor_height):
    focal_length_m = focal_length / 1000
    sensor_width_m = sensor_width / 1000
    sensor_height_m = sensor_height / 1000

    angle_horizontal_rad = calculate_angle(sensor_width_m, focal_length_m)
    angle_vertical_rad   = calculate_angle(sensor_height_m, focal_length_m)
    
    angle_horizontal_deg = math.degrees(angle_horizontal_rad)
    angle_vertical_deg   = math.degrees(angle_vertical_rad)

    return angle_horizontal_rad, angle_vertical_rad, angle_horizontal_deg, angle_vertical_deg


def calculate_frame(angle, distance):
    return 2 * distance * math.tan(angle / 2)


def calculate_frames(angle_horizontal, angle_vertical, distance):
    frame_width = calculate_frame(angle_horizontal, distance)
    frame_height = calculate_frame(angle_vertical, distance)

    return frame_width, frame_height