# rational-nums-class-python

Class in Python for rational numbers that symbolyzing like "5/6".

A) __init__ phase:

--> The numerator and denominator of rational number must be an integer in this class.

--> If the user inputs the decimal number(float), __init__ method converts the numerator and denominator to an integer based on mathematical rules.

--> If the user inputs a value other than float or integer, ParameterError occurs.


METHODS:

1) simplify():

    --> This method makes the rational number the simplest if it has no parameter.

    --> If the user gives an integer parameter to this method and if the numerator and the denominator can be divided by parameter
        the method simplifies the rational number with this parameter. Else it returns the same rational number.

        Examples:
            rational(6,12).simplify() --> rational(1,2)
            rational(6,12).simplify(3) --> rational(2,4)
            rational(6,12).simplify(7) --> rational(6,12)
            rational(3.5,7).simplify(3.5) --> rational(1,2)

2) expanse():

     --> This method takes an parameter and expanses the rational number with this parameter.

     --> If the parameter is a decimal number the method returns rational number based on initializing rules.

            Examples:
                rational(2,3).expanse(5) --> rational(10,15)
                rational(1,2).expanse(2.5) --> rational(25,50)

3)value():

    --> This method returns the value of rational number.

        Examples:
            rational(2,1).value() --> 2.0
            rational(3,2).value() --> 1.5




### Writed by Enes CANBAY ###
### Last Update: December/9/2022 ###
