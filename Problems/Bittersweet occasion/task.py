# work with the variable `child`
# class Drinks():
#     pass
#
#
# class Pastry():
#     pass
#
#
# class Sweets():
#     pass
#
# class PumpkinJuice(Drinks):
#     pass
#
# class CauldronCake(Pastry):
#     pass
#
# class ChocolateFrog(Sweets):
#     pass
#
# child = PumpkinJuice

if issubclass(child, Drinks):
    print("Drinks")
elif issubclass(child, Pastry):
    print("Pastry")
elif issubclass(child, Sweets):
    print("Sweets")
