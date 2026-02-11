from config import heavy_file
def weight_tags(data:list[list[str]]):
    extracted_by_weight = ["LARGE" if int(line[5].strip()) > heavy_file else "NORMAL" for line in data]
    return extracted_by_weight
def inquiries(data:list[list[str]])->dict:
    ip_list = [row[1] for row in data]
    return {ip:ip_list.count(ip) for ip in set(ip_list)}
def map_port_protocol(data:list[list[str]])->dict:
    return {int(line[3]):line[4] for line in data}
