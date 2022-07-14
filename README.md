# dac - Diagrams as Code
Combinations of Diagrams as Code tools, aiming for a minimal workflow. 

## Motivation
Diagrams really aid understanding a software system or architecture and the tooling around such diagramming techniques are not quite straight forward or need installation of many dependencies. 
We use a minimal docker image and container to run all diagram processing. 

## Tools
The project includes ability to generate diagrams from code using:
- Python - [diagrams](https://diagrams.mingrammer.com/). Generates architecture diagrams from python code.
- Uml - [plantuml](https://plantuml.com/). Generates any uml diagram.
- C4 Model - [c4-plantuml](https://github.com/plantuml-stdlib/C4-PlantUML). Generates diagrams from uml code with C4 resources available. 
- Docker - To run and containerize the tools.
