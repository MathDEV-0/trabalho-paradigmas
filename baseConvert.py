class BaseConverter:
    def __init__(self):
        self.digits = "0123456789ABCDEF"

    def convert_to_decimal(self, number: str, base: int) -> int:
        number = number.upper()
        decimal = 0
        power = 0

        for digit in reversed(number):
            value = self.digits.index(digit)
            if value >= base:
                raise ValueError(f"Dígito '{digit}' inválido para base {base}")
            decimal += value * (base ** power)
            power += 1
        return decimal

    def convert_from_decimal(self, decimal: int, base: int) -> str:
        if decimal == 0:
            return "0"

        result = ""
        while decimal > 0:
            remainder = decimal % base
            result = self.digits[remainder] + result
            decimal //= base
        return result

    def convert(self, number: str, from_base: int, to_base: int) -> str:
        decimal = self.convert_to_decimal(number, from_base)
        return self.convert_from_decimal(decimal, to_base)


if __name__ == "__main__":
    converter = BaseConverter()

    while True:
        print("\n=== Conversor de Bases Numéricas ===")
        num = input("Digite o número (ou 'sair' para encerrar): ")
        if num.lower() == "sair":
            break

        try:
            from_base = int(input("Base de origem (2-16): "))
            to_base = int(input("Base de destino (2-16): "))
            if not (2 <= from_base <= 16) or not (2 <= to_base <= 16):	
                print("As bases devem estar entre 2 e 16.")
                continue

            result = converter.convert(num, from_base, to_base)
            print(f"{num} (base {from_base}) → {result} (base {to_base})")

        except ValueError as e:
            print("Erro:", e)

