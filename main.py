from src.detection.detect_communities import detect_communities
from src.file_reader import file_reader

def main():
    file_path = input("Informe o caminho do arquivo com os dados: ")

    graph = file_reader(file_path)

    communities = detect_communities(graph)

    print("Comunidades encontradas:")
    for idx, community in enumerate(communities):
        print(f"Comunidade {idx+1}: {community}")

if __name__ == "__main__":
    main()