from src import Parser, HubsFactory, ConnectionsFactory, DronesFactory


def tester(val: int) -> None:
    file_name = "./maps/medium/01_dead_end_trap.txt"
    drones, raw_hubs, raw_connections = Parser.file_opener(file_name)
    clean_drones = Parser.parse_drones(drones)
    clean_hubs = Parser.parse_hubs(raw_hubs)
    clean_conn = Parser.parse_connections(raw_connections)
    if val == 0:
        print("\n===Produce hubs in factory===\n")
        produced_hubs = HubsFactory().make_hubs(clean_hubs, clean_drones)
        for ahub in produced_hubs:
            ahub.describe()
    if val == 1:
        print("\n===Produce Connection in factory===\n")
        produced_conn = ConnectionsFactory().make_connections(clean_conn)
        for conn in produced_conn:
            conn.describe()
    if val == 2:
        print("\n===Produce Drone in factory===\n")
        produced_drones = DronesFactory().make_drones(clean_drones)
        for adrone in produced_drones:
            adrone.describe()


if __name__ == "__main__":
    for i in range(3):
        tester(i)
