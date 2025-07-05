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
                raise ValueError(f"Digit '{digit}' is invalid for base {base}")
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
        print("\n╔═══════════════════════════════════════════════════╗\n║ Number Base Converter")
        num = input("║ Enter the number (or 'QUIT' to quit): ")
        if num.lower() == "quit":
            break

        try:
            from_base = int(input("║ From base (2-16): "))
            to_base = int(input("║ To base (2-16): "))
            if not (2 <= from_base <= 16) or not (2 <= to_base <= 16):
                print("║ Bases must be between 2 and 16.")
                continue

            result = converter.convert(num, from_base, to_base)
            print(f"║ {num} (base {from_base}) → {result} (base {to_base})")

        except ValueError as e:
            print("Error:", e)

        print("╚═══════════════════════════════════════════════════╝")
