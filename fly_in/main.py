from config_parsing import Parser
from class_model import HubsFactory

if __name__ == "__main__":
    file_name = "./maps/medium/03_priority_puzzle.txt"
    parsed_hubs, parsed_connections = Parser.file_opener(file_name)
    hubs_list = HubsFactory().make_hub(parsed_hubs)
    for hub in hubs_list:
        hub.describe()
        print()
