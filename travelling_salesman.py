import itertools

def calculate_distance(path, distance_matrix):
    return sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1)) + distance_matrix[path[-1]][path[0]]

def travelling_salesman(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_path = None
    min_distance = float('inf')
    for perm in itertools.permutations(cities):
        dist = calculate_distance(perm, distance_matrix)
        if dist < min_distance:
            min_distance = dist
            min_path = perm
    return min_path, min_distance

# Example usage
if __name__ == "__main__":
    # Example distance matrix (symmetric, 4 cities)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    path, distance = travelling_salesman(distance_matrix)
    print("Optimal path:", path)
    print("Minimum distance:", distance)