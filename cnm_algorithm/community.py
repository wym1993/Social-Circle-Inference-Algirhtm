from copy import deepcopy
import networkx as nx
from collections import defaultdict
import numpy as np

def ModularityWithCommunities(networkxGraph, communities):
    """
        Computes Modularity with the given Communities
    """
    nodes = networkxGraph.nodes()
    degrees = networkxGraph.degree(nbunch=nodes)
    edges = len(nodes)
    mod = 0
    for community in communities:
        for i in community:
            for j in community:
                mod += float(int(networkxGraph.has_edge(i, j)))*(2.0*edges) - degrees[i]*degrees[j] 
    return mod/ (2.0*edges)

def MergeCommunities(communities, firstcomm, secondcomm):
    """
        Returns a new community set with the first and
            second communities merged
    """
    comm1 = communities[firstcomm]
    comm2 = communities[secondcomm]
    newer = [v for i, v in enumerate(communities) if i not in (firstcomm, secondcomm)]
    newer.append(comm1 | comm2)
    return newer

def CNMCommunityModified(networkxGraph):
    """
        Modified Prototypical CNM Algorithm
    """
    thresh = -35
    person_threshold = 100
    communities = [set((i,)) for i in networkxGraph.nodes()]
    bestMod = ModularityWithCommunities(networkxGraph, communities)
    while True:
        pairings = ((i, j) for i in range(len(communities)) for j in range(1, len(communities)-1) if i != j)
        bestdelta = thresh
        bestq = -1
        bestPairing = (-1, -1)
        for i, j in pairings:
            newer = MergeCommunities(communities, i, j)
            q = ModularityWithCommunities(networkxGraph, newer)
            delta = q - bestMod
            if delta > bestdelta and len(newer[-1]) < person_threshold:
                bestPairing = (i, j)
                bestdelta = delta
                bestq = q

        if bestq == -1:
            break

        communities = MergeCommunities(communities, *bestPairing)
        print("Merged {} {}".format(*bestPairing))
        bestMod = bestq
    return communities