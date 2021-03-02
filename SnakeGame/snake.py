class Snake:
    def __init__(self):
        self.body = [(3,10), (3,9), (3,8)]
        self.length = len(self.body)

    def insert(self, head_coord):
        self.body.insert(0, head_coord)

    def append(self, tail_coord):
        self.body.append(tail_coord)
    
    def pop(self):
        return self.body.pop()
    
    def move_up(self):
        x_head = self.body[0][1]
        y_head = self.body[0][0]

        y_head += -1
        self.insert((y_head, x_head))
    
    def move_right(self):
        x_head = self.body[0][1]
        y_head = self.body[0][0]

        x_head += 1
        self.insert((y_head, x_head))
    
    def move_down(self):
        x_head = self.body[0][1]
        y_head = self.body[0][0]

        y_head += 1
        self.insert((y_head, x_head))
    
    def move_left(self):
        x_head = self.body[0][1]
        y_head = self.body[0][0]

        x_head += -1
        self.insert((y_head, x_head))
    
    def x_out_of_bound(self, yWindowSize, xWindowSize):
        x_head = self.body[0][1]
        y_head = self.body[0][0]

        if x_head > (xWindowSize - 1):
            self.insert((y_head, 1))
            last = self.pop()
            return last
        elif x_head < 1:
            self.insert((y_head, xWindowSize))
            last = self.pop()
            return last
    
    def y_out_of_bound(self, yWindowSize, xWindowSize):
        x_head = self.body[0][1]
        y_head = self.body[0][0]

        if y_head > (yWindowSize - 1):
            self.insert((1, x_head))
            last = self.pop()
            return last
        elif y_head < 1:
            self.insert((yWindowSize, x_head))
            last = self.pop()
            return last

    def get_body(self):
        return self.body
    
    def get_last_element(self):
        return list(self.body[-1])