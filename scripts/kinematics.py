import math

# Dimensions du bras (cm)
BASE_HEIGHT = 6.0
L1 = 12.0
OFFSET = 2.5
L2 = 20.5

# Constantes calculées
AC = math.sqrt(L1**2 + OFFSET**2)
EPSILON = math.atan2(OFFSET, L1)


def fk(theta1_deg, theta2_deg, theta3_deg):
    t1 = math.radians(theta1_deg)
    t2 = math.radians(theta2_deg)
    t3 = math.radians(theta3_deg)

    r = L1 * math.cos(t2) + OFFSET * math.sin(t2) + L2 * math.cos(t2 + t3)
    z = BASE_HEIGHT + L1 * math.sin(t2) + OFFSET * math.cos(t2) + L2 * math.sin(t2 + t3)
    x = r * math.cos(t1)
    y = r * math.sin(t1)

    return x, y, z


def ik(x, y, z):
    theta1 = math.atan2(y, x)

    r = math.sqrt(x**2 + y**2)
    z_prime = z - BASE_HEIGHT

    AD = math.sqrt(r**2 + z_prime**2)

    if AD > AC + L2 or AD < abs(AC - L2):
        print(f"Point ({x}, {y}, {z}) hors de portée!")
        return None

    cos_a = (AC**2 + AD**2 - L2**2) / (2 * AC * AD)
    cos_a = max(-1, min(1, cos_a))
    angle_A = math.acos(cos_a)

    cos_d = (L2**2 + AD**2 - AC**2) / (2 * L2 * AD)
    cos_d = max(-1, min(1, cos_d))
    angle_D = math.acos(cos_d)

    alpha = math.atan2(z_prime, r)

    theta2 = alpha + angle_A - EPSILON

    angle_C = math.pi - angle_A - angle_D
    theta3 = -(angle_C - EPSILON)

    t1 = math.degrees(theta1)
    t2 = math.degrees(theta2)
    t3 = math.degrees(theta3)

    return t1, t2, t3
