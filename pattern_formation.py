import numpy as np
import matplotlib.pyplot as plt
# Import function to create character coordinates for a sentence
from characters import create_sentence


def update_positions(agents, velocity, targets):
    """
    Update agent positions based on velocity and distance to target points.

    Parameters:
    agents (ndarray): Current positions of agents.
    velocity (ndarray): Current velocities of agents.
    targets (ndarray): Target points each agent is moving toward.

    Returns:
    bool: True if all agents are close enough to their targets, otherwise False.
    """
    n_agents = len(agents)
    all_close = True  # Flag to check if all agents are near their targets

    for i in range(n_agents):
        # Calculate vector and distance from the agent to its target
        to_target = targets[i] - agents[i]
        distance_to_target = np.linalg.norm(to_target)

        # If any agent is not close to its target, keep the loop going
        if distance_to_target >= 0.05:
            all_close = False

        # Adjust step size based on distance to target for smoother approach
        step_size = np.clip((distance_to_target ** 2) * 0.1, 0.005, 0.1)

        # Calculate cohesive force, adjusting the direction and magnitude of movement
        cohesion_force = to_target / (distance_to_target + 1e-5) * step_size
        # Update agent's velocity by combining its existing velocity and the cohesive force
        velocity[i] = velocity[i] * 0.6 + cohesion_force
        agents[i] += velocity[i]  # Move agent according to updated velocity

    return all_close  # Return whether all agents are close to their targets


def swarm_pattern_formation(sentence, num_agents=None):
    """
    Initialize and display agents forming a sentence pattern using a swarm approach.

    Parameters:
    sentence (str): Sentence to be formed by the agents.
    num_agents (int, optional): Number of agents to use. If not provided, defaults to required number.
    """
    # Set spacing between letters
    letter_spacing = 7
    sentence_points = []  # Store coordinates for the entire sentence

    # Add left padding to improve readability of the first letter
    x_offset = 15

    # Generate and arrange coordinates for each letter in the sentence
    for word in sentence.split(" "):
        word_points = create_sentence(word)
        for (x, y) in word_points:
            sentence_points.append((x + x_offset, y))
        x_offset += max([pt[0] for pt in word_points]) + letter_spacing

    points = np.array(sentence_points)
    required_agents = len(points)
    print(f"Recommended number of agents for this sentence: {required_agents}")

    # Prompt user for agent count, defaulting to recommended number if not specified
    user_input = input(
        f"Enter the number of agents (or press Enter to use {required_agents}): ")
    if user_input.strip():
        num_agents = int(user_input)
    else:
        num_agents = required_agents

    # Initialize agent positions and velocities
    agents = np.random.rand(num_agents, 2) * np.max(points, axis=0)
    velocity = np.zeros((num_agents, 2))

    # Adjust the number of target points if agent count differs from required
    targets = np.tile(
        points, (num_agents // required_agents + 1, 1))[:num_agents]

    # Set dynamic plot limits based on sentence dimensions
    max_x = x_offset
    max_y = max([y for _, y in points]) + 20
    min_y = -10

    plt.ion()  # Interactive mode for real-time plotting
    fig, ax = plt.subplots(figsize=(max_x / 10, max_y / 10))

    while True:
        all_close = update_positions(agents, velocity, targets)
        ax.clear()
        ax.scatter(agents[:, 0], agents[:, 1], color='blue', label='Agents')
        ax.scatter(targets[:, 0], targets[:, 1], color='red', alpha=0.0)
        ax.legend()
        ax.set_xlim(0, max_x)
        ax.set_ylim(max_y, min_y)
        plt.draw()
        plt.pause(0.01)

        if all_close:
            break

    plt.ioff()  # End interactive mode
    plt.show()


# Prompt user for input and visualize the sentence pattern
user_sentence = input("Enter the sentence you want to display: ")
swarm_pattern_formation(user_sentence)
