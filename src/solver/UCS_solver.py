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
        return node.moves  # or any other cost function, e.g., number of moves


    def _reconstruct_path(self, node):
        return super()._reconstruct_path(node) 

    def expand(self, node: Node)-> list[Node]:
        next_states = node.board.generate_next_states()  
        next_nodes = [Node(state, node.moves+1,node) for state in next_states]  
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

            # check goal
            if curr_node.board.is_goal():  
                self.solution = self._reconstruct_path(curr_node)  
                self.moves = curr_node.moves  
                return self.solution

            # check if visited
            is_visited = curr_node in visited 
            if not is_visited:
                visited[curr_node] = curr_node.moves   

                # expand  
                for neighbor in self.expand(curr_node):  
                    is_neighbor_visited = neighbor in visited 
                    if not is_neighbor_visited:
                        neighbor.previous = curr_node 
                        neighbor.priority = self.get_cost(neighbor)
                        heappush(queue,neighbor) 

    
        return None


    # if is_goal
    #   self.solution = _reconstruct_path 
    #   ...