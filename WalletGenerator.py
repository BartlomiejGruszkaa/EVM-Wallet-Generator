from web3 import Web3
from eth_account import Account
from mnemonic import Mnemonic


mnemo = Mnemonic("english")

MAIN_NET_HTTP_ENDPOINT = 'https://mainnet.infura.io/v3/a332b48488d64ecf9d1c0588d3179a8e'

def generate_eth_wallets(num_wallets):
    output_file = "wallets.txt"
    with open(output_file, "w") as file:
        for _ in range(num_wallets):
            words = mnemo.generate(strength=256)
            seed = mnemo.to_seed(words, passphrase="")
            w3 = Web3(Web3.HTTPProvider(MAIN_NET_HTTP_ENDPOINT))
            account = Account.from_key(seed[:32])
            private_key = account.key.hex()
            public_key = account.address

            file.write(f"{public_key}\t{private_key}\n")

if __name__ == "__main__":
    num_wallets = int(input("How many wallets do you want?: "))

    generate_eth_wallets(num_wallets)

    print(f"{num_wallets} wallets are in wallets.txt.")



