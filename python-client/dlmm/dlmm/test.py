from dlmm import DLMM_CLIENT
from solders.pubkey import Pubkey

# RPC URL for the Solana devnet
RPC = "https://api.devnet.solana.com"

# Replace this with the pool address you're testing
pool_address = Pubkey.from_string(
    "3W2HKgUa96Z69zzG3LK1g8KdcRAWzAttiLiHfYnKuPw5")

# Initialize the DLMM client
dlmm = DLMM_CLIENT.create(pool_address, RPC)

# Print the DLMM client object to verify
print(dlmm)
