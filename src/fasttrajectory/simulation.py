import numpy as np
from numba import njit


@njit
def simulate_projectile(
    velocity: float,
    angle_deg: float,
    dt: float = 0.01,
    drag: float = 0.0,
    gravity: float = 9.81,
):
    """
    Simulate projectile motion with optional air drag.

    Parameters
    ----------
    velocity : float
        Initial velocity in m/s.
    angle_deg : float
        Launch angle in degrees.
    dt : float
        Time step in seconds.
    drag : float
        Air resistance coefficient.
    gravity : float
        Gravitational acceleration in m/s^2.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Arrays of x and y coordinates.
    """

    angle_rad = np.radians(angle_deg)

    vx = velocity * np.cos(angle_rad)
    vy = velocity * np.sin(angle_rad)

    x = 0.0
    y = 0.0

    xs = [x]
    ys = [y]

    while y >= 0:

        speed = np.sqrt(vx**2 + vy**2)

        ax = -drag * speed * vx
        ay = -gravity - drag * speed * vy

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

        xs.append(x)
        ys.append(y)

    return np.array(xs), np.array(ys)