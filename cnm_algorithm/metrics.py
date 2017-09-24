from evaluate import load_ground_truth_fb
from functools import reduce

def load_feature_groups(net_number):
    """
        Creates a dictionary of features
    """
    rayray = open("facebook/{}.feat".format(net_number)).readlines()
    stuffs = [map(int, i.strip().split(" ")) for i in rayray]
    dictionary = {i[0]:i[1:] for i in stuffs}
    return dictionary

def load_probabilities(net_number):
    """
        Creates an average likiness 
        of everyone in the group
    """
    groups = load_ground_truth_fb(net_number)
    prob = load_feature_groups(net_number)
    yeah = len(prob[0])
    for community in groups:
    	init = [0 for _ in range(yeah)]
    	for person in community:
    		arr = prob[person]
    acc = reduce(lambda x, y: [i+j for i,j in zip(x,y)], prob)
    mean = [acc / float(len(prob))]