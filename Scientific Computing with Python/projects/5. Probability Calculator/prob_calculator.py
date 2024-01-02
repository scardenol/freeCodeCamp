import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def __str__(self):
        return str(self.contents)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        else:
            drawn_balls = []
            for i in range(num_balls):
                drawn_balls.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
            return drawn_balls


# The experiment function should return a probability.
# For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    M = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            if ball in drawn_balls_dict:
                drawn_balls_dict[ball] += 1
            else:
                drawn_balls_dict[ball] = 1
        if all(drawn_balls_dict.get(key, 0) >= value for key, value in expected_balls.items()):
            M += 1
            probability = M / num_experiments
    return probability
