from prettytable import PrettyTable

table = PrettyTable()


table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.border = False

table_method2 = PrettyTable()
table_method2.add_column("Pokemon Name", ["Pikachu", "Squietle", "Charmander"])
table_method2.add_column("Type", ["Electric", "Water", "Fire"])
table_method2.align["Pokemon Name"] = "l"
print(table)

print(table_method2)
