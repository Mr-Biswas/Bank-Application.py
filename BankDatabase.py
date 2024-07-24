#Bank Database Management System

# Operations Performed
# Open New Account
# Deposit Money
# Withdraw Money
# Balance Enquiry
# Show Customer Details
# Close An Account

# Created a database with name SBI_Bank
# Account Table contains "Name | AccNo | DOB | Address | ContactNumber | EmailId | OpeningBalance"
# Amount Table contains "Name | AccNo | Balance"


import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password='123456', database='sbi_bank')
if mydb.is_connected():
    print("Connection Established")


def OpenAcc():
    n=input("Enter the Name: ")
    an=input("Enter the Account Number: ")
    db=input("Enter the Date of Birth: ")
    add=input("Enter the Address: ")
    cn=input("Enter the Conatact Number: ")
    ei=input("Enter the Email: ")
    ob=int(input("Enter the Opening Balance: "))
    data1=(n, an, db, add, cn, ei, ob)
    data2=(n,an,ob)
    sql1=("insert into Accounts values (%s, %s, %s, %s, %s, %s, %s)")
    sql2=("insert into Amount values(%s, %s, %s)")
    a=mydb.cursor()
    a.execute(sql1, data1)
    a.execute(sql2, data2)
    mydb.commit()
    print("Task Accomplished without Any Error.")
    main()

def DepositMoney():
    amount=int(input("Enter the amount to be deposited? "))
    an=input("Enter the Account Number: ")
    b='select Balance from Amount where AccNo=%s'
    data=(an, )
    a=mydb.cursor()
    a.execute(b, data)
    result=a.fetchone()
    bal=result[0]+amount
    sql=('update amount set Balance=%s where AccNo= %s')
    c=(bal, an)
    a.execute(sql, c)
    mydb.commit()
    print("Task Accomplished without Any Error.")
    main()

def WithdrawMoney():
    amount=int(input("Enter the amount to be withdraw? "))
    an=input("Enter the Account Number: ")
    b='select Balance from Amount where AccNo=%s'
    data=(an,)
    a=mydb.cursor()
    a.execute(b, data)
    result=a.fetchone()
    bal=result[0]-amount
    sql=('update amount set balance=%s where AccNo= %s')
    c=(bal, an)
    a.execute(sql, c)
    mydb.commit()
    print("Task Accomplished without Any Error.")
    main()

def Balance():
    an=input('Enter the Account Number: ')
    d='select * from Amount where AccNo=%s'
    data=(an,)
    a=mydb.cursor()
    a.execute(d, data)
    result=a.fetchone()
    print()
    print("Balance for Account Number",an, "is",result[-1])
    main()

def CustomerDetails():
    an=input('Enter the Account Number: ')
    d='select * from Accounts where AccNo=%s'
    data=(an,)
    a=mydb.cursor()
    a.execute(d, data)
    result=a.fetchall()
    for i in result:
        print("The Full Details(Name, AccNo, DOB, Address, PhoneNo, Email, Opening Balance) of a Customer with Account Number", an,"is", i)
    main()

def close():
    an=input("Enter the Account Numner: ")
    sql1='delete from Accounts where AccNo= %s'
    sql2= 'delete from Amount where AccNo= %s'
    data=(an,)
    a=mydb.cursor()
    a.execute(sql1, data)
    a.execute(sql2, data)
    mydb.commit()
    print("Task Accomplished without Any Error.")
    main()

def tata():
        print()
        print("***************************Thanks for trusting SBI.********************************")
        return


def main():
    print( '''
            1. OPENING ACCOUNT
            2. DEPOSIT MONEY
            3. WITHDRAW MONEY
            4. BALANCE ENQUIRY
            5. DISPLAY CUSTOMER DETAILS
            6. CLOSING ACCOUNT
            9. Exit''')
    print()
    choice=input("Enter the Number You want to Perform: ")
    if choice=="1":
        OpenAcc()
    elif choice=="2":
        DepositMoney()
    elif choice=="3":
        WithdrawMoney()
    elif choice=="4":
        Balance()
    elif choice=="5":
        CustomerDetails()
    elif choice=="6":
        close()
    elif choice=="9":
        tata()

    else:
        print('Invalid Choice, Sorry!')
        main()
#Password Protection
x=int(input("Enter the Password:: "))
if x==123456:

    main()
else:
    print("Please Leave!!")
