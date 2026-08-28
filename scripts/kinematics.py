import math

# Dimensions du bras (cm)
BASE_HEIGHT = 6.0
L1 = 12.0
OFFSET = 2.5
L2 = 20.5

# Constantes géométriques (step 0)
AC = math.sqrt(L1**2 + OFFSET**2)  # 12.26 cm
CD = L2  # 20.5 cm
BAC = math.atan2(OFFSET, L1)  # ≈ 11.7° (rad)


def fk(theta1_deg, theta2_deg, theta3_deg):
    t1 = math.radians(theta1_deg)
    t2 = math.radians(theta2_deg)
    t3 = math.radians(theta3_deg)

    r = L1 * math.cos(t2) - OFFSET * math.sin(t2) + L2 * math.cos(t2 + t3)
    z = BASE_HEIGHT + L1 * math.sin(t2) + OFFSET * math.cos(t2) + L2 * math.sin(t2 + t3)
    x = r * math.cos(t1)
    y = r * math.sin(t1)

    return x, y, z


def ik(x, y, z):
    # 1) θ₁
    theta1 = math.atan2(y, x)

    # 2) r signé, z'
    r = x * math.cos(theta1) + y * math.sin(theta1)
    z_prime = z - BASE_HEIGHT

    # 3) AD, ∠DAE
    AD = math.sqrt(r**2 + z_prime**2)

    if AD > AC + CD or AD < abs(AC - CD):
        print(f"Point ({x}, {y}, {z}) hors de portée!")
        return None

    DAE = math.atan2(z_prime, r)

    # 4) Loi des cosinus sur △ACD
    cos_CAD = (AC**2 + AD**2 - CD**2) / (2 * AC * AD)
    cos_CAD = max(-1, min(1, cos_CAD))
    CAD = math.acos(cos_CAD)

    cos_ACD = (AC**2 + CD**2 - AD**2) / (2 * CD * AC)
    cos_ACD = max(-1, min(1, cos_ACD))
    ACD = math.acos(cos_ACD)

    # 5) θ₂, θ₃
    theta2 = DAE + CAD - BAC
    theta3 = ACD - (2 * BAC) - math.pi / 2 + DAE

    return math.degrees(theta1), math.degrees(theta2), math.degrees(theta3)


test_cases = [
    (90, 0, -110),
    (90, 45, -135),
    (90, 60, -120),
    (90, 100, -140),
    (90, 90, -150),
    (90, 30, -115),
    (90, 135, -160),
    (90, 10, -170),
]

for t1, t2, t3 in test_cases:
    pos = fk(t1, t2, t3)
    result = ik(*pos)
    if result is None:
        continue
    ang_err = max(abs(a - b) for a, b in zip((t1, t2, t3), result))
    status = "✓" if ang_err < 0.1 else "✗"
    print(
        f"{status} IN({t1:4},{t2:4},{t3:4}) -> IK({result[0]:7.2f},{result[1]:7.2f},{result[2]:7.2f})  err={ang_err:.2f}°"
    )
