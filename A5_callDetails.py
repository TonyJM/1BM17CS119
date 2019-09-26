class CallDetail:
    def __init__(self,c,r,d,t):
        self.cal=c
        self.rcv=r
        self.dur=d
        self.typ=t

    def disp(self):
        print("\nCaller : ",self.cal)
        print("Receiver : ",self.rcv)
        print("Duration : ",self.dur)
        print("Type : ",self.typ)            

class Util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            x=i.split(",")
            o=CallDetail(*x)
            self.list_of_call_objects.append(o)

    def disp(self):
        for i in self.list_of_call_objects:
            i.disp()
            
call1='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000004,9330000003,6,ISD'
list_of_call_string=[call1,call2,call3]
ob=Util()
ob.parse_customer(list_of_call_string)
ob.disp()

