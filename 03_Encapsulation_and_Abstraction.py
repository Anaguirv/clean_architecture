from abc import ABC, abstractmethod

class Account(ABC):
    """Abstracción: sólo define operaciones."""
    @abstractmethod
    def deposit(self, amount: float): ...
    @abstractmethod
    def withdraw(self, amount: float): ...


class BankAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0):
        # Encapsulamiento: estado interno “privado”
        self._owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Monto debe ser positivo")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Fondos insuficientes")
        self._balance -= amount

    # Encapsulado: método interno no expuesto
    def _apply_fee(self):
        self._balance -= 5.0
        

if __name__ == "__main__":
    acount_test = BankAccount("arnoldo", 5000)

    print(f"Cuenta creada para {acount_test._owner}, con un monto inicial de: ${acount_test._balance}")
    
    acount_test.deposit(25000)
    print(f"Balance actualizado: ${acount_test._balance}")

    acount_test.withdraw(3000)
    print(f"Balance actualizado: ${acount_test._balance}")

    acount_test._apply_fee()
    print(f"Balance actualizado: ${acount_test._balance}")
