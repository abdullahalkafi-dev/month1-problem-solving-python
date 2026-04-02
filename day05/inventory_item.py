class InventoryItem:
    def __init__(self, sku, name, price, quantity):
        self.sku = sku
        self.name = name
        if not isinstance(price, (int, float)):
            raise TypeError("price data type not allowed")
        if not isinstance(quantity, int):
            raise TypeError("quantity data type not allowed")
        if price <= 0:
            raise ValueError("price must be greater than 0")
        if quantity < 0:
            raise ValueError("quantity must be greater than or equal to 0")
        self._price = float(price)
        self._quantity = quantity

    def add_stock(self, qty: int) -> int:
        if not isinstance(qty, int):
            raise TypeError("qty data type not allowed")
        if qty <= 0:
            raise ValueError("qty must be greater than 0")
        self._quantity = self._quantity + qty
        return self._quantity

    def remove_stock(self, qty: int) -> int:
        if not isinstance(qty, int):
            raise TypeError("qty data type not allowed")
        if qty <= 0:
            raise ValueError("qty must be greater than 0")
        if qty > self._quantity:
            raise ValueError("not enough stock")
        self._quantity = self._quantity - qty
        return self._quantity

    def set_price(self, new_price: float) -> float:
        if not isinstance(new_price, (int, float)):
            raise TypeError("price data type not allowed")
        if new_price <= 0:
            raise ValueError("price must be greater than 0")
        self._price = float(new_price)
        return self._price

    def inventory_value(self) -> float:
        return self._price * self._quantity