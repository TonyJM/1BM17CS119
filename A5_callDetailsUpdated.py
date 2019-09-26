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
        self.stdC=0
        self.localC=0
        self.isdC=0

    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            x=i.split(",")
            o=CallDetail(*x)
            self.list_of_call_objects.append(o)
            if o.typ=='STD':
                self.stdC+=1
            elif o.typ=='Local':
                self.localC+=1
            elif o.typ=='ISD':
                self.isdC+=1
            

    def disp(self):
        for i in self.list_of_call_objects:
            i.disp()
        print("\nCount :")
        print("STD : ",self.stdC)
        print("Local : ",self.localC)
        print("ISD : ",self.isdC)
            
call1='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000004,9330000003,6,ISD'
list_of_call_string=[call1,call2,call3]
ob=Util()
ob.parse_customer(list_of_call_string)
ob.disp()

