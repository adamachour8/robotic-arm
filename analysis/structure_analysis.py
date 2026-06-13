import numpy as np

# Hypothèses :
# Cisaillement négligé (flexion domine largement)
# Section rectangulaire creuse, constante par lien
# Pire cas : bras horizontal
# Infill 20%

# Dimensions (mm pour RDM, cm pour masses)
L1_cm, L2_cm, L3_cm = 12, 10, 7
L1, L2, L3 = 120, 100, 70

# Section rectangulaire creuse
b_ext = 30
h_ext = 20
t = 2

b_int = b_ext - 2 * t
h_int = h_ext - 2 * t

I = (b_ext * h_ext**3 - b_int * h_int**3) / 12
y = h_ext / 2

# Masses (g)
densites = {
    "PLA": 1.24,
    "PLA+": 1.24,
    "PETG": 1.27,
    "ABS": 1.04,
    "ASA": 1.07,
    "Nylon": 1.14,
}

sigma_yield = {
    "PLA": 50,
    "PLA+": 45,
    "PETG": 50,
    "ABS": 40,
    "ASA": 45,
    "Nylon": 70,
}

infill = 0.20
A1, A2, A3 = 1.8, 1.5, 1.2
Mgripper = 30
Mservo = 55
Mpayload = 200
G = 9.81


def charges(materiau):
    rho = densites[materiau]
    ML1 = rho * A1 * L1_cm * infill
    ML2 = rho * A2 * L2_cm * infill
    ML3 = rho * A3 * L3_cm * infill

    F3 = (Mgripper + Mpayload + ML3) * G / 1000
    F2 = (Mservo + Mgripper + Mpayload + ML3 + ML2) * G / 1000
    F1 = (2 * Mservo + Mgripper + Mpayload + ML3 + ML2 + ML1) * G / 1000
    return F1, F2, F3


def analyse_rdm(materiau):
    F1, F2, F3 = charges(materiau)
    sy = sigma_yield[materiau]

    resultats = []
    for nom, F, L_mm in [("Lien 1", F1, L1), ("Lien 2", F2, L2), ("Lien 3", F3, L3)]:
        M = F * L_mm
        sigma = M * y / I
        sf = sy / sigma
        resultats.append((nom, M, sigma, sf))
    return resultats


pire_mat = None
pire_sf = float("inf")

for mat in densites:
    res = analyse_rdm(mat)
    sf_min = res[0][3]
    if sf_min < pire_sf:
        pire_sf = sf_min
        pire_mat = mat

print(f"Analyse RDM — materiau le plus faible : {pire_mat}")
print(f"  sigma_yield = {sigma_yield[pire_mat]} MPa")
print(f"  Section : {b_ext}x{h_ext} mm, paroi {t} mm")
print(f"  I = {I:.0f} mm4, y = {y:.0f} mm")
print()
print(f"  {'Lien':<10} {'M (N.mm)':>10} {'sigma (MPa)':>12} {'SF':>10}")
for nom, M, sigma, sf in analyse_rdm(pire_mat):
    print(f"  {nom:<10} {M:>10.1f} {sigma:>12.3f} {sf:>10.1f}x")
