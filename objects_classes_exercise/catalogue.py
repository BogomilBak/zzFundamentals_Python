class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [x for x in self.products if x[0] == first_letter]

    def __repr__(self):
        result_1 = self.products.copy()
        result_1.sort()
        result = f"Items in the {self.name} catalogue:\n"
        for element in result_1:
            if element == result_1[-1]:
                result += element
            else:
                result += element + "\n"
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)