# FastTrajectory

A lightweight Python package for simulating projectile motion with optional air drag using Numba acceleration.

## Features

* Numba-accelerated simulation
* Optional air resistance
* Automated testing with pytest
* GitHub Actions CI/CD
* Automatic documentation deployment
* Automated publishing to TestPyPI

## Installation

```bash
pip install --index-url https://test.pypi.org/simple/ fasttrajectory
```

## Example

```python
from fasttrajectory import simulate_projectile

x, y = simulate_projectile(
    velocity=50,
    angle_deg=45,
    drag=0.01,
)
```

## Documentation

[https://waszka20.github.io/RSE-task1/fasttrajectory.html](https://waszka20.github.io/RSE-task1/fasttrajectory.html)


## License

GPL3.0 License
