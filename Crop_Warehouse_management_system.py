import xlrd
import xlwt
import openpyxl as op
import matplotlib.pyplot as plt
def vieway(year):
    loc = ("C:/Users/yasharth dubey/Downloads/CropsDataFile.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(0,sheet.nrows):
        if(sheet.cell_value(i,2)==year):
            print(sheet.row_values(i))
        
def viewac(crop):
    loc = ("C:/Users/yasharth dubey/Downloads/CropsDataFile.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    a = [ ]
    b = [ ]
    c=[ ]
    d=[ ]
    for i in range(0,sheet.nrows):
        if(sheet.cell_value(i,4)==crop):
            a.append(sheet.cell_value(i,2))
            b.append(sheet.cell_value(i,6))
    sum = 0
    for i in range(0,len(a)):
        h=0
        for k in c: 
            if(k == a[i]) : 
                h  = 1 
        if(h==0):
            for j in range(0,len(a)):
                if(a[i]==a[j]):
                    sum = sum + b[j]
            c.append(a[i])
            d.append(sum)
            sum=0            
    for i in range (len(c)):
        for j in range(i + 1, len(c)):
            if(c[i] > c[j]):
                temp = c[i]
                c[i] = c[j]
                c[j] = temp
                temp = d[i]
                d[i] = d[j]
                d[j] = temp
    plt.xlabel("Year")
    plt.ylabel("Production")
    plt.plot(c,d)
    plt.show()

def write_file(State_Name,District_Name,Crop_year,Season,Crop,Area,Production):
    Crop_yeara  = int(Crop_year)
    wb = op.load_workbook("C:/Users/yasharth dubey/Downloads/CropsDataFile.xlsx")
    ws = wb.get_sheet_by_name("Sheet1")
    ws.append([State_Name,District_Name,Crop_yeara,Season,Crop,Area,Production])
    wb.save(filename = 'C:/Users/yasharth dubey/Downloads/CropsDataFile.xlsx')
    wb.close()
login = input("Type the login id:")
flag = 0
flag1 = 0
loc = ("C:/Users/yasharth dubey/Downloads/LOGINID.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
for i in range(0,sheet.nrows):
    if(sheet.cell_value(i,0)==login):
        flag = 1
        password = int(input("enter the password:"))
        for j in range(0,sheet.nrows):
            if(sheet.cell_value(j,1)==password):
                flag1 = 1
        if(flag1 == 0):
            print("Wrong password,program terminating")
            exit()
if(flag1 == 1):
    print("welcome ADMIN-"+login)
    print("Choose a option,ADD or VIEW:",end=" ")
    option = input()
    if(option == "ADD"):
        State_Name = input("Type the State name:")
        District_Name = input("Type the District name:")
        Crop_year = input("Type the crop year:")
        Season = input("Type the Season:")
        Crop = input("Type the Crop:")
        Area = input("Type the area:")
        Production = input("Type the production:")
        write_file(State_Name,District_Name,Crop_year,Season,Crop,Area,Production)
    elif(option == "VIEW"):
        option2 = input("Do you want to view by YEAR or CROP:")
        if(option2 == "YEAR"):
            year = int(input("enter the year you want to see:"))
            vieway(year)
        elif(option2 == "CROP"):
            crop = input("enter the crop you want to see:")
            viewac(crop)    
elif(flag == 0):
    print("LOGIN FAILED")
    option3 = input("do you want to login as user,YES or NO:")
    if(option3=="YES"):
        option4 = input("Do you want to view by YEAR or CROP:")
        if(option4 == "YEAR"):
            year = int(input("enter the year you want to see:"))
            vieway(year)
        elif(option4 == "CROP"):
            crop = input("enter the crop you want to see:")
            viewac(crop) 
    else:
        print("thanks for visiting!")
        exit()



                








