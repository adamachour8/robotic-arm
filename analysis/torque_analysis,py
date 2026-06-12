# Dimensions des membres en cm
L1 = 10
L2 = 8
L3 = 6

# Section transversale estimée des membres (cm²)
# Profil creux rectangulaire ~2cm x 3cm, épaisseur paroi 2mm
A1 = 1.8  # cm² — section estimée lien 1
A2 = 1.5  # cm² — section estimée lien 2
A3 = 1.2  # cm² — section estimée lien 3

# Masses volumiques des plastiques courants (g/cm³)
densites = {
    "PLA": 1.24,
    "PLA+": 1.24,
    "PETG": 1.27,
    "ABS": 1.04,
    "ASA": 1.07,
    "Nylon": 1.14,
    "TPU": 1.21,
}

# Taux de remplissage (infill) — 1.0 = solide, 0.2 = 20%
infill = 0.20

# Choix du matériau
materiau = "PETG"
rho = densites[materiau]

# Masses des membres (g) = densité × section × longueur × infill
ML1 = rho * A1 * L1 * infill
ML2 = rho * A2 * L2 * infill
ML3 = rho * A3 * L3 * infill

# Masses fixes (g)
Mgripper = 30
Mservo = 55
Mpayload = 200
G = 9.81  # m/s²


def torque_joint(masses_bras):
    """
    Calcule le couple au pire cas (bras horizontal).
    masses_bras : liste de (masse en g, bras de levier en cm)
    Retourne le couple en kg·cm
    """
    total = 0
    for masse_g, bras_cm in masses_bras:
        total += (masse_g / 1000) * bras_cm  # kg × cm
    return total


# Joint 4 — poignet
T4 = torque_joint(
    [
        (ML3, L3 / 2),  # lien 3 à son centre
        (Mgripper, L3),  # gripper au bout
        (Mpayload, L3),  # bonbon au bout
    ]
)

# Joint 3 — coude
T3 = torque_joint(
    [
        (ML2, L2 / 2),  # lien 2 à son centre
        (Mservo, L2),  # servo poignet au bout de L2
        (ML3, L2 + L3 / 2),  # lien 3
        (Mgripper, L2 + L3),  # gripper
        (Mpayload, L2 + L3),  # bonbon
    ]
)

# Joint 2 — épaule
T2 = torque_joint(
    [
        (ML1, L1 / 2),  # lien 1 à son centre
        (Mservo, L1),  # servo coude
        (ML2, L1 + L2 / 2),  # lien 2
        (Mservo, L1 + L2),  # servo poignet
        (ML3, L1 + L2 + L3 / 2),  # lien 3
        (Mgripper, L1 + L2 + L3),  # gripper
        (Mpayload, L1 + L2 + L3),  # bonbon
    ]
)

print("Couple par joint (pire cas : bras horizontal)")
print(f"  Joint 4 (poignet) : {T4:.2f} kg·cm")
print(f"  Joint 3 (coude)   : {T3:.2f} kg·cm")
print(f"  Joint 2 (épaule)  : {T2:.2f} kg·cm")
