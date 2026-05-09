import numpy as np

from fasttrajectory import simulate_projectile


def test_simulation_returns_arrays():
    x, y = simulate_projectile(
        velocity=50,
        angle_deg=45,
    )

    assert isinstance(x, np.ndarray)
    assert isinstance(y, np.ndarray)


def test_arrays_have_same_length():
    x, y = simulate_projectile(
        velocity=50,
        angle_deg=45,
    )

    assert len(x) == len(y)


def test_projectile_moves_forward():
    x, y = simulate_projectile(
        velocity=50,
        angle_deg=45,
    )

    assert x[-1] > 0


def test_projectile_reaches_positive_height():
    x, y = simulate_projectile(
        velocity=50,
        angle_deg=45,
    )

    assert np.max(y) > 0