Real-World Analogy

The buttons and switches in your smartphone behave differently depending on the current state of the device:

    When the phone is unlocked, pressing buttons leads to executing various functions.
    When the phone is locked, pressing any button leads to the unlock screen.
    When the phone’s charge is low, pressing any button shows the charging screen.


The State Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. It is particularly useful for objects that have clear, distinguishable states and whose behavior varies depending on their state. This pattern encapsulates each state into a separate class, making the code modular and allowing state-specific behavior changes without complex conditional statements.
Real-Life Example: Document Workflow

Imagine a document with different states in an approval workflow: Draft, Submitted, Approved, and Rejected. Each state defines what actions are allowed, like submitting, approving, or rejecting. By using the State Pattern, we can separate the behaviors associated with each state, making it easier to add or modify states in the workflow.
Implementation of the State Pattern

    We create a State interface or abstract base class.
    We create concrete classes for each state (DraftState, SubmittedState, etc.), each implementing the behavior for that state.
    The main Document class changes its state by delegating the action to the current state class.








Explanation

    State Interface (DocumentState): Defines actions like submit, approve, and reject.
    Concrete States (DraftState, SubmittedState, ApprovedState, RejectedState): Each class represents a specific state of the document, implementing behavior for each action as it applies to that state.
    Context Class (Document): Holds a reference to the current state and delegates actions to the current state object.

Real-World Use Cases for the State Pattern

    Media Player: A media player may have states like Playing, Paused, and Stopped, each with its own specific actions.
    ATM Machine: ATMs can have states such as Idle, HasCard, CorrectPIN, and NoCash, each affecting the available operations.
    Online Order: Orders go through various states (e.g., Created, Paid, Shipped, Delivered, and Cancelled), each with its own set of valid operations.
    Game Character States: In a game, characters might have different states like Standing, Running, Jumping, and Attacking, each with different animations and behaviors.

Benefits of the State Pattern

    Simplifies complex conditionals: Avoids large if-else statements for state-specific behavior.
    Enhances flexibility: Makes it easy to add new states without altering existing code.
    Encapsulates state behavior: Each state is self-contained, making code easier to read and maintain.

The State Pattern is especially useful when an object’s behavior depends on its current state, as it provides a clean and organized approach for implementing and managing state-specific behavior.
