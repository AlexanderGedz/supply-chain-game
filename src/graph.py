from enum import Enum
import networkx as nx

class NodeType(Enum):
    SOURCE = "source"
    INTERMEDIARY = "intermediary"
    END_CONSUMER = "end_consumer"

    def __str__(self):
        return self.value

class SupplyChainNode:
    def __init__(self, title, inventory, type):
        self.title = title
        self.inventory = inventory
        if not isinstance(type, NodeType):
            raise ValueError(f"Invalid type: {type}. Must be a NodeType value.")
        else:
            self.type = type

    def __str__(self):
        return(f"{self.title}: {{'inventory': {self.inventory}, 'type': '{self.type}'}}")

supply_chain_graph = nx.DiGraph()

production = SupplyChainNode("Production", None, NodeType.SOURCE)
factory = SupplyChainNode("Factory", 12, NodeType.INTERMEDIARY)
distributor = SupplyChainNode("Distributor", 12, NodeType.INTERMEDIARY)
wholesaler = SupplyChainNode("Wholesaler", 12, NodeType.INTERMEDIARY)
retailer = SupplyChainNode("Retailer", 12, NodeType.INTERMEDIARY)
end_consumer = SupplyChainNode("End Consumer", None, NodeType.END_CONSUMER)

nodes_list = [production,factory,distributor,wholesaler,retailer,end_consumer]

edges_list = [
    (
        production, factory, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        factory, distributor, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        distributor, wholesaler, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        wholesaler, retailer, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        retailer, end_consumer, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    )
]

supply_chain_graph.add_nodes_from(nodes_list)
supply_chain_graph.add_edges_from(edges_list)

def display_graph(graph):
    print("Nodes:")
    for node, attributes in graph.nodes(data=True):
        print(f"  {node}")
    print("\nEdges:")
    for source, target, attributes in graph.edges(data=True):
        print(f"  {source.title} -> {target.title}: {attributes}")

display_graph(supply_chain_graph)
