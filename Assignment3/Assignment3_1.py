##########################################################
# File Name :   Assignment3_1.py
# Description : Used to calculate the sum of list elements
# Author :      Nikita Shahaji Omase
# Date :        15/05/2025
###########################################################

def Addition(num):
    li = []
    n1= 0
    sum = 0
    print("Enter the element");
    for i in range (num):
        n1 = int(input())
        li.append(n1)
        sum = sum + n1
    
    return sum     
 
def main():
    
    no = 0
    iRet = 0
    print("Enter the number of elements");
    no = int(input())
    iRet = Addition(no)
    print("Addition of elements are : ",iRet);
   
if __name__ == "__main__":
    main()