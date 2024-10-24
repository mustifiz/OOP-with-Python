#Dictionary, Mapping and List Examples in OOP

class DataManager:
    def __init__(self):
        # Dictionary: anahtar-değer çiftleri
        self.data_dict = {"apple": 10, "banana": 5, "orange": 8}
        
        # List: birden fazla öğeyi saklamak için liste kullanımı
        self.data_list = ["apple", "banana", "orange"]
        
        # Mapping: bir veri yapısı (mesela bir dictionary) üzerinde çalışmayı sağlayan bir fonksiyon
        # map() fonksiyonu kullanılacak
        self.data_prices = [2.5, 1.5, 3.0]  # Fiyatlar listesi

    # Dictionary içindeki bir veriyi güncelleme ve ekleme
    def update_or_add_to_dict(self, fruit, quantity):
        self.data_dict[fruit] = quantity
        print(f"Updated dictionary: {self.data_dict}")

    # Listeye yeni bir öğe ekleme
    def add_to_list(self, fruit):
        if fruit not in self.data_list:
            self.data_list.append(fruit)
        print(f"Updated list: {self.data_list}")
    
    # Mapping kullanarak meyve fiyatlarını yüzdeyle güncelleme
    def update_prices(self, percentage_increase):
        # Fiyatları yüzdeyle artırıyoruz (mapping kullanımı)
        self.data_prices = list(map(lambda price: price * (1 + percentage_increase/100), self.data_prices))
        print(f"Updated prices: {self.data_prices}")

    # Dictionary içindeki tüm meyvelerin toplam miktarını hesaplama
    def get_total_quantity(self):
        total_quantity = sum(self.data_dict.values())
        print(f"Total quantity of fruits: {total_quantity}")
        return total_quantity
    
    # Listede meyvenin olup olmadığını kontrol etme
    def is_fruit_in_list(self, fruit):
        return fruit in self.data_list

# Sınıfı kullanma
manager = DataManager()

# Dictionary'de veri güncelleme ve ekleme
manager.update_or_add_to_dict("apple", 15)  # Elmanın miktarını 15 yapar
manager.update_or_add_to_dict("grape", 20)  # Üzüm ekler

# Listeye yeni meyve ekleme
manager.add_to_list("grape")  # Üzümü listeye ekler

# Fiyatları yüzde 10 artırma (mapping ile)
manager.update_prices(10)

# Toplam meyve miktarını hesaplama
manager.get_total_quantity()

# Listede meyve olup olmadığını kontrol etme
print(manager.is_fruit_in_list("banana"))  # True
print(manager.is_fruit_in_list("kiwi"))  # False
