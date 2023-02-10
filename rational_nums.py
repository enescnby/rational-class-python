"""
Class in python for rational numbers.

  ## Writed by Enes Canbay ##
  ## Last Update: February/7/2023 ##
"""

class Rational:

    """
    Class in Python for rational numbers that symbolyzing like "5/6".\n\n
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
        This is an error for Rational class.\n
        Rational num's denominator can not be 0.\n
        If user gives 0 to denominator this error occurs.
        """

        def __init__(self,message="Denominator can not be 0."):

            self.msg=message

        def __str__(self):

            return str(self.msg)

    def __init__(self,numerator: int | float, denominator:int | float):

        if denominator==0:
            raise Rational.ZeroDenominatorError()

        if denominator!=0:
            if not isinstance(numerator,int) and not isinstance(numerator,float):
                error_source=type(numerator).__name__
                raise Rational.ParameterError(error_source)

            if not isinstance(denominator,int) and not isinstance(denominator,float):
                error_source=type(denominator).__name__
                raise Rational.ParameterError(error_source)

        if isinstance(numerator,int) and isinstance(denominator,int):
            self.numerator=numerator
            self.denominator=denominator

        elif isinstance(numerator,float) and isinstance(denominator,float):
            numerator_part_list=str(numerator).split(".")
            denominator_part_list=str(denominator).split(".")
            exp_num=max(len(numerator_part_list[1]),len(denominator_part_list[1]))
            self.numerator=int(numerator*10**exp_num)
            self.denominator=int(denominator*10**exp_num)

        elif isinstance(numerator,float) and isinstance(denominator,int):
            numerator_part_list=str(numerator).split(".")
            exp_num=len(numerator_part_list[1])
            self.numerator=int(numerator*10**exp_num)
            self.denominator=denominator*10**exp_num

        elif isinstance(numerator,int) and isinstance(denominator,float):
            denominator_part_list=str(denominator).split(".")
            exp_num=len(denominator_part_list[1])
            self.denominator=int(denominator*10**exp_num)
            self.numerator=numerator*10**exp_num

    def setnum(self, numerator : int | float) -> None:

        """Sets the numerator"""

        self.numerator = numerator
        Rational.__init__(self, self.numerator, self.denominator)

    def setden(self, denominator) -> None:

        """Sets the denominator."""

        self.denominator = denominator

        Rational.__init__(self, self.numerator, self.denominator)

    def getnum(self) -> int:

        """Returns the numerator."""

        return self.numerator

    def getden(self) -> int:

        """Returns the denominator."""

        return self.denominator

    def __str__(self):

        return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self,other):

        numerator=(self.denominator*other.numerator)+(self.numerator*other.denominator)
        denominator=self.denominator*other.denominator
        return Rational(numerator,denominator).simplify()

    def __sub__(self,other):

        numerator=self.numerator*other.denominator-self.denominator*other.numerator
        denominator=self.denominator*other.denominator
        if self>other:
            return Rational(abs(numerator),denominator)
        return Rational(numerator,denominator)

    def __mul__(self,other):

        numerator=self.numerator*other.numerator
        denominator=self.denominator*other.denominator
        return Rational(numerator,denominator)

    def __truediv__(self,other):

        numerator=self.numerator*other.denominator
        denominator=self.denominator*other.numerator
        return Rational(numerator,denominator)

    def __eq__(self,other):

        if self.numerator*other.denominator==self.denominator*other.numerator:
            return True
        return False

    def __ne__(self,other):

        value_self=self.numerator/self.denominator
        value_other=other.numerator/other.denominator
        if value_self!=value_other:
            return True
        return False

    def __gt__(self,other):

        value_self=self.numerator/self.denominator
        value_other=other.numerator/other.denominator
        if value_self>value_other:
            return True
        return False

    def __lt__(self,other):

        value_self=self.numerator/self.denominator
        value_other=other.numerator/other.denominator
        if value_self<value_other:
            return True
        return False

    def __ge__(self,other):

        value_self=self.numerator/self.denominator
        value_other=other.numerator/other.denominator
        if value_self>=value_other:
            return True
        return False

    def __le__(self,other):

        value_self=self.numerator/self.denominator
        value_other=other.numerator/other.denominator
        if value_self<=value_other:
            return True
        return False

    def expanse(self,expansation_num : int | float):

        """
            --> This method takes an parameter and expanses
            the rational number with this parameter.\n
            --> If the parameter is a decimal number the method
            returns rational number based on initializing rules.\n
        """

        numerator=self.numerator*expansation_num
        denominator=self.denominator*expansation_num
        return Rational(numerator,denominator)

    def simplify(self, num : None | int | float = None):

        """
        --> This method makes the rational number the simplest if it has no parameter.\n
        --> If the user gives an integer parameter to this method and if the numerator and
        the denominator can be divided by parameter the method simplifies
        the rational number with this parameter.
        Else it returns the same rational number.
        """

        if num is None:
            if abs(self.numerator)>abs(self.denominator):
                small_num=self.denominator
            else:
                small_num=self.numerator
            for i in range(1,abs(small_num)+1):
                if self.numerator%i==0 and self.denominator%i==0:
                    gcd=i
            return Rational(int(self.numerator/gcd),int(self.denominator/gcd))

        if isinstance(num,int):
            if self.numerator%num==0 and self.denominator%num==0:
                return Rational(int(self.numerator/num),int(self.denominator/num))
            print(f"Can not be simplify with {num}")
            return Rational(self.numerator,self.denominator)

        if isinstance(num,float) and self.numerator%num==0 and self.denominator%num==0:
            return Rational(int(self.numerator/num),int(self.denominator/num))
        print(f"Can not be simplify with {num}")
        return Rational(self.numerator,self.denominator)


    def value(self) -> float:

        """This method returns the value of rational number."""

        value=self.numerator/self.denominator
        return value
