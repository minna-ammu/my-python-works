class Users:
    data=[
        {"id":1,"username":"john","email":"j56john@gmail.com","password":"john@2034"},
        {"id":2,"username":"peter","email":"p890@gmail.com","password":"ptr34"},
        {"id":3,"username":"jyothisha","email":"jtop@gmail.com","password":"jyths"},
        {"id":4,"username":"madavan","email":"m678davan@gmail.com","password":"mad@56"},
        {"id":5,"username":"sara","email":"saraok@gmail.com","password":"sweetiee"} ]
    
    def get(self):                                                 # listing  all (1)
        return self.data
    def retrive(self,id):
        return [u    for u in self.data    if u.get("id")==id]     # orennathinte details edukkn  (2)
    def post(self,newid):                                            #  add new users details   (3)            
        self.data.append(newid)
    def destroy(self,id):                                            #  to delete one id (4)
        del_id=[ u     for u in self.data    if u.get("id")==id][0]
        self.data.remove(del_id)
    def put(self,id,values):                                         #  e values vachitt an update cheyyuka . ath kodukknm; values nn
        updt=[up     for up in self.data    if up.get("id")==id][0]  #  to update  (5)
        print(values)
        pos=self.data.index(updt)   # index position vachittupdate cheyynm.pos for position
        self.data[pos]=values
    
    


obj1=Users()
# print(obj1.get())            #(1)


# print(obj1.retrive(2))        #(2)


# new_user={"id":6,"username":"ami","emil":"a90mi@gmail.com","password":"ami@2021"}     #(3)
# obj1.post(new_user)
# print(obj1.get())


# obj1.destroy(3)                  #(4)
# print(obj1.get())       


dta={"id":4,"username":"madavi","email":"m678davie@gmail.com","password":"madv@56"}
obj1.put(4,dta)                  #(5)
# print(obj1.get())