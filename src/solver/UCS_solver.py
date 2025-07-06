from .solver_base import Solver, Node, Solution
from time import sleep
from heapq import heappop, heappush,heapify
from ..game.game import Board



class UCSSolver(Solver):
    def __init__(self, initial_board:Board): 
        # sanitize
        if initial_board.get_red_car().y != 2: 
            raise ValueError("The red car must be at row 2 to be solveable") 
        super().__init__(initial_board) 

    def get_cost(self,node: Node)->int:  
        prev_state = node.previous.board if node.previous else None
        # if first move, cost is 0: 
        if prev_state is None:  
            return 0

        # calculate cost based on the previous state and current state
        cost = self.get_move_cost(prev_state, node.board)
        return cost


    def _reconstruct_path(self, node):
        return super()._reconstruct_path(node) 

    def expand(self, node: Node)-> list[Node]:
        next_states = node.board.generate_next_states()  

        # initialize next nodes with moves + 1 
        next_nodes = [Node(state, node.moves+1,node) for state in next_states]  
        # calculate priority for each next node
        for next_node in next_nodes:
            next_node.priority = node.priority + self.get_cost(next_node)
        
        return next_nodes


    def solve(self)-> Solution | None: 
        """
        Dictionary of node-cost: Python dict use hash table for O(1) lookup.
        """
        visited: dict[Node,float] = {}

        """
        Min heap is best because we want to expand the node with the lowest cost first. 
        """
        queue: list[Node] =  [Node(self.initial_board, 0, None)]  
        heapify(queue)

        # get all moves 
        while len(queue) != 0:  
            curr_node = heappop(queue)   


            is_visited = curr_node in visited
            is_visited_cheaper = visited.get(curr_node,float('inf')) < curr_node.priority
            # skip if visited node is cheaper (better)
            if is_visited and is_visited_cheaper:
                continue

            # check goal
            if curr_node.board.is_goal():  
                self.solution = self._reconstruct_path(curr_node)  
                self.moves = curr_node.moves   
                self.expanded_nodes = len(visited)
                return self.solution

            # check if visited
            visited[curr_node] = curr_node.priority   

            # expand  
            for neighbor in self.expand(curr_node):  
                is_neighbor_visited = neighbor in visited  
                is_neighbor_cheaper = neighbor.priority < visited.get(neighbor,float('inf'))
                if not is_neighbor_visited or is_neighbor_cheaper:
                    heappush(queue,neighbor) 

        return None
