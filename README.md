# Python-Learning
by Ahmad Salehi

Rename bunch of files:
rename 's/^Skywatch//' Skywatch_*

**From basics to advance, here is code samples to learn Python!**

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around objects—which are instances of classes.
Each object bundles together:
Data (attributes/state) → variables that describe the object.
Behavior (methods/functions) → operations that the object can perform.

The main principles of OOP are:
- Encapsulation → hiding internal details, exposing only what is necessary.
Example: A bank account object hides how balance is updated, and just exposes deposit() and withdraw().

- Abstraction → focusing on what an object does, not how.
Example: A Car class might have a drive() method; you don’t need to know the details of how the engine works.

- Inheritance → ability to create new classes (subclasses) from existing ones, reusing and extending code.
Example: Dog and Cat inherit from a Animal class.

- Polymorphism → ability to use the same interface for different types of objects.
Example: both Dog.speak() and Cat.speak() implement speak(), but behave differently.

The importance of OOP lies in its ability to improve maintainability, scalability, and reusability of code. Because objects are self-contained and interact through well-defined interfaces, large systems can be developed in a modular way. Changes in one part of the code are less likely to disrupt other parts, making software more robust. Moreover, by reusing existing classes through inheritance or composition, developers avoid duplication and create more efficient, adaptable systems.

OOP has numerous real-world applications. In software development, it forms the basis of graphical user interfaces, game engines, and web frameworks, where each component is represented as an object. In scientific and engineering applications, OOP is used to model complex systems such as physical simulations, neural networks, or image processing pipelines. In enterprise applications, concepts like accounts, transactions, and users are represented as objects, making systems like banking platforms, e-commerce sites, and healthcare systems easier to design and manage. Even in embedded systems and robotics, sensors, actuators, and controllers are abstracted as objects, allowing structured and reliable control over hardware.

For example, in computer vision libraries such as OpenCV or PyTorch, images, models, and transformations are often treated as objects with methods that operate on them. This makes it easier to construct pipelines where each component (e.g., loading an image, filtering, applying a neural network) can be developed, tested, and reused independently. OOP, therefore, is not only a theoretical concept but also a practical foundation for modern computing across a wide range of fields.
