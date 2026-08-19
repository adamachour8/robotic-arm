# Calibration
Base (MG996R, CH0): min=100, center=300, max=580
Shoulder (DS3218, CH1): min=85, center=330, max=580, 45deg=235
Elbow (MG996R, CH2): min=100, center=300, max=580
Gripper (SG90, CH4): fermé=100, ouvert=330

# Poids et longueur
Base link = structure base + corps du servo base
166g; H=6cm
Link 1 = horn base + bras + corps du servo shoulder
120g; L=12cm
Link 2 = horn shoulder + avant-bras + corps du servo elbow
99g; L=11cm; distance de 2.5cm avec L1
Link 3 = horn elbow + gripper + SG90
44g; L=10.5cm; Target=9.5-10cm

## Ranges angulaires
Base (θ1): 180° à 0°
Shoulder (θ2): 0° à 180° (reach -90°)
Elbow (θ3): -180° à -90° (reach 0°)

## Ratios et zéros
Elbow: +0.4°/tick, tick_zero=500
Shoulder: +0.643°/tick, tick_zero=180
Base: +0.36°/tick, tick_zero=105

### Elbow (MG996R, CH2)
100 ticks = -160°
150 ticks = -140°
200 ticks = -120°

### Shoulder (DS3218, CH1)
250 ticks = 45°
320 ticks = 90°

### Base (MG996R, CH0)
230 ticks = 45°
375 ticks = 90°
480 ticks = 135°
520 ticks = 170°

### Gripper (SG90, CH4)
90 ticks = fermé 100%
150 ticks = assez ouvert
250 ticks = complètement ouvert