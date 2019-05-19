class FibonacciNumbers:

    def __init__(self, n):
        self.n = n

    def calc(self):
        result = []
        a, b = 0, 1
        while a < self.n:
            result.append(a)
            a, b = b, a+b
        return result
