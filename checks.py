from config import authorised_ips
def external_ips(data:list[list[str]]):
    extracted_ip = [line[1] for line in data if not line[1].startswith(authorised_ips)]
    return extracted_ip