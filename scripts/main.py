from kinematics import fk, ik


def main():
    while True:
        print("\n--- Bras Robotique 3-DOF ---")
        choix = input("FK ou IK ? (q pour quitter): ").strip().lower()

        if choix == "q":
            break

        elif choix == "fk":
            t1 = float(input("theta1 (base, degrés): "))
            t2 = float(input("theta2 (shoulder, degrés): "))
            t3 = float(input("theta3 (elbow, degrés): "))

            x, y, z = fk(t1, t2, t3)
            print(f"\nPosition du gripper:")
            print(f"  x = {x:.2f} cm")
            print(f"  y = {y:.2f} cm")
            print(f"  z = {z:.2f} cm")

        elif choix == "ik":
            x = float(input("x (cm): "))
            y = float(input("y (cm): "))
            z = float(input("z (cm): "))

            result = ik(x, y, z)
            if result:
                t1, t2, t3 = result
                print(f"\nAngles:")
                print(f"  theta1 (base)     = {t1:.2f}°")
                print(f"  theta2 (shoulder) = {t2:.2f}°")
                print(f"  theta3 (elbow)    = {t3:.2f}°")

                x2, y2, z2 = fk(t1, t2, t3)

        else:
            print("Tape 'fk', 'ik' ou 'q'")


if __name__ == "__main__":
    main()
