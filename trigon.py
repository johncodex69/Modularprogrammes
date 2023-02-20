#This implements trigonometry functions
import math

#Find the sin
def get_sin(x):
    #x is in degrees
    angle_rad = math.radians(x)
    angle_sin = math.sin(angle_rad)

    return angle_sin

def get_tan(x):
      #x is in degrees
    angle_rad = math.radians(x)
    angle_tan = math.tan(angle_rad)

    return angle_tan

def get_cos(x):
      #x is in degrees
    angle_rad = math.radians(x)
    angle_cos = math.cos(angle_rad)

    return angle_cos
