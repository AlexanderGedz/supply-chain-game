import networkx as nx

supply_chain_graph = nx.DiGraph()

nodes_list = [
    (
        0, {
            "title": "Production",
            "type": "source"
        }
    ),
    (
        1, {
            "title": "Factory",
            "type": "intermediary",
            "inventory": 4
        }
    ),
    (
        2, {
            "title": "Distributor",
            "type": "intermediary",
            "inventory": 4
        }
    ),
    (
        3, {
            "title": "Wholesaler",
            "type": "intermediary",
            "inventory": 4
        }
    ),
    (
        4, {
            "title": "Retailer",
            "type": "intermediary",
            "inventory": 4
        }
    ),
    (
        5, {
            "title": "End Consumer",
            "type": "consumer"
        }
    )
]

edges_list = [
    (
        0, 1, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        1, 2, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        2, 3, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        3, 4, {
            "distance": 2,
            "batches_en_route": [4, 4],
            "order": 4,
            "backlog": 0
        }
    ),
    (
        4, 5, {
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
        print(f"  {node}: {attributes}")
    print("\nEdges:")
    for source, target, attributes in graph.edges(data=True):
        print(f"  {source} -> {target}: {attributes}")

display_graph(supply_chain_graph)
