# tron-address-converter
Package for converting TRON address > EVM address | EVM address > TRON address
Based on https://tronscan.org/#/tools/code-converter/tron-ethereum-address
and https://github.com/wemaketech/tron-format-address/blob/master/lib/crypto.ts

# Installation

```bash
pip install tron-address-converter
```

# Usage

```python
import tron_address_converter

evm_wallet = tron_address_converter.to_hex("TXXmULCEzRo6JfxUP1LYfmzbiKUezUvUNj")
# 0xec830e98468d23f54c58174bb9a3671fcc440ff2
tron_wallet = tron_address_converter.from_hex("0xec830e98468d23f54c58174bb9a3671fcc440ff2")
# TXXmULCEzRo6JfxUP1LYfmzbiKUezUvUNj

print(evm_wallet) # 0xec830e98468d23f54c58174bb9a3671fcc440ff2
print(tron_wallet) # TXXmULCEzRo6JfxUP1LYfmzbiKUezUvUNj
```