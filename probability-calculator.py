import copy
import random

class Hat:
    def __init__(self, **content):
        self.contents = []
        for color, count in content.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        balls = []
        if num >= len(self.contents):
            balls = self.contents.copy()
            self.contents.clear()
        else:
            for _ in range(num):
                balls.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_no = {}
        for ball in drawn_balls:
            drawn_no[ball] = drawn_no.get(ball, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if drawn_no.get(color, 0) < count:
                success = False
                break

        if success:
            M += 1

    return M/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)