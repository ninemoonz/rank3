from config_parsing import Parser
from class_model import HubsFactory

if __name__ == "__main__":
    file_name = "./maps/medium/03_priority_puzzle.txt"
    drones, raw_hubs, raw_connections = Parser.file_opener(file_name)
    clean_hubs = Parser.parse_hubs(raw_hubs)
    for one_hub in clean_hubs:
        print(one_hub)