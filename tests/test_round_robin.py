import numpy as np
import random
from scripts.models.parameters import Parameters
from scripts.algorithms.round_robin import RoundRobin


def test_local_voting_protocol():
    generate = True
    num_agents = 5
    productivities = [10] * num_agents
    num_steps = 20

    pars = Parameters()
    pars.n = num_agents
    Adj = np.array([
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0]
    ])
    pars.b = Adj / 2

    pars.neib_add = 5
    pars.add_neib_val = 0.3
    pars.static_system = False
    pars.params_dict = {
        "h": 0.2,
    }
    random_task_generate = [random.randint(0, 100) for _ in range(100)]

    alg_lvp = RoundRobin(params=pars, random_task_generate=random_task_generate)
    alg_lvp.run(num_steps=num_steps, generate=generate, productivities=productivities)
