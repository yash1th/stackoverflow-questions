d={'a': ['apple'], 'd': ['dog', 'dance', 'dragon'], 'r': ['robot'], 'c': ['cow', 'cotton']}
def order_by_set_size(d):
    return sorted(d, key=lambda k: len(d[k]), reverse=True)
print(order_by_set_size(d))
