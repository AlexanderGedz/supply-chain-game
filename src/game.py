class Game:
    """
    Overall game controller, storing and coordinating the game state, and managing turns.
    """

    def __init__(self, end_turn, nodes, edges):
        """
        Initializes the game with default values and configurations.

        Args:
            end_turn (int): The total number of turns for the game.
        """
        self.current_turn = 0
        self.end_turn = end_turn
        self.nodes = nodes
        self.edges = edges

    def initialize(self):
        """
        Sets up the initial game state, including nodes, edges, and their relationships.
        """
        self.populate_inventories()
        self.populate_edges()
        self.set_up_initial_orders()

    def populate_inventories(self, initial_inventory):
        """
        Fills in the initial inventory levels for all nodes.
        """
        for node in self.nodes:
            node.inventory = initial_inventory

    def populate_edges(self):
        """
        Adds initial batches to the edges to simulate supply chain flow at the start of the game.
        """
        for edge in self.edges:
            # TODO: return here after defining Batch and Edge classes
            # define populating the list of batches in every edge with edge.delay number of batches
            ...

    def set_up_initial_orders(self, initial_order):
        """
        Sets up the initial orders for all the participants to start the game.
        """
        for edge in self.edges:
            edge.order = initial_order

    def update_turn(self):
        """
        Executes a single turn of the game by performing the following:
        1. Demand announcement from the consumer node.
        2. Order placement by each node.
        3. Order fulfillment.
        4. Movement of batches along edges.
        5. Cost calculation for the turn.
        """
        ...

    def end_game(self):
        """
        Ends the game and generates a summary of results.
        """
        ...
