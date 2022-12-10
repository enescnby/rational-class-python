"""
Class in python for rational nums.
"""

class Rational:

    """
    Class in Python for rational numbers that symbolyzing like "5/6".\n\n
    A) __init__ phase:\n
    --> The numerator and denominator of rational number must be an integer in this class.\n
    --> If the user inputs the decimal number(float), __init__ method converts the numerator
    and denominator to an integer based on mathematical rules.\n
    --> If the user inputs a value other than float or integer, ParameterError occurs.
    """

    class ParameterError(Exception):

        """
        This is an error for Rational class.\n
        Rational class' parameters must be an integer or float.\n
        If user gives invalid parameter this error occurs.
        """

        def __init__(self,error_source):
            message="The parameters of rational num's must be an integer or float not"
            self.msg=message+" "+error_source

        def __str__(self):
            return str(self.msg)

    class ZeroDenominatorError(Exception):

        """
        It is an error for Rational class.\n
        Rational num's denominator can not be 0.\n
        If user gives 0 to denominator this error occurs.
        """

        def __init__(self,message="Denominator can not be 0."):
            self.msg=message

        def __str__(self):
            return str(self.msg)

    def __init__(self,top:int,bottom:int):
        if bottom==0:
            raise Rational.ZeroDenominatorError()

        if bottom!=0:
            if not isinstance(top,int) and not isinstance(top,float):
                error_source=type(top).__name__
                raise Rational.ParameterError(error_source)

            if not isinstance(bottom,int) and not isinstance(bottom,float):
                error_source=type(bottom).__name__
                raise Rational.ParameterError(error_source)

        if isinstance(top,int) and isinstance(bottom,int):
            self.top=top
            self.bottom=bottom

        elif isinstance(top,float) and isinstance(bottom,float):
            top_part_list=str(top).split(".")
            bottom_part_list=str(bottom).split(".")
            exp_num=max(len(top_part_list[1]),len(bottom_part_list[1]))
            self.top=int(top*10**exp_num)
            self.bottom=int(bottom*10**exp_num)

        elif isinstance(top,float) and isinstance(bottom,int):
            top_part_list=str(top).split(".")
            exp_num=len(top_part_list[1])
            self.top=int(top*10**exp_num)
            self.bottom=bottom*10**exp_num

        elif isinstance(top,int) and isinstance(bottom,float):
            bottom_part_list=str(bottom).split(".")
            exp_num=len(bottom_part_list[1])
            self.bottom=int(bottom*10**exp_num)
            self.top=top*10**exp_num


    def __str__(self):
        return str(self.top)+"/"+str(self.bottom)

    def __add__(self,other):
        top=(self.bottom*other.top)+(self.top*other.bottom)
        bottom=self.bottom*other.bottom
        return Rational(top,bottom)

    def __sub__(self,other):
        top=self.top*other.bottom-self.bottom*other.top
        bottom=self.bottom*other.bottom
        if self>other:
            return Rational(abs(top),bottom)
        return Rational(top,bottom)

    def __mul__(self,other):
        top=self.top*other.top
        bottom=self.bottom*other.bottom
        return Rational(top,bottom)

    def __truediv__(self,other):
        top=self.top*other.bottom
        bottom=self.bottom*other.top
        return Rational(top,bottom)

    def __eq__(self,other):
        if self.top*other.bottom==self.bottom*other.top:
            return True
        return False

    def __ne__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self!=value_other:
            return True
        return False

    def __gt__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self>value_other:
            return True
        return False

    def __lt__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self<value_other:
            return True
        return False

    def __ge__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self>=value_other:
            return True
        return False

    def __le__(self,other):
        value_self=self.top/self.bottom
        value_other=other.top/other.bottom
        if value_self<=value_other:
            return True
        return False

    def expanse(self,expansation_num):

        """
            --> This method takes an parameter and expanses
            the rational number with this parameter.\n
            --> If the parameter is a decimal number the method
            returns rational number based on initializing rules.\n
            Examples:\n
            \trational(2,3).expanse(5) --> rational(10,15)\n
            \trational(1,2).expanse(2.5) --> rational(25,50)

        """

        top=self.top*expansation_num
        bottom=self.bottom*expansation_num
        return Rational(top,bottom)

    def simplify(self,num=None):

        """
        --> This method makes the rational number the simplest if it has no parameter.\n
        --> If the user gives an integer parameter to this method and if the numerator and
        the denominator can be divided by parameter the method simplifies
        the rational number with this parameter.
        Else it returns the same rational number.
        \nExamples:
        \trational(6,12).simplify() --> rational(1,2)\n
        \trational(6,12).simplify(3) --> rational(2,4)\n
        \trational(6,12).simplify(7) --> rational(6,12)\n
        \trational(5,10).simplify(2.5) --> rational(2,4)
        """

        if num is None:
            if abs(self.top)>abs(self.bottom):
                small_num=self.bottom
            else:
                small_num=self.top
            for i in range(1,abs(small_num)+1):
                if self.top%i==0 and self.bottom%i==0:
                    gcd=i
            return Rational(int(self.top/gcd),int(self.bottom/gcd))

        if isinstance(num,int):
            if self.top%num==0 and self.bottom%num==0:
                return Rational(int(self.top/num),int(self.bottom/num))
            print(f"Can not be simplify with {num}")
            return Rational(self.top,self.bottom)

        if isinstance(num,float) and self.top%num==0 and self.bottom%num==0:
            return Rational(int(self.top/num),int(self.bottom/num))
        print(f"Can not be simplify with {num}")
        return Rational(self.top,self.bottom)


    def value(self):

        """
        --> This method returns the value of rational number.\n
        Examples:
        \trational(2,1).value() --> 2.0\n
        \trational(3,2).value() --> 1.5

        """

        value=self.top/self.bottom
        return value
