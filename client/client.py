class Start:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method_one(self):
        print(self.a + self.b)

def static_f(n):
    return n ** 2

test_S = Start(8, 4) #?
test_S.b #?
test_S.b = 3
test_S.b #?
test_S.b = static_f(test_S.a)
test_S.b #?
