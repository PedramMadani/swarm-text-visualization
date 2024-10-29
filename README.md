# Swarm Text Visualization

Swarm Text Visualization is a Python project that uses agent-based swarm dynamics to form sentences on a 2D plane. It visualizes sentences by treating each letter in the sentence as a series of pixel targets for "agents" to reach, simulating a swarm as it forms readable text in real time. This project leverages agent-based motion, dynamic plotting, and pixel-based representations of characters.

## Features

- **Sentence and Word Formation**: Visualize any sentence or word by simulating the movement of individual agents (points) toward pixel-based target coordinates.
- **Dynamic Spacing and Scaling**: Adjusts spacing between words and letters to improve readability, automatically resizing for longer sentences.
- **Interactive Agent Control**: Choose the number of agents and see how it affects the text formation.
- **Swarm Dynamics**: Agents move using cohesion forces, providing a simulation of swarm intelligence behavior.

## Getting Started

### Prerequisites

- Python 3.x
- `matplotlib` for visualization
- `numpy` for array manipulation

Install the dependencies via pip:
```bash
pip install matplotlib numpy
```
### Running the Project

#### Clone the Repository:

```bash
git clone https://github.com/PedramMadani/swarm-text-visualization.git
cd swarm-text-visualization
```

#### Run the Main Script:
```bash
python pattern_formation.py
```
Enter your desired sentence when prompted, and specify the number of agents if desired. The program will recommend the optimal number of agents but allows for custom input.

### Code Overview

- **pattern_formation.py**: Main script that initializes agents and targets, manages the swarm behavior, and visualizes the sentence formation.
- **characters.py**: Contains hexadecimal representations of each character and converts them to pixel-based coordinates. It also processes sentences to create target coordinates with appropriate spacing.

### Customization

- **Agent Count**: Choose the number of agents for each run. Fewer agents may result in incomplete text, while additional agents can increase display density.
- **Spacing**: Adjust the spacing between letters and words by modifying `letter_spacing` and `word_spacing` in `characters.py`.

### Project Structure

```plaintext
swarm-text-visualization/
├── pattern_formation.py    # Main script for visualization
├── characters.py           # Character data and coordinate generation
└── README.md               # Project documentation
```
### Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

### License

This project is licensed under the MIT License.
