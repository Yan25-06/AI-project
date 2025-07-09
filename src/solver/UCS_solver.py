from .solver_base import Solver, Node, Solution
from time import sleep
from heapq import heappop, heappush,heapify
from ..game.game import Board
import heapdict



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
        next_nodes = [Node(state, node.moves+1, node) for state in next_states]  
        # calculate priority for each next node
        for next_node in next_nodes:
            next_node.priority = node.priority + self.get_cost(next_node)
        
        return next_nodes


    def solve(self)-> Solution | None: 
        """
        Min heap is best for pop() because we want to expand the node with the lowest cost first.  
        Dictionary is used for O(1) lookup of visited nodes. 
        -> heapdict = min heap + dictionary
        """
        queue = heapdict.heapdict({Node(self.initial_board,0): 0})  

        """
        closed_set is used to keep track of nodes that have already been popped from frontier (queue).
        """
        closed_set: set[Node] = set()

        # get all moves 
        while len(queue) != 0:  
            curr_node:Node = queue.popitem()[0]


            # because it's used to be popped, we won't expand it again
            is_closed = curr_node in closed_set
            if is_closed: 
                continue


            # check goal
            if curr_node.board.is_goal():  
                self.solution = self._reconstruct_path(curr_node)  
                self.moves = len(self.solution) - 1 # we don't count intial board
                self.expanded_nodes = len(closed_set)  # number of expanded nodes == len(closed_set)
                return self.solution



            # marked as popped and expanded
            closed_set.add(curr_node)

            # expand  
            for neighbor in self.expand(curr_node):  
                is_neighbor_reached = neighbor in queue 
                # add if not reached
                if not is_neighbor_reached: 
                    queue[neighbor] = neighbor.priority  
                # if reached, and cheaper, update it
                else: 
                    is_neighbor_cheaper = neighbor.priority < queue[neighbor]
                    if is_neighbor_cheaper:
                        queue[neighbor] = neighbor.priority

        return None
