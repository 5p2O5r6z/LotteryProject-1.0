#大乐透
import base_lottery_class

class brings_class(base_lottery_class.base_lotter_class):
    isTheSame = False
    def __init__(self) -> None:
        super().__init__()
        self.def_red_ball_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        self.def_blue_ball_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.red_number = 5
        self.blue_number = 2
        self.isTheSame = False
     