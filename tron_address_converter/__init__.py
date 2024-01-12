try:
    from tron_address_converter.convert import TronConverter
except ImportError:
    from .convert import TronConverter

to_hex = TronConverter.to_hex
from_hex = TronConverter.from_hex

__all__ = [
    'TronConverter', 
    'to_hex',
    'from_hex'
]
