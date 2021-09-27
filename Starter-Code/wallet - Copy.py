import subprocess
import json

command = 'php derive -g --mnemonic="ritual jungle crack head imitate exotic someone reflect goddess dinner install leader" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
