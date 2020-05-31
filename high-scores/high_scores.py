def latest(scores):
    return scores.pop()

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    top_three = sorted(scores,reverse=True)
    return top_three[0:3]

