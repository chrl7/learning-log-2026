# OOP
class Car:
    def __init__(self, brand, color, speed=0):
        self.brand = brand
        self.color = color
        self.speed = speed

    def drive(self, speed_increment):
        self.speed += speed_increment
        print(f"{self.brand} is now traveling at {self.speed} km/h")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} has stopped.")

my_car = Car("Toyota", "Silver")
my_car.drive(40)    
my_car.drive(20)     
my_car.stop()  


# ====================================------------------------ Exercise -------------------======================================
# Atribut: judul, penulis, jumlah_halaman, dan halaman_terbaca (default 0)
# Method baca(jumlah) → menambah halaman_terbaca sebanyak jumlah, lalu cetak progress, misal: "Kamu sudah membaca 50 dari 300 halaman."
# Method info() → mencetak judul dan penulis dalam format rapi  
class Book :
    def __init__(self, title, author, number_of_pages, pages_read=0):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.pages_read = pages_read
    
    def read(self, total) :
        self.pages_read += total
        
        if self.pages_read > self.number_of_pages :
            self.pages_read = self.number_of_pages
            
        print(f"You have read {self.pages_read} pages out of {self.number_of_pages} pages")
        
    def info(self):
        print("===== Book Information =====")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("==========================")
        
book1 = Book("the psychology of money", "Morgan Housel", 238)

book1.info()

book1.read(20)
book1.read(10)
        