class rational:
    def __init__(self,top,bottom):
        if type(top)==int and type(bottom)==int: 
            self.top=top
            self.bottom=bottom

        elif type(top)==float and type(bottom)==float:
            top_part_list=str(top).split(".")
            bottom_part_list=str(bottom).split(".")
            exp_num=max(len(top_part_list[1]),len(bottom_part_list[1]))
            self.top=int(top*10**exp_num)
            self.bottom=int(bottom*10**exp_num)
        
        elif type(top)==float or type(bottom)==int:
            top_part_list=str(top).split(".")
            exp_num=len(top_part_list[1])
            self.top=int(top*10**exp_num)
            self.bottom=bottom*10**exp_num

        elif type(top)==int or type(bottom)==float:
            bottom_part_list=str(bottom).split(".")
            exp_num=len(bottom_part_list[1])
            self.bottom=int(bottom*10**exp_num)
            self.top=top*10**exp_num
    
    def __str__(self):
        return str(self.top)+"/"+str(self.bottom)

    def __add__(self,other):
        top=(self.bottom*other.top)+(self.top*other.bottom)
        bottom=self.bottom*other.bottom
        return rational(top,bottom)

    def __sub__(self,other):
        top=self.top*other.bottom-self.bottom*other.top
        bottom=self.bottom*other.bottom
        if self>other:
            return rational(abs(top),bottom)
        else:
            return rational(top,bottom)

    def __mul__(self,other):
        top=self.top*other.top
        bottom=self.bottom*other.bottom
        return rational(top,bottom)

    def __truediv__(self,other):
        top=self.top*other.bottom
        bottom=self.bottom*other.top
        return rational(top,bottom)

    def __eq__(self,other):
        x=rational(self.top,self.bottom).simplify()
        y=rational(other.top,other.bottom).simplify()
        if x.top==y.top and x.bottom==y.bottom:
            return True
        else:
            return False
    
    def __ne__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self!=value_other:
            return True
        else:
            return False

    def __gt__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self>value_other:
            return True
        else:
            return False
    
    def __lt__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self<value_other:
            return True
        else:
            return False

    def __ge__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self>=value_other:
            return True
        else:
            return False

    def __le__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self<=value_other:
            return True
        else:
            return False

    def expanse(self,expansation_num):
        top=self.top*expansation_num
        bottom=self.bottom*expansation_num
        return rational(top,bottom)

    def simplify(self):
        if abs(self.top)>abs(self.bottom):
            small_num=self.bottom
        else:
            small_num=self.top
        for i in range(1,abs(small_num)+1):
            if self.top%i==0 and self.bottom%i==0:
                gcd=i
        return rational(int(self.top/gcd),int(self.bottom/gcd))
    
a=rational(2,3.55)
print(a.simplify())