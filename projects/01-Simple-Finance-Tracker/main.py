import csv
from datetime import date



# ============================================== CUSTOM EXCEPTIONS ==============================================
class InvalidAmount(Exception):
    pass

class InsufficientBalance(Exception):
    pass

 
 
# ============================================== TRANSACTION CLASSES ==============================================
class Transaction:
    def __init__(self, description, count, day=None):
        
        if count<=0:
            raise InvalidAmount(f"The number of {description} transactions must be greater than 0! (Value provided: {count})")
        
        self.description=description
        self.count=count
        self.day=day if day else date.today().isoformat()
        
    def show(self):
        print(f"[{self.day}] {self.description} : Rp.{self.count}")
        
        
class Revenue(Transaction) :
    def show(self):
        print(f"[{self.day}] + {self.description} : Rp.{self.count} (Revenue)")
    
    
class Expenditure(Transaction) :
    def show(self):
        print(f"[{self.day}] - {self.description} : Rp.{self.count} (Expenditures)")
        


# ============================================== WALLET CLASS (WITH FILE I/O) ==============================================
class Wallet:
    def __init__(self, owner):
        self.owner=owner
        self.transactions=[]
        
    def add_transaction(self, transaction):  
        if isinstance(transaction, Expenditure):
            current_balance=self.get_balance()
            if transaction.count > current_balance:
                raise InsufficientBalance(f"Failed to withdraw Rp.{transaction.count}! {self.owner} currently has a balance of only Rp.{current_balance}")
        
        self.transactions.append(transaction)
        
    def get_balance(self):
        total_revenue=0
        total_expenditure=0
        
        for t in self.transactions:
            if isinstance(t, Revenue):
                total_revenue +=t.count
            elif isinstance(t, Expenditure):
                total_expenditure +=t.count
        return total_revenue - total_expenditure
    
    def show_all(self):
        print(f"=====--- wallet {self.owner} ---=====")
        if not self.transactions:
            print("No transactions yet")
        else:
            for t in self.transactions:
                t.show()
        print("="*35)
        print(f"total balance : Rp.{self.get_balance()}\n")
         
    
    # ------------------------- SAVE TO CSV -------------------------
    def save_to_csv(self, filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer=csv.writer(file)
            
            writer.writerow(["type", "description", "count", "day"])
            
            for t in self.transactions:
                trans_type="Revenue" if isinstance(t, Revenue) else "Expenditure"
                writer.writerow([trans_type, t.description, t.count, t.day])
                
        print(f"Successfully saved {len(self.transactions)} transactions to the file {filename}.")
        
    # ------------------------- LOAD FROM CSV -------------------------
    def load_from_csv(self, filename):
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader=csv.reader(file)
                header=next(reader)
                
                loaded_count=0
                for row in reader:
                    trans_type, description, count_str, day=row
                    count=int(count_str)
                    
                    if trans_type == "Revenue":
                        obj=Revenue(description, count, day)
                    elif trans_type == "Expenditure":
                        obj=Expenditure(description, count, day)
                    else:
                        continue
                    
                    self.transactions.append(obj)
                    loaded_count +=1
            print(f"Successfully loaded {loaded_count} transactions from the file {filename}")
            
        except FileNotFoundError:
            print(f"The file {filename} was not found. Starting with an empty wallet.")
            


wallet = Wallet("Chrl")

wallet.add_transaction(Revenue("Monthly Salary", 5000000))
wallet.add_transaction(Expenditure("Buy Coffee", 25000))
wallet.save_to_csv("transactions.csv")

# Program restarted → data is still there
new_wallet = Wallet("Chrl")
new_wallet.load_from_csv("transactions.csv")
new_wallet.show_all()