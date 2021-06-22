import numpy as np


class Tracker:
    def __init__(self, width, height, depth, pi_x, pi_y, pi_d):
        self.width = width
        self.height = height
        self.depth = depth

        self.pi_x = pi_x
        self.pi_y = pi_y
        self.pi_d = pi_d
        self.pi_yaw = pi_d

        self.error_x = 0
        self.error_y = 0
        self.error_d = 0
        self.error_yaw = 0

    def __call__(self, x, y, d, yaw):
        error_x = x - 0
        error_y = y - 0
        error_d = d - self.depth
        error_yaw = 0 - yaw

        #print(error_x, error_y, error_d)

        s_1 = self.pi_x[0] * error_x + self.pi_x[1] * (error_x - self.error_x)
        s_1 = int(np.clip(s_1, -100, 100))

        s_2 = self.pi_y[0] * error_y + self.pi_y[1] * (error_y - self.error_y)
        s_2 = -1 *int(np.clip(s_2, -100, 100))

        s_3 = self.pi_d[0] * error_d + self.pi_d[1] * (error_d - self.error_d)
        s_3 = int(np.clip(s_3, -100, 100))

        s_4 = self.pi_yaw[0] * error_yaw + self.pi_yaw[1] * (error_yaw - self.error_yaw)
        # s_4 = int(np.clip(s_4, -100, 100))

        self.error_x = error_x
        self.error_y = error_y
        self.error_d = error_d
        self.error_yaw = error_yaw

        if x == 0:
            self.error_x = 0
            s_1 = 0

        if y == 0:
            self.error_y = 0
            s_2 = 0

        if d == 0:
            self.error_d = 0
            s_3 = 0
        # print(s_1,s_2,s_3)

        return s_1, s_2, s_3
