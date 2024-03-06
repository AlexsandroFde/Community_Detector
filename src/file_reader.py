import csv

def file_reader(file_path):
    graph = {}

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            user, *connections = row
            graph[user] = connections

    return graph