def intro(File=0,**data):
    print("File No. : 0{}".format(File))
    for key,value in data.items():
        print ("{} is {}".format(key,value))



intro (1,FirstName="Harshal",LastName="Joshi")
intro (2,FirstName="Mohan",LastName="Sharma",Age=25,Phone=12345)
intro (3,FirstName="Vikram",LastName="Verma",Email="vikramverma@gmail.com",Country="India",Age=25,Phone=12345)

