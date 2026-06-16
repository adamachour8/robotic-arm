import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Plages de mouvement (range total)
range2 = 160  # épaule peut balayer 120°
range3 = 160  # coude
range4 = 160  # poignet

# Position actuelle (ce que le slider va contrôler)
theta2 = 0  # position initiale
theta3 = 0
theta4 = 0

# Dimensions de la bas
Hbase = 7  # hauteur de la base
Lbase = 6  # cote de la base carre

# Dimensions des membres en cm
L1 = 12
L2 = 10
L3 = 7


def fw_2d():
    x1, y1 = 0, 0  # sol
    x2, y2 = 0, Hbase  # haut de la base

    a2 = np.radians(theta2 + 90)
    a3 = np.radians(theta2 + theta3 + 90)
    a4 = np.radians(theta2 + theta3 + theta4 + 90)

    x3, y3 = x2 + L1 * np.cos(a2), y2 + L1 * np.sin(a2)  # épaule
    x4, y4 = x3 + L2 * np.cos(a3), y3 + L2 * np.sin(a3)  # coude
    x5, y5 = x4 + L3 * np.cos(a4), y4 + L3 * np.sin(a4)  # EE

    return (x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)


fig, ax = plt.subplots(figsize=(10, 8))
fig.subplots_adjust(bottom=0.35)

ax_t2 = fig.add_axes([0.2, 0.20, 0.6, 0.03])
ax_t3 = fig.add_axes([0.2, 0.13, 0.6, 0.03])
ax_t4 = fig.add_axes([0.2, 0.06, 0.6, 0.03])

s_t2 = Slider(ax_t2, "θ2", -range2 / 2, range2 / 2, valinit=theta2)
s_t3 = Slider(ax_t3, "θ3", -range3 / 2, range3 / 2, valinit=theta3)
s_t4 = Slider(ax_t4, "θ4", -range4 / 2, range4 / 2, valinit=theta4)


def update_plot():
    ax.clear()

    pts = fw_2d()
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    # Le bras
    ax.plot(xs, ys, "o-", color="#2563EB", linewidth=2.5, markersize=8)

    # La base (rectangle)
    base_rect = plt.Rectangle(
        (-Lbase / 2, 0),
        Lbase,
        Hbase,
        fill=True,
        facecolor="#334155",
        edgecolor="white",
        linewidth=1,
    )
    ax.add_patch(base_rect)

    # Le sol
    ax.axhline(0, color="gray", linewidth=1)

    # End-effector
    ax.plot(xs[-1], ys[-1], "*", color="red", markersize=14)

    # Labels
    labels = ["Sol", "Base", "Épaule", "Coude", "EE"]
    for label, (x, y) in zip(labels, pts):
        ax.annotate(
            label, (x, y), textcoords="offset points", xytext=(6, 6), fontsize=9
        )

    ax.set_xlim(-30, 30)
    ax.set_ylim(-10, 30)
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_xlabel("X (cm)")
    ax.set_ylabel("Z (cm)")
    ax.set_title(f"θ2={theta2}° θ3={theta3}° θ4={theta4}°")


def on_change(val):
    global theta2, theta3, theta4
    theta2 = s_t2.val
    theta3 = s_t3.val
    theta4 = s_t4.val
    update_plot()
    fig.canvas.draw_idle()


s_t2.on_changed(on_change)
s_t3.on_changed(on_change)
s_t4.on_changed(on_change)

update_plot()
plt.show()
