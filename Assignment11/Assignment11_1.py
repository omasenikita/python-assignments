
i = 1
def Series(no):
    global i 
    if(i<=no):
        print(i)
        i = i + 1   
        Series(no)
    
def main():
    no = 0
    print("Enter a number:")
    no = int(input())
    
    Series(no)    
if __name__=="__main__":
    main()
