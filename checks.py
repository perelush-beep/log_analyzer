from config import *
def external_ips(data:list[list[str]]):
    extracted_ip = [line[1] for line in data if not line[1].startswith(authorised_ips)]
    return extracted_ip
def port_filter(data:list[list[str]]):
    extracted_ports = [line for line in data if line[3].strip() in sensitive_ports]
    return extracted_ports
def weight_filter(data:list[list[str]]):
    extracted_by_weight = [line for line in data if int(line[5].strip()) > heavy_file]
    return extracted_by_weight