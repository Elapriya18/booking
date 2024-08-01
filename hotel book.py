from datetime import date
class hotel:
    def __init__(self):
        pass
    def check_in(self,name,addres, phone):
        pass
    def room_service(self,room_no):
        self.rooms={}
        self.available_rooms={'std':[101,102],'delux':[201,202]}
        self.roomprice={1:2000,2:3000}
        pass
    def display_occupied(self):
        pass
    def check_out(self,room_number):
        pass
    def start_app(self):
        while True:
            print('welcome 5star hotel')
            print("1.check_in")
            print("2.room_service")
            print("3.display_occupied rooms")
            print("4.check _out")
            print("5.exit")
            choice=input("enter your choice(1-3):")
            if choice=='1':
                name=input ("enter your client name:")
                address=input("enter address:")
                phone=input("enter cotact no:")
                self.check_in(name,address,phone)
            elif choice=='2':
                room_no=int(input("enter room number:"))
                room_price=int(input("enter room price :"))
                self.room_service(room_no)
            elif choice=='3':
                self.display_occupied()
            elif choice=='4':
                room_number=int(input("enter room number:"))
                self.check_out(room_number)
            elif choice=='5':
             break
            else:
                print("valid choice. please try again.")
h=hotel()
h.start_app()
                    
                
            
