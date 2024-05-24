from prettytable import PrettyTable

# Tabloyu oluştur
table = PrettyTable()
table.field_names = ["Ad", "Soyad", "Yaş"]

# Verileri ekle
table.add_row(["John", "Doe", 28])
table.add_row(["Jane", "Smith", 25])
table.add_row(["Michael", "Johnson", 32])

# Tabloyu yazdır
print(table)

"""
        tree.insert("", "end", values=("21.08.2023", ))
        tree.insert("", "end", values=("22.08.2023", ))
        tree.insert("", "end", values=("23.08.2023", ))
        tree.insert("", "end", values=("24.08.2023", ))
        tree.insert("", "end", values=("25.08.2023", ))
        tree.insert("", "end", values=("26.08.2023", ))
        tree.insert("", "end", values=("27.08.2023", ))
        tree.insert("", "end", values=("28.08.2023", ))
        tree.insert("", "end", values=("29.08.2023", ))
"""