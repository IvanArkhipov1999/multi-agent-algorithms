import numpy as np


# TODO: Finish documentation
class Parameters:
    """
    A class representing parameters of multi-agent algorithms.

    Parameters
    ----------
    n: int
        Number of agents in multi-agent network.
    adj: np.matrix
        Adjacency matrix for agents.
    productivity: np.matrix
        Productivity matrix for agents.
    theta_hat: np.matrix
        Estimations?
    """
    n: int
    adj: np.matrix
    product: np.matrix
    theta_hat: np.matrix = np.matrix([[0], [0], [0]])
    neib_add: int
    add_neib_val: float

    params_dict: dict
