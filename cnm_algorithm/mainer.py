#!/usr/bin/env python

from loaddata import load_data_networkx_facebook
from evaluate import evalautate_communities, load_ground_truth_fb, cesna_loss
from community import CNMCommunityDetection, CNMCommunityModified
import sys

def main(egonet):
    graph = load_data_networkx_facebook(egonet)
    communities = CNMCommunityModified(graph)
    truth = load_ground_truth_fb(egonet)

    if truth == -1:
        return
    acc = cesna_loss(truth, communities)

    if acc != -1:
        print("Accuracy of Community CNM: {}".format(acc))
    else:
        print("No training set")

if __name__ == '__main__':
    main(int(sys.argv[1]))
