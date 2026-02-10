def traffic_reader(path)->list:
    with open(path, "r") as file:
        load_csv = [line.strip().split(",") for line in file]
    return load_csv
