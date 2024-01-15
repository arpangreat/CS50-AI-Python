# Knowledge-Based Agents

agents that reason by operating on internal replesentations of knowledge

# Sentence

an assertion about the world in a knowledge representation language

# Propositional Logic

## Propositional Symbols

P Q R

NOT| AND | OR | IMPLICATION |BICONDITIONAL
¬ | ∧ | v | --> | <-->

## Model

assignment of a truth value to every Propositional symbol ( a "possible world")

### Model: P: It's rainnig, Q: It's tuesday

{ P = True, Q = False }

If there are n numbers of items the model will contain 2^n possible worlds

## Knwoledg Base

a set of sentences known by a Knwoledge-Based Agent

## Entaliment

KB |= α ( KB entails α )

In every model in which KB is true, α is also true

### Inference

The process of deriving new sentences from old ones

P: Swastik is a Boy
Q: Swastik is not Single
R: Swastik is a Bachelor

KB: (P ∧ ¬Q) --> R [ if Swastik is a Boy and Swastik is Single then Swastik is a Bachelor ]

P is true AND ¬Q is true then it inferece R is true

### Inference Algorithm

#### Model Checking

- To determine KB |= α:
  - enumerate all possible models.
  - If in every model where KB is true, α is also true them KB entails α
