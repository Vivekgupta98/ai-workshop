import matplotlib.pyplot as plt
import networkx as nx


def show_graph(graph):
    source = graph.get_graph()
    flow = nx.DiGraph((edge.source, edge.target) for edge in source.edges)
    labels = {
        key: node.name.strip("_").replace("_", "\n")
        for key, node in source.nodes.items()
    }
    routes = {
        (edge.source, edge.target): edge.data
        for edge in source.edges
        if edge.data
    }

    for layer, nodes in enumerate(nx.bfs_layers(flow, "__start__")):
        for node in nodes:
            flow.nodes[node]["layer"] = layer

    positions = nx.multipartite_layout(flow, subset_key="layer")
    plt.figure(figsize=(10, 6))
    nx.draw_networkx(
        flow,
        positions,
        labels=labels,
        node_color="#dbeafe",
        node_size=3200,
        arrowsize=20,
        font_size=9,
    )
    nx.draw_networkx_edge_labels(flow, positions, edge_labels=routes)
    plt.axis("off")
    plt.show()
