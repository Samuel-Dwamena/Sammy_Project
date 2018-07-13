#def get_name():
   # get_name = (input("Enter ur name:"))
    #return get_name
#print(get_name())

#def get_age():
    #get_age = int(input("Enter ur age:"))
    #return get_age
#print(get_age())
def pyramid():
    to_print=1
    going_down = False
    for i in range (0,7):
       for j in range(0,to_print):
           print("*", end="")
       print("")
       #time.sleep(1)
       if to_print == 4:
           going_down = True

       if going_down:
             to_print -= 1
       else:
            to_print += 1

pyramid()
             
         
        
           
