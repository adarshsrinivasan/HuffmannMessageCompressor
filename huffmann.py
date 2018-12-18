class Node:
    class LL:
        def __init__(self,val=None,cou=None):
            self.value=val
            self.count=cou
            self.lc=None
            self.rc=None
            self.prev=None
            self.next=None

    def __init__(self):
        self.head=self.LL()
        self.tail=self.LL()
        self.size=0

def form_link(char,cou):
    n=Node()
    for i in range(len(char)):
        c=n.LL(char[i],cou[i])
        if(n.head.value==None):
            n.head=c
            n.tail=c
            n.size=n.size+1
        else:
            n.tail.next=c
            c.prev=n.tail
            n.tail=c
            n.size=n.size+1
    return(n)

def sort_link(n,sz):
    cur=n.head
    temp=Node().LL()
    for i in range(sz-1):
        cur=n.head
        for h in range(i):
            cur=cur.next
        nn=cur.next
        while(nn.next!=None):
            if(nn.count>cur.count):
                t1=cur.value
                t2=cur.count
                t3=cur.lc
                t4=cur.rc
                cur.value=nn.value
                cur.count=nn.count
                cur.lc=nn.lc
                cur.rc=nn.rc
                nn.value=t1
                nn.count=t2
                nn.lc=t3
                nn.rc=t4
            nn=nn.next
        if(nn.count>cur.count):
            t1=cur.value
            t2=cur.count
            t3=cur.lc
            t4=cur.rc
            cur.value=nn.value
            cur.count=nn.count
            cur.lc=nn.lc
            cur.rc=nn.rc
            nn.value=t1
            nn.count=t2
            nn.lc=t3
            nn.rc=t4
    temp_tail=n.head
    while(temp_tail.next!=None):
        temp_tail=temp_tail.next
    n.tail=temp_tail
    return(n)
    
def make_list(s):
    j=0
    char=[]
    coun=[]
    for i in s:
        if i not in char:
            char.append(i)
    for i in char:
        for h in s:
            if(i==h):
                j=j+1
        coun.append(j)
        j=0
    return(char,coun)

def make_tree(n,sz):
    cur=n.head
    print("Input List:")
    t=n.head
    while(t.next!=None):
        print(t.value)
        t=t.next
    print(t.value)
    if((n.head.next!=n.tail) & (n.head.next!=None)):
        c=Node().LL((n.tail.value + n.tail.prev.value),(n.tail.count + n.tail.prev.count))
        c.rc=n.tail.prev
        c.lc=n.tail
        n.tail.prev.prev.next=c
        c.prev=n.tail.prev.prev
        n.tail=c
        cur=n.head
        print("------------------------------------")
        while(cur.next!=None):
            print(cur.value,cur.count,"->")
            cur=cur.next
        print(cur.value,cur.count)
        print("------------------------------------")
        return(make_tree(sort_link(n,sz-1),sz-1))

    elif(n.head.next==n.tail):
        c=Node().LL((n.tail.value + n.head.value),(n.tail.count + n.head.count))
        c.rc=n.head
        c.lc=n.tail
        n.head=c
        n.tail=c
        print("------------------------------------")
        print(n.head.value)
        return(n)
    else:
        return(n)  

def huff_traverse(n,char,seg=[],flag=0):
    print("seg:",seg)
    if(n.value!=char):
        print("checking...:",n.value)
        if((n.lc!=None) & (n.rc!=None)):
            seg.append(0)
            a,flag=huff_traverse(n.lc,char,seg)
            if(a=='no match'):
                seg.pop()
                flag=2
            if(flag!=1):
                if((len(seg)!=0)&(a!='no match')):
                    seg.pop()
                seg.append(1)
                b,flag=huff_traverse(n.rc,char,seg)
                if(b=='no match'):
                    seg.pop()
                return(b,flag)
            else:
                return(a,1)
        else:
            return('no match',None)
    else:
        print("match:",char,n.value)
        return(seg,1)

def isnum(s):
    try:
        int(s)
        return(True)
    except ValueError:
        return(False)

def code_gen(n,char,coun):
    code=[]
    su=0
    fs=0
    for i in char:
        s=huff_traverse(n.head,i,[],0)
        if(isnum(str(s[0]))!=True):
            s=s[0]
        code.append(s)
    print("--------------------------------------------------------------------------")
    print("Character\t\tCode\t\tFrequency\t\tBits")
    print("--------------------------------------------------------------------------")
    for i in range(len(char)):
        print(char[i],"\t\t",code[i],"\t\t",coun[i],"\t\t\t",len(code[i])*coun[i])
        su=su+len(code[i])*coun[i]
        fs=fs+coun[i]
    print("\n\nTotal Bits Required(Actual):",fs*8)
    print("\nTotal Bits Required(Now):",su)
    print("\nPercentage of memory saved:",100-int(((su/(fs*8))*100)),"%")
    
    

        
    

n=Node()
l=list(input("Enter the Message:"))
char,coun=make_list(l)
n=form_link(char,coun)
n=sort_link(n,len(char))
n=make_tree(n,len(char))
code_gen(n,char,coun)
