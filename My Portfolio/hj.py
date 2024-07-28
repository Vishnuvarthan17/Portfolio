class A:
    def greet(self):
        print("Hello from class A")

class B(A):
    def greet(self):
        super().greet()  # Calls the greet method from class A
        print("Hello from class B")

class C(A):
    def greet(self):
        super().greet()  # Calls the greet method from class A
        print("Hello from class C")

class D(B, C):
    def greet(self):
        super().greet()  # Calls the greet method from class B and class C
        print("Hello from class D")

d = D()
d.greet()
