# Agent

entity that percives its environment and acts upon that environment

# State

a configuration of the agent and its environment

# Action

choices that can be made in a given state

Actions(s) returns the set of actions that can be executed in state s

# Transition Model

a description of what state results from performing any applicable action in any state

Result(s,a) returns the state that results from doing action a in state s

# State Space

the set of all states reachable from the initial state by any sequence of actions

# Goal Test

determines whether a given state is a goal state

# Path Cost

numerical cost associated with a given path

# Node

a data structure that keeps track of:

- a state
- a parent (node that generated this node)
- an action (action applied to parent to get node)
- a path cost (from initial state to node)

# Approach

- start with a frontier that contains the initial state
- repeat:
  - if the frontier is empty, then no solution
  - remove a node from the frontier
  - if node contains goal state, return the solution
  - expand node, add resulting nodes to the frontier

# Revised Approach

- start with a frontier that contains the initial state
- start with an empty explored set
- Repeat:
  - if the frontier is empty, then no solution
  - remove a node from the frontier
  - if node contains goal state, return the solution
  - add the node to the explored set
  - expand node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set

# Depth-First Search

search algorithm that always expands the deepest node in the current frontier of the search tree

## Stack

a data structure that uses the last-in, first-out (LIFO) principle

# Breadth-First Search

search algorithm that always expands the shallowest node in the current frontier of the search tree

## Queue

a data structure that uses the first-in, first-out (FIFO) principle

# uninformed search

search strategy that uses no problem-specific knowledge

# informed search

search strategy that uses problem-specific knowledge to find solutions more efficiently

# greedy best-first search

search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)

# A\* search

search algorithm that expands node with lowest value of g(n) + h(n)

g(n) = cost to reach node
h(n) = estimated cost to goal

Optimal if:

- h(n) is admissible (never overestimates the cost to reach the goal)
- h(n) is consistent (for every node n and successor n' with step cost c, h(n) <= h(n') + c)

# Adversarial Search

searching for the best move for an agent assuming that the opponent is also making moves

## Minimax

algorithm that assumes that the opponent will play optimally

- MAX player tries to maximize the score
- MIN player tries to minimize the score

### Game

- S(0) initial state
- PLAYER(s) returns which player to move in state s
- ACTIONS(s) returns legal moves in state s
- RESULT(s,a) returns state after action a taken in state s
- TERMINAL(s) checks if state s is a terminal state
- UTILITY(s) returns the utility value of terminal state s
- MIN-VALUE(s) returns the value for a min node
- MAX-VALUE(s) returns the value for a max node

### Pseudocode

- Given a state s:
  -- MAX picks action a in ACTIONS(s) that produces highest value of MIN-VALUE(RESULT(s,a))
  -- MIN picks action a in ACTIONS(s) that produces lowest value of MAX-VALUE(RESULT(s,a))

  ```
    function MAX-VALUE(s):
        if TERMINAL(s) then return UTILITY(s)
        v <- -infinity
        for each a in ACTIONS(s) do
        v <- MAX(v, MIN-VALUE(RESULT(s,a)))
        return v

    function MIN-VALUE(s):
        if TERMINAL(s) then return UTILITY(s)
        v <- infinity
        for each a in ACTIONS(s) do
        v <- MIN(v, MAX-VALUE(RESULT(s,a)))
        return v
  ```

## Optimization

### Alpha-Beta Pruning

algorithm that eliminates branches of the search tree that cannot possibly influence the final decision

### Depth-Limited Minimax

algorithm that limits the depth of the search tree

#### Evaluation Function

a function that estimates the expected utility of the game from a given state
