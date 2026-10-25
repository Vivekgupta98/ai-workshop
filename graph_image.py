import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyArrowPatch


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
        if edge.data and edge.source != edge.target
    }

    for layer, nodes in enumerate(nx.bfs_layers(flow, "__start__")):
        for node in nodes:
            flow.nodes[node]["layer"] = layer

    positions = nx.multipartite_layout(flow, subset_key="layer")
    regular_edges = [edge for edge in flow.edges if edge[0] != edge[1]]
    figure, axes = plt.subplots(figsize=(10, 6))
    nx.draw_networkx(
        flow,
        positions,
        labels=labels,
        node_color="#dbeafe",
        node_size=3200,
        arrowsize=20,
        font_size=9,
        edgelist=regular_edges,
        ax=axes,
    )
    nx.draw_networkx_edge_labels(flow, positions, edge_labels=routes, ax=axes)

    x_values = [position[0] for position in positions.values()]
    y_values = [position[1] for position in positions.values()]
    graph_width = max(max(x_values) - min(x_values), 1)
    axes.set_xlim(
        min(x_values) - 0.15 * graph_width,
        max(x_values) + 0.15 * graph_width,
    )
    axes.set_ylim(
        min(y_values) - 0.15 * graph_width,
        max(y_values) + 0.20 * graph_width,
    )
    axes.set_autoscale_on(False)

    for node in nx.nodes_with_selfloops(flow):
        x, y = positions[node]
        loop = FancyArrowPatch(
            (x - 0.05 * graph_width, y + 0.03 * graph_width),
            (x + 0.05 * graph_width, y + 0.03 * graph_width),
            connectionstyle="arc3,rad=-0.8",
            arrowstyle="-|>",
            mutation_scale=20,
            color="black",
            linewidth=1.5,
        )
        axes.add_patch(loop)

    axes.axis("off")
    figure.tight_layout()
    plt.show()
