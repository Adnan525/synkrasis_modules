import warnings

warnings.filterwarnings('ignore')

import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    result = 0.0
    for i, coeff in enumerate(xs):
        result += coeff * math.pow(x, i)
    return result


def derivative(xs: list) -> list:
    """Calculates the derivative of a polynomial represented by its coefficients."""
    if len(xs) == 1:
        return [0]

    # Derivative coefficients are (n-1)*c_i for each term c_i*x^i
    new_coefficients = [(len(xs) - i - 1) * coeff for i, coeff in enumerate(xs[:-1])]
    return new_coefficients


def find_zero(xs: list):
    """Uses the Newton-Raphson method to find a zero of the polynomial defined by xs."""

    # Initial guess is set to 0
    x = 0.0

    while True:
        fx = poly(xs, x)

        if abs(fx) < 1e-6:  # Check for convergence based on absolute value of function value.
            break

        fpx = poly(derivative(xs), x)

        # Avoid division by zero or near-zero numbers to prevent numerical instability
        if abs(fpx) > 0:
            x -= fx / fpx

    return round(x, 2)


# Example usage without running the script directly (since this is just a snippet):
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # Should output approximately -0.5
