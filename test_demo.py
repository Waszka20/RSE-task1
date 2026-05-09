import matplotlib.pyplot as plt

from fasttrajectory import simulate_projectile

x, y = simulate_projectile(
    velocity=50,
    angle_deg=45,
    drag=0.01,
)

plt.plot(x, y)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion")
plt.grid(True)

plt.show()