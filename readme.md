# ELLevator ReadMe
#### _Potential Engineer Interview Submission_

##### Summary
This project simulates the behavior of a single elevator.

##### Languages and Libraries Used
- Python 3.7

##### Files Included
- main.py
- ellevator.py
- readme.md

### How to Run
- Be sure you have installed Python 3.7 or higher and all files listed above are in the same directory
- In a Terminal shell, navigate to the directory chosen in the above step
- Type the command: 
```sh
python3 main.py
```
- You will see text output in your terminal giving status info and prompting you for input. Respond accordingly
- _Alternatively, you can run this from an environment of your choice. You will still run main.py to inititate the program_

### Assumptions, Limitations, and Decisions Made
##### Assumptions
- When finished with its list of requests, the Elevator should return to the first floor (or lobby)
- There is only one Elevator
- There is only one master queue, which exists outside of and is accessed by the Elevator
- The Elevator accepts an input of (floor, direction) from the 'outside'. This summons the Elevator.
- The Elevator accepts an input of (floor, exit) from the 'inside'. This is logged as a destination.

##### Decisions
- The Elevator moves incremenetally up and down along a list of integers between and including a provided minimum and maximum floor number. At each floor, the Elevator will decide if it should stop.
- The Elevator **will stop** at a floor if there exists an external summon request for the current floor _in the **same** direction the Elevator is already traveling_
- The Elevator **will stop** at a floor if there exists an internal request for the current floor, _regardless of direction_
- The Elevator **will not stop** at a floor if there exists an external summon request for the current floor _in the **opposite** direction the Elevator is already traveling_

##### Limitations (personal and technical)
- The Elevator can only accept input while the doors are open.
- The Elevator's behavior is hard-coded at the moment. It cannot quickly become another flavor of Elevator.
- The Elevator currently checks direction and if it should open its doors twice. This is in response to the decisions outlined above. I imagine there is a more efficient way to ensure the Elevator turns around at the top or bottom of its path, but I kept things simple for my and your (mostly my) sanity.