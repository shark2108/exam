
class Shop:
    def init(self,name,description,len,price):
        self.name=name
        self.disc=description
        self.len=len
        self.price=price
    def summa(self):
        a=int(self.len*self.price)
        return f'{a} сум'
    def name_(self):
        return f'название {self.name},{self.disc},{self.len},{self.price}'
    
if name=='main':
    d=Shop('Macbook','777\9',10,1000)
    print(d.summa())
    print(d.name_())
