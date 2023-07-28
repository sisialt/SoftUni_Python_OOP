# from project.computer_store_app import ComputerStoreApp
# computer_store = ComputerStoreApp()
# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
# print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))

def powers_of_two():
    start = 2
    while start <= 128:
        yield start
        start *= 2

print(list(powers_of_two()))