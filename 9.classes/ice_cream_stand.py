from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """ This class is specific kind of restaurant. """

    def __init__(self, name, cuisine_type, number_served, list_of_flavors):
        super().__init__(name, cuisine_type, number_served=0)
        self.flavors = list_of_flavors

    def print_all_icecream_flavors(self):
        for flavor in self.flavors[:-1]:
            print(f"{flavor},", end=" ", flush=True, )
        print(self.flavors[-1])
