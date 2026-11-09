import numpy as np
def simulate_markov_chain(transition_matrix, initial_state, num_steps):
    state = initial_state
    states = [i for i in range(len(transition_matrix))]
    path = [initial_state]
    for i in range(num_steps):
        state = int(np.random.choice(states,p= transition_matrix[state]))
        path.append(state)
    return path