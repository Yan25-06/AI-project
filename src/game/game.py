class Car:
    def __init__(self, name, x, y, length, dir):
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.dir = dir
        self.is_red_car = True if name == 'R' else False
    def copy(self):
        return Car(self.name, self.x, self.y, self.length, self.dir)
    
class Board:
    def __init__(self, cars_dict, size=6, exit_row=2, exit_col=4):
        '''
        Khởi tạo Board từ:
        - dict dạng thường: {'A': {'x':..., 'y':..., ...}}
        - hoặc dict dạng object: {'A': Car(...)}
        '''
        self.size = size
        self.exit_row = exit_row
        self.exit_col = exit_col
        self.cars = {}
        for name, data in cars_dict.items():
            if isinstance(data, Car):
                self.cars[name] = data
            elif isinstance(data, dict):
                self.cars[name] = Car(name, **data)
            else:
                raise TypeError(f"Invalid car data for '{name}': {data}")
    def copy(self):
        new_cars = {name: car.copy() for name, car in self.cars.items()}
        return Board(new_cars)
    def __is_car_at(self, x, y):
        '''
        Trả về True nếu tại ô (x, y) có xe nào chiếm.
        '''
        for car in self.cars.values():
            for i in range(car.length):
                if car.dir == 'H':
                    cx = car.x + i
                    cy = car.y
                else:  # 'V'
                    cx = car.x
                    cy = car.y + i
                if cx == x and cy == y:
                    return True
        return False

    def can_move(self, car_name, steps):
        '''
        Kiểm tra xem xe có thể di chuyển một số bước nhất định mà không va chạm.

        Parameters:
        - car_name: str, tên xe cần kiểm tra (ví dụ 'R', 'A',...)
        - steps: int, số bước cần di chuyển (âm = lùi/trái, dương = tiến/phải)

        Return:
        - bool: True nếu hợp lệ, False nếu bị cản hoặc vượt khỏi lưới.
        '''
        if abs(steps) > 1:
            raise ValueError("steps = ±1")

        car = self.cars[car_name]
        dx, dy = 0, 0
        if car.dir == 'H':
            dx = steps
        else:
            dy = steps

        if steps > 0:
            check_x = car.x + dx * car.length
            check_y = car.y + dy * car.length
        else:
            check_x = car.x + dx
            check_y = car.y + dy

        if not (0 <= check_x < self.size and 0 <= check_y < self.size):
            return False
        if self.__is_car_at(check_x, check_y):
            return False
        return True
        

    def move(self, car_name, steps):
        '''
        Thực hiện di chuyển xe (khi hợp lệ).

        Parameters:
        - car_name: str, tên xe cần di chuyển
        - steps: int, số bước di chuyển (âm/dương tùy chiều)

        Return: None (cập nhật vị trí xe trực tiếp)
        '''
        if abs(steps) > 1:
            raise ValueError("steps = ±1")
        car = self.cars[car_name]
        if car.dir == 'H':
            car.x += steps
        else:
            car.y += steps
    def generate_next_states(self)->list['Board']:
        '''
        Sinh ra tất cả trạng thái hợp lệ kế tiếp từ trạng thái hiện tại.
        Parameters: None

        Return:
        - list[Board]: danh sách các Board mới sau từng nước đi hợp lệ.
        '''
        states_list = []

        # Try red car first for faster goal reaching
        car_order = ['R'] + [name for name in self.cars if name != 'R']
        
        for car_name in car_order:
            for step in [1, -1]:  # Try forward first, then backward
                if self.can_move(car_name, step):
                    new_board = self.copy()
                    new_board.move(car_name, step) 
                    states_list.append(new_board)
        return states_list
    def get_red_car(self):
        for car in self.cars.values():
            if car.is_red_car:
                return car
    def is_goal(self):
        '''Kiểm tra trạng thái hiện tại có phải là trạng thái thắng (xe R tới biên phải).

        Parameters: None

        Return:
        - bool: True nếu thắng, False nếu chưa.
        '''
        car = self.get_red_car()
        if car.x == self.exit_col and car.y == self.exit_row:
            return True
        return False
    def to_matrix(self):
        '''
        Chuyển trạng thái board hiện tại thành ma trận 2D 6x6.

        Parameters: None

        Return:
        - list[list[str]]: ma trận 6x6, mỗi ô là '.', hoặc ký hiệu xe.
        '''
        mat = [['.' for _ in range(self.size)] for _ in range(self.size)]
        for name, car in self.cars.items():
            x, y, l, d = car.x, car.y, car.length, car.dir
            for i in range(l):
                if d == 'H':
                    mat[y][x + i] = name
                else:
                    mat[y + i][x] = name
        return mat
    def print(self):
        mat = self.to_matrix()
        for row in mat:
            print(" ".join(row))
    def __hash__(self):
        '''
        Hàm băm để sử dụng trong set hoặc dict.
        Trả về giá trị băm duy nhất cho trạng thái board hiện tại.
        '''
        return hash(tuple(sorted((car.name, car.x, car.y, car.length, car.dir) for car in self.cars.values())))
    
    def __eq__(self, other):
        '''
        So sánh hai Board có bằng nhau không.
        Hai board bằng nhau nếu tất cả xe có vị trí và thuộc tính giống nhau.
        '''
        if not isinstance(other, Board):
            return False
        if self.size != other.size or self.exit_row != other.exit_row or self.exit_col != other.exit_col:
            return False
        if len(self.cars) != len(other.cars):
            return False
        for name, car in self.cars.items():
            if name not in other.cars:
                return False
            other_car = other.cars[name]
            if (car.x != other_car.x or car.y != other_car.y or 
                car.length != other_car.length or car.dir != other_car.dir):
                return False
        return True
