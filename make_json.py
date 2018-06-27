import json


def write_to_json(seed_list, fp):
    """
    This method takes in the seed list and the file path. Then:
    1. opens the file and loads it's data into a variable
    2. updates the SeedList section in the variabe and closes the file
    3. reopens the file to write the variable changes to it
    :param seed_list: list of nodes whose rpc ports are working,
    thus we assume the p2p ports are working as well
    :param fp: file path to the protocol currently being used
    :return: doesn't really do anything, I just felt the need to return something
    """
    protocol = None  # initializing the variable to prevent possible errors
    with open(fp, 'r') as file_path:
        protocol = json.load(file_path)
        protocol["ProtocolConfiguration"]["SeedList"] = seed_list
        file_path.close()
    with open(fp, 'w') as file_path:
        json.dump(protocol, file_path, indent=4)
        file_path.close()
    return True
