# -----------------------------------------
# This file needs to be executed outside of
# the tbears environment or this won't work
# -----------------------------------------
import sys, json, os

script_path = os.path.dirname(os.path.realpath(sys.argv[0]))
root_dir_path = os.path.normpath(script_path + (os.sep + os.pardir))

testnet_uri = "https://bicon.net.solidwallet.io/api/v3"
local_uri = "http://localhost:9000/api/v3"

def editTbearsConfig( network ):
    os.chdir(root_dir_path)
    tbears_cli_config = "tbears_cli_config.json"
    with open(tbears_cli_config, 'r+') as f:
        data = json.load(f)
        if network == "testnet":
            data['uri'] = testnet_uri
        elif network == "local":
            data['uri'] = local_uri
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

def editJSConfig( network ):
    os.chdir(root_dir_path + '/web/src/js/config')
    web_config= "config.js"
    uri = local_uri if network == "local" else testnet_uri
    lines = open(web_config).read().splitlines()
    for it in range(len(lines)):
        if "url" in lines[it]:
            lines[it] = '  url : "' + uri + '",'
    open(web_config,'w').write('\n'.join(lines))


if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == 'testnet' or sys.argv[1] == 'local'):
        editTbearsConfig(sys.argv[1])
        editJSConfig(sys.argv[1])

        print("Switched to ", sys.argv[1])
    else:
        print("Add only 'local' or 'testnet' as an argument")
