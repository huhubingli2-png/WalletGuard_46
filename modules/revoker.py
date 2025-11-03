def generate_revoke_links(address):
    return [
        f"https://revoke.cash/address/{address}?chain=bsc",
        f"https://bscscan.com/tokenapprovalchecker?search={address}"
    ]
