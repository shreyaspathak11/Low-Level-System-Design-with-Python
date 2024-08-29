# players:alpha,beta,gamma,delta;trump:s;self:alpha;cards:s3;beta:s10;delta:s5;gamma:ca 
input_string = input()
hash_map = {}
input_string = input_string.split(';')
for parts in input_string:
    key,value = parts.split(':')
    if key == "players":
        players = value.split(',')
        hash_map[key] = players
    if key == "trump":
        hash_map[key] = value
    if key == "self":
        hash_map[key] = value
    if key == "cards":
        hash_map[key] = value

