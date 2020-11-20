from Scripts import MongoHandlers
MongoHandlers.drop()

print("Application On CRUD ")
choice = input("Enter y to continue and n to break")
while(choice == 'y'):
    print("1.Create  2.Search  3.Update  4.Delete")
    ch = int(input("Enter Operation Choice"))
    if (ch==1):
        my_list = [
          { "name": "Amy", "address": "Apple st 652"},
          { "name": "Hannah", "address": "Mountain 21"},
          { "name": "Michael", "address": "Valley 345"},
          { "name": "Sandy", "address": "Ocean blvd 2"},
          { "name": "Betty", "address": "Green Grass 1"},
          { "name": "Richard", "address": "Sky st 331"},
          { "name": "Susan", "address": "One way 98"},
          { "name": "Vicky", "address": "Yellow Garden 2"},
          { "name": "Ben", "address": "Park Lane 38"},
          { "name": "William", "address": "Central st 954"},
          { "name": "Chuck", "address": "Main Road 989"},
          { "name": "Viola", "address": "Sideway 1633"}
        ]


        MongoHandlers.create(my_list)
        print("Database Created")
    if(ch==2):
        query = input("Enter name to search")
        Query = {"name": query}
        MongoHandlers.my_search(Query)

    if(ch==3):
        f_query = input("Enter the name to be replaced")
        f_update = {"name": f_query}
        t_query = input("Enter new name ")
        t_update = {"$set": {"name": t_query}}
        MongoHandlers.oupdate(f_update, t_update)


        my_query = {"address": {"$regex": "^P"}}
        new_values = {"$set": {"name": "Minnie"}}
        MongoHandlers.update(my_query, new_values)
    if(ch==4):
        d_query = input("Enter name to delete")
        DQuery = {"name": d_query}
        MongoHandlers.delete(DQuery)
    choice = input("Do you want to continue?(y/n)")
if(choice=='n'):
    print("End Task!")