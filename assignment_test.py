import numpy as np
import assignment


def test_poissonmle():
    np.random.seed(42)  # seed sampling
    dataset = np.random.poisson(5, 100)  # sample 100 points from Poisson with lambda = 5
    mle = assignment.PoissonMLE(dataset)
    assert mle == 4.94
