from config import *
def identify_suspects(data:list[list[str]])->dict:
    suspects = {}
    massage = ("EXTERNAL_IP", "SENSITIVE_PORT", "LARGE_PACKET", "NIGHT_ACTIVITY")
    for line in data:
        ip = line[1]
        current_suspicions = []
        if ip not in authorised_ips:
            current_suspicions.append(massage[0])
        if line[3] in sensitive_ports:
            current_suspicions.append(massage[1])
        if int(line[5]) > 5000:
            current_suspicions.append(massage[2])
        if int(line[0][11]) == 0 and int(line[0][12]) <6:
            current_suspicions.append(massage[3])

        if current_suspicions:
            if ip in suspects:
                suspects[ip].extend(current_suspicions)
            else:
                suspects[ip] = current_suspicions
    return suspects
def suspects_filter(identify_suspects)->dict:
    return {k:v for k,v in identify_suspects.items() if len(v)>1}