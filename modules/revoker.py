def generate_revoke_links(address):
    return [
        f"https://revoke.cash/address/{address}?chain=bsc",
        f"https://bscscan.com/tokenapprovalchecker?search={address}"
    ]
# 功能分支 feature/revoker 添加的注释
print("正在执行 revoker 模块")
