from modules.scanner import scan_wallet
from modules.revoker import generate_revoke_links
import sys

def main(wallet_file):
    with open(wallet_file, 'r') as f:
        wallets = [line.strip() for line in f if line.strip()]
    
    for address in wallets:
        print(f"\n[+] 正在扫描钱包: {address}")
        approvals = scan_wallet(address)
        if approvals:
            print(f" 发现 {len(approvals)} 个授权记录")
            for a in approvals:
                print(f" - Token: {a['token']}, Spender: {a['spender']}, Amount: {a['amount']}")
            links = generate_revoke_links(address)
            print(" 🔗 撤销链接:")
            for link in links:
                print(f" - {link}")
        else:
            print(" 无授权记录或查询失败")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python main.py <wallet_list.txt>")
    else:
        main(sys.argv[1])
