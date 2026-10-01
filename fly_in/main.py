from config_parsing import Parser
from class_model import HubsFactory, ConnectionsFactory


def tester(val: int) -> None:
    file_name = "./maps/medium/01_dead_end_trap.txt"
    drones, raw_hubs, raw_connections = Parser.file_opener(file_name)
    clean_hubs = Parser.parse_hubs(raw_hubs)
    clean_conn = Parser.parse_connections(raw_connections)
    if val == 0:
        print("[Produce hubs in factory]")
        produced_hubs = HubsFactory().make_hubs(clean_hubs)
        for ahub in produced_hubs:
            ahub.describe()
    if val == 1:
        print("[Produce Connection in factory]")
        produced_conn = ConnectionsFactory().make_connections(clean_conn)
        for conn in produced_conn:
            conn.describe()


if __name__ == "__main__":
    tester(1)
