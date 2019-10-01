import sys, json, os

testnet_uri = "https://bicon.net.solidwallet.io/api/v3"
local_uri = "http://localhost:9000/api/v3"

def editTbearsConfig( network ):
    os.chdir("/work")
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


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == 'testnet' or sys.argv[1] == 'local':
            editTbearsConfig(sys.argv[1])

            print("Switched to ", sys.argv[1])
        else:
            print("Add only 'local' or 'testnet' as an argument")
    else:
        print("Add only 'local' or 'testnet' as an argument")
