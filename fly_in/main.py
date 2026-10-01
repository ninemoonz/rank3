from config_parsing import Parser
from class_model import HubsFactory

if __name__ == "__main__":
    file_name = "./maps/medium/02_circular_loop.txt"
    drones, raw_hubs, raw_connections = Parser.file_opener(file_name)
    clean_hubs = Parser.parse_hubs(raw_hubs)
    clean_conn = Parser.parse_connections(raw_connections)
    print("[Hubs Info]")
    for hub in clean_hubs:
        print(hub)
    print("[Produce hubs in factory]")
    produced_hubs = HubsFactory().make_hubs(clean_hubs)
    for ahub in produced_hubs:
        ahub.describe()
    print("[Connection Info]")
    for conn in clean_conn:
        print(conn)
