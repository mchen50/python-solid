# python-solid

SOLID OOD principles in Python

SOLID is a set of five object-oriented design principles that can help you write more maintainable, flexible, and scalable code based on well-designed, cleanly structured classes.

1. Single-responsibility principle (SRP)
    - A class should have only one reason to change.
2. Open–closed principle (OCP)
    - Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
3. Liskov substitution principle (LSP)
    - Subtypes must be substitutable for their base types.
4. Interface segregation principle (ISP)
    - Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.
5. Dependency inversion principle (DIP)
    - Abstractions should not depend upon details. Details should depend upon abstractions.

## Run

- Setup:

```bash
make setup
```

- Run:

```bash
source venv/bin/activate
cd SRP
python -u xxx.py
```

## References

[SOLID Principles: Improve Object-Oriented Design in Python](https://realpython.com/solid-principles-python/#liskov-substitution-principle-lsp)
