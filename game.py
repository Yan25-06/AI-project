class Car:
    def __init__(self, name, x, y, length, direction, is_red_car=None):
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.dir = direction
        self.is_red_car = is_red_car
    
class Board:
    def __init__(self, cars_dict): ...
    def can_move(self, car_name, steps):
        '''
        Kiểm tra xem xe có thể di chuyển một số bước nhất định mà không va chạm.

        Parameters:
        - car_name: str, tên xe cần kiểm tra (ví dụ 'R', 'A',...)
        - steps: int, số bước cần di chuyển (âm = lùi/trái, dương = tiến/phải)

        Return:
        - bool: True nếu hợp lệ, False nếu bị cản hoặc vượt khỏi lưới.
        '''
    def move(self, car_name, steps):
        '''
        Thực hiện di chuyển xe (khi hợp lệ).

        Parameters:
        - car_name: str, tên xe cần di chuyển
        - steps: int, số bước di chuyển (âm/dương tùy chiều)

        Return: None (cập nhật vị trí xe trực tiếp)
        '''
    def generate_next_states(self):
        '''
        Sinh ra tất cả trạng thái hợp lệ kế tiếp từ trạng thái hiện tại.
        Parameters: None

        Return:
        - list[Board]: danh sách các Board mới sau từng nước đi hợp lệ.
        '''

    def is_goal(self):
        '''Kiểm tra trạng thái hiện tại có phải là trạng thái thắng (xe R tới biên phải).

        Parameters: None

        Return:
        - bool: True nếu thắng, False nếu chưa.
        '''
    def to_matrix(self):
        '''
        Chuyển trạng thái board hiện tại thành ma trận 2D 6x6.

        Parameters: None

        Return:
        - list[list[str]]: ma trận 6x6, mỗi ô là '.', hoặc ký hiệu xe.
        '''
    def print(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    