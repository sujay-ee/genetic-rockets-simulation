## Genetic Rockets Simulation
A genetic algorithm simulation of rockets trying to reach the target

#### Project Structure
```
.
├── services            Core components of the simulation
│   ├── controller.py   Central processing block
│   ├── population.py   Service to handle creation and deletion of test agents
│   ├── world.py        Environment where agents interact
│   └── visualizer.py   Pygame wrapper with utility functions
├── shared              Components shared throughout the app
│   ├── configs.py      App level Configuration
│   └── colors.py       Rgb color values
├── main.py             Entry point for the simulation
└── README.md
```

#### Usage
- Create a virtual environment
    ```
    python3 -m venv venv
    ```
- Activate the virtual environment
    ```
    source venv/bin/activate
    ```
- Install the requirements
    ``` 
    pip3 install -r requirements.py
    ```
- To run the simulation
    ```
    python3 main.py
    ```
- To update the simulation configurations use the configs file located at `shared/configs.py`
- To exit the virtual env
    ```
    deactivate
    ```


#### References
- Vectors
  - https://www.mathsisfun.com/algebra/vectors.html
  - https://natureofcode.com/book/chapter-1-vectors
- Autonomous Agents (Controlling rockets on the screen) - 
  - https://natureofcode.com/book/chapter-6-autonomous-agents/
- Genetic Algorithm
  - https://natureofcode.com/book/chapter-9-the-evolution-of-code/
  - Youtube tutorial - https://www.youtube.com/watch?v=9zfeTw-uFCw&list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV
