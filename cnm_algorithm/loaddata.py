try:
    import networkx as nx
except ImportError:
    import sys
    sys.path.insert(0, '/usr/local/lib/python2.7/dist-packages/')
    import networkx as nx

def get_min_max(number):
    filename = 'facebook/{}.edges'.format(number)
    lines = [a.strip().split(" ") for a in open(filename).readlines()]
    raw = [int(item) for sublist in lines for item in sublist]

    lhs = min(raw)
    rhs = max(raw)
    return (lhs, rhs)

def add_edges_with_callback(number, callback):
    filename = 'facebook/{}.edges'.format(number)
    with open(filename) as f:
        for line in f:
            connections = [int(a) for a in line.split(" ")]
            callback(*connections)

def load_data_networkx_facebook(number):
    """
        Creates a networkx graph with an
        ego_net at egonet number
    """
    graph = nx.Graph()
    gen = (i.strip().split(" ") for i in open("facebook/{}.edges".format(number)).readlines())
    graph.add_edges_from((int(i[0]), int(i[1])) for i in gen)
    return graph