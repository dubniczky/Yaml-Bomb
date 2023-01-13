import json
import sys
import yaml

with open(sys.argv[1], encoding='utf8') as f:
    loaded = yaml.safe_load(f)
    
json_str = json.dumps(loaded)

print(len(json_str)) # Print number of bytes
