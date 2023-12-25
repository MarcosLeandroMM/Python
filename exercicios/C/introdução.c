/*
Variables

In programming, a variable is a container (storage area) to hold data.

To indicate the storage area, each variable should be given a unique name (identifier). Variable names are just the symbolic representation of a memory location. For example:
*/
int playerScore = 95;


// Escape Sequences. Sometimes, it is necessary to use characters that cannot be typed or has special meaning in C programming. For example: newline(enter), tab, question mark etc. In order to use these characters, escape sequences are used.

/*
Escape Sequences
	
		
			Escape Sequences
				Character
		

	
	
		
			\b
				Backspace
		

		
			\f
				Form feed
		

		
			\n
				Newline
		

		
			\r
				Return
		

		
			\t
				Horizontal tab
		

		
			\v
				Vertical tab
		

		
			\\
				Backslash
		

		
			\'
				Single quotation mark
		

		
			\"
				Double quotation mark
		

		
			\?
				Question mark
		

		
			\0
				Null character
		*/	
				

// Constants. If you want to define a variable whose value cannot be changed, you can use the const keyword. This will create a constant. For example:
const double PI = 3.14;


/* C data types - In C programming, data types are declations for variables. This determines the type and size of data associated with variables.

Basic types   - Size(bytes)             -  Format Specifier
int         at least 2, usually 4       -       %d,%i
char                1                   -      %c
float               4                   -      %f
double              8                   -      %lf
short int        2 usually              -      %hd
usigned int      at least 2,usually 4   -      %u
long int         at least 4, usually 8  -      %ld, %li
long long int    at least 8             -      %lld, %lli
usigned long int at least 4             -      %lu

usigned long long int -  at least 8     -      %llu 
signed char                1            -      %c
unsigned char              1            -      %C
long double  at least 10, usually 12 or 16 -   %Lf

*/

// int - Integers are whole numbers that can have both zero, positive and negative values but no decimal values.

// float and double - are used to hold real numbers
// char - Keyword char is used for declaring character type variables.
// void - is an incomplete type. It means "nothing" or "no-type". You can think of void as absent.
// short and long - if you nedd to use a large number, you can use a type specifier long.
// signed and unsigned - In C, signed and unsigned aretypes modifiers. You can alter the data storage of a data type by using them. Signed: allows for storage of both positive and negative numbers. Unsigned: allows for storage of only positive numbers


/* C operators - An operator is a symbol that operates on a value or a variable. For example: + is an operator to perform addition.

C operators arithmetic:

Operator      -    Meaning of Operator
+                  addition or unary plus
-                  subtraction or unary minus
*                  multiplication
/                  division
%                  remainder after division(modulo division)


C Increment and Decrement Operators - C programming has two operators increment ++ and decrement -- to change the values of an operand (constant or variable) by 1.

C Assignment Operators - An assigment operator is used for assigning a value to a variable. The most common assignment operator is =

Operator         Example         Same as
=                a = b           a = b
+=               a += b          a = a + b
-=               a -= b          a = a-b
*=               a *= b          a = a*b
/=               a /= b          a = a / b
%=               a % = b         a = a % b



C Relational Operators - A relational operator checks the relationship between two operands. If the relation is true, ti returns 1; if the relation is false, ir return value 0.

Operator        Meaning of Operator       Example
==              Equal to                  5 == 3 is 0
>               Greater than              5 > 3 is 1
<               Less than                 5 < 3 is 0
!=              Not equal to              5 != 3 is 1
>=              Greater than or equal to  5 >= 3 is 1
<=              Less than or equal to     5 <= 3 is 0




C logical Operators - An expression containing logical operator return either 0 or 1 depending upon wheter expression results true or false.

Operator   Meaning              Example
&&         AND.                 if c = 5 and d = 2 then,
           True only if all     expression 
           operands are true    ((c==5) && (d>5)) equal 0

||         OR.
           True only if either  if c=5 and d=2 then,
           one operand is true   expression
           ((c==5) || (d>5)) equals to 1;
        
!          NOT.
           True only if the
           operands is 0.       if c=5 then,
                                !(c==5) equals to 0.




C bitwise Operators
During computation, mathematical operations like:
addition, subtraction, multiplication, division, etc are converted to bit-level which makes processing faster and saves power

Bitwise operators are used in C programming to perform bit-level operations

Operators    Meaning of Operators
&            AND
|            OR
^            Exclusive OR
"            complement
<<           shift left
>>           shift right



Other operators

Comma Operator - are used to link related expressions together. int a, c = 5, d;

The sizeof operator - is a unary operator that returns the size of data(constants, variables, array, structure,etc).
*/




// Input/Output
#include <stdio.h>

// Integer Output

int main() 
{
    int testInteger = 5;
    printf("Number = %d", testInteger);
    return 0;
 
}

// We use %d format specifier to print int types. Here, the %d inside the quotations will be replaced by the value of testInteger.

// Float and double Output
#include <stdio.h>
int main()
{
    float number1 = 13.5;
    double number2 = 12.4;

    printf("number1 = %f\n", number1);
    printf("number2 = %f", number2);
    return 0;
}

// o print float, we use %f format specifier. Similarly, we use %lf to print double values.


// Print Characters
#include <stdio.h>
int main()
{
    char chr = 'a';
    printf("character = %c", chr);
    return 0;
}

// To print char, we use %c format specifier.



// C input ( scanf( is one of the commonly used function to take input from the user. The scanf() function reads formatted input from the standard input such as keyboards.) )

// Example 5: Integer Input/Output
#include <stdio.h>
int main()
{

    int testeInteger;
    printf("Enter an integer: ");
    scanf("%d", &testeInteger);
    printf("Number = %d", testeInteger);
    return 0;

}

// Float and Double Input/Output
#include <stdio.h>
int main()
{
    float num1;
    double num2;

    printf("Enter a number: ");
    scanf("%f", &num1);
    printf("Enter another number: ");
    scanf("%lf", &num2);

    printf("num1 = %f\n", num1);
    printf("num2 = %lf", num2);

    return 0;
}


// Example 7: C Character I/O
#include <stdint.h>
int main()
{
    char chr;
    printf("Enter a character: ");
    scanf("%c", &chr);
    printf("You entered %c.", chr);
    return 0;
}