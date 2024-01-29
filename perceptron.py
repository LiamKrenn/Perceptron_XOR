def heaviside(sum: float) -> int:
    if sum >= 0:
        return 1
    else:
        return 0


def perceptron(values: list[int], weights: list[float], bias: float) -> int:
    # Number of values and weights must be the same
    if len(values) != len(weights):
        raise ValueError("The number of values and weights must be the same.")

    # Calculate the sum of the values times the corresponding weights
    sum = 0
    for i in range(len(values)):
        sum += values[i] * weights[i]

    # Add the bias
    sum += bias

    # Return the result of the heaviside function
    return heaviside(sum)
