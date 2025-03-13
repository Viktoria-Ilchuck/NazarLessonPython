def calc():
    print('Shopping Calculator')
    l=[]
    while True:
        p=input('Enter product name or "done":')
        if p=='done':
           break;
        c=float(input('Enter price:'))
        l.append((p,c))
        total=0;
        print('Your products:');
        for i in l:
            print(i[0],' - ',i[1]);
            total+=i[1]
            print('Total:',total)
calc()