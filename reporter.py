from config import heavy_file
def weight_tags(data:list[list[str]]):
    extracted_by_weight = ["LARGE" if int(line[5].strip()) > heavy_file else "NORMAL" for line in data]
    return extracted_by_weight