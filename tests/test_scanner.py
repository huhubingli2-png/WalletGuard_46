from modules.scanner import scan_wallet

def test_scan_wallet():
    test_address = "0x0000000000000000000000000000000000001004"
    result = scan_wallet(test_address)
    assert isinstance(result, list)
