__author__ = 'andydelso'


class TestCase:

    def __init__(self, d, s, r):
        self.description = d
        self.steps = s
        self.results = r

    def __str__(self):
        # Mistake I was making here
        # you can't print instead of returning
        # so I had to rework this
        return """Description: {0}\nSteps:\n{1}\n\nResults:\n{2}""".format(self.description, self.steps, self.results)