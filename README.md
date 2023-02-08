# RATIONAL NUMBERS CLASS IN PYTHON

[Github Repository](https://github.com/enescnby/rational-class-python)

Class in Python for rational numbers that symbolyzed like "5/6".


## Initializing Phase:

+ The numerator and denominator of rational number must be an integer in this class.

- If the user inputs the decimal number(float), __init__ method converts the numerator and denominator to an integer based on mathematical rules.

* If the user inputs a value other than float or integer, ParameterError occurs.

+ If the user gives '0' to the denominator, ZeroDenominatorError occurs.


## Methods:

1 \) **setnum** \(numerator : int \| float\) -> None :

      This method sets the numerator with given parameter.

2 \) **setden** \(denominator : int \| float\) -> None :

      This method sets the denominator with given parameter.

3 \) **getnum** \(\) -> int :

      This method returns the numerator.

4 \) **getden** \(\) -> int :

       This method returns the denominator.

5 \) **simplify** \(simplification_num : None \| int \| float\) -> Rational :

    --> This method makes the rational number the simplest if it has no parameter.

    --> If the user gives an integer parameter to this method and if the numerator and the denominator can be divided by parameter
        the method simplifies the rational number with this parameter. Else it returns the same rational number.

        Examples:

            Rational(6,12).simplify() --> Rational(1,2)
            Rational(6,12).simplify(3) --> Rational(2,4)
            Rational(6,12).simplify(7) --> Rational(6,12)
            Rational(5,10).simplify(2.5) --> Rational(2,4)

6 \) **expanse** \(expansation_num : int \| float\) -> Rational :

     --> This method takes an parameter and expanses the rational number with this parameter.

     --> If the parameter is a decimal number the method returns rational number based on initializing rules.

            Examples:

                Rational(2,3).expanse(5) --> Rational(10,15)
                Rational(1,2).expanse(2.5) --> Rational(25,50)

7 \) **value** \(\) -> float:

    --> This method returns the value of rational number.

        Examples:

            Rational(2,1).value() --> 2.0
            Rational(3,2).value() --> 1.5



> ###### *Writed by [Enes Canbay](https://github.com/enescnby)*
> ###### *Last Update: February/8/2023*
