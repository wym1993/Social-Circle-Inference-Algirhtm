try:
    import snap
except:
    pass

def jaccard(comm1, comm2):
    """
        Jacardian similarity between two sets
        comm1 and comm2 are sets
    """
    int_length = float(len(comm1 & comm2))
    return int_length / (len(comm1) + len(comm2) - int_length)

def cesna_loss(ground_truth_circles, predicted_circles):
    """
        Calculates the Loss using the CESNA metric
        ground_truth_circles: A list of sets representing communities
        predicted_circles: A list of sets representing the predicted communities
    """
    loss_predicted = 0.0
    for ci in predicted_circles:
        loss_predicted += max(jaccard(ci, cj) for cj in ground_truth_circles)

    loss_predicted /= (2*len(predicted_circles))

    loss_ground = 0.0
    for ci in ground_truth_circles:
        loss_ground += max(jaccard(ci, cj) for cj in predicted_circles)

    loss_ground /= (2*len(ground_truth_circles))
    return loss_ground+loss_predicted

def evalautate_communities(communities, egonet_number):
    """
        Takes predicted communities and an egonet_number
        and calculate the CESNA loss
    """
    ground_truth_circles = []
    try:
        ground_truth_circles = load_ground_truth_fb(egonet_number)
    except IOError:
        print("Training File Not Found!")
        return -1
    predicted_circles = []
    for community in communities:
        circle = set()
        for node in community:
            circle.add(node)
        predicted_circles.append(circle)

    return cesna_loss(ground_truth_circles, predicted_circles)


def load_ground_truth_fb(egonet_number):
    """
        Given an egonet number in egonets.
        Returns a list of sets
    """
    ground_truth_circles = []
    with open("facebook/{}.circles".format(egonet_number)) as f:
        for line in f:
            liner = line.strip()
            circle = liner.split("\t")[1:]
            # Some of the lines are empty
            circle = list(filter(lambda x: x != '', 
                circle))
            circle = set(list(int(i) for i in circle))
            ground_truth_circles.append(circle)
    return ground_truth_circles
