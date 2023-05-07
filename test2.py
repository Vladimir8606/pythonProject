class Switch:
    def info(self):
        print(f"Hostname: {self.hostname}\nModel: {self.model}")

    def generate_interfaces(self, intf_type, number_of_intf):
        interfaces = [f"{intf_type}{number}" for number in range(1, number_of_intf + 1)]
        self.interfaces=interfaces


sw1 = Switch()
sw1.hostname = 'sw1'
sw1.model = 'Cisco 3850'
sw1.generate_interfaces('Fa0/', 10)
print(sw1.interfaces)
sw1.info()
print('123')