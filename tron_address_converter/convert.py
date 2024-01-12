import base58
import hashlib

def sha256(msg):
    return hashlib.sha256(bytes.fromhex(msg)).hexdigest()

class TronConverter:
    @staticmethod
    def to_hex(address: str) -> str:
        """TRON address to EVM address"""
        return "0x" + base58.b58decode(address).hex()[2:-8]

    @staticmethod
    def from_hex(address: str) -> str:
        """EVM address to TRON address"""
        addr = '41' + address[2:]
        doubleSha256 = sha256(sha256(addr))
        checkSum = doubleSha256[:8]
        _address = bytes.fromhex(addr + checkSum)
        return base58.b58encode(_address).decode()