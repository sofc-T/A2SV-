class Robot:

    def __init__(self, width: int, height: int):
        self.w,self.h = width, height
        self.p = (2 * width + 2 * height ) - 4
        self.point = 0
        self.n = (width + height) * 2 - 4
        self.n1 = width
        self.n2 = width + height - 1
        self.n3 = 2 * width + height - 2
        self.mov = False
    def step(self, num: int) -> None:
        self.point += num
        self.point %= self.p
        if not self.mov:
            self.mov = True

    def getPos(self) -> List[int]:
        if self.point < self.n1:
            return [self.point, 0]
        elif self.point < self.n2:
            return [self.w-1, self.point - self.n1 + 1]
        elif self.point < self.n3:
            return [self.n3 - 1 - self.point, self.h-1]
        else:
            return [0, self.n - self.point]

    def getDir(self) -> str:
        if self.point < self.n1:
            if self.mov and self.point == 0:
                return "South"
            return "East"
        elif self.point < self.n2:
            return "North"
        elif self.point < self.n3:
            return "West"
        else:
            return "South"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()