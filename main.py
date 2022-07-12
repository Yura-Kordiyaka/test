class ABC:
    name = str()
    a = []

    def __init__(self, name, a):
        self.a = a
        self.name = name

    def cout(self):
        for j in self.a:
            print(j, end="" + " ")
        print("\n")

    def count(self):
        print(len(self.a))


class EnglishABC(ABC):
    numbers = 0
    b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]

    def __init__(self, name, a, numbers):
        super().__init__(name, a)
        self.a = a
        self.name = name
        self.numbers = numbers

    def belong(self, x):
        s = str()
        for g in self.b:
            if str(x).lower() == str(g).lower():
                s = "belongs"
        if len(s) > 0:
            print(s)
        else:
            print("not belong")

    def example(self):
        print(
            "Let me introduce myself. My name is Ann. I am"
            " twenty. I am a student. I study at the university. I am a prospective economist. I like this"
            " profession, that's why I study with pleasure. My parents are not economists, but they support me "
            "in my choice. We are a friendly family and try to understand and support each other in any situation."
            " Understanding and support is what I need in friendship as well.")


v = ["a", "d", "c", "g"]
first = ABC("English", v)
first.count()
first.cout()
second = EnglishABC("English", v, 5)
second.belong(v[0])
second.example()