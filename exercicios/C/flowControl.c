/* C if...else Statement
The syntax of the if statement in C programing is:
if(test expression)
{
    code
}


*/

// Program to display a number if it is negative
/*
#include <stdio.h>
int main() {
    int number;

    printf("Enter an integer: ");
    scanf("%d", &number);

    // true if number is less than 0
    if(number < 0) 
    {
        printf("You entered %d.\n", number);
    }

    printf("The if statement is easy. ");
    
    return 0;
}
*/


// if...else

/* #include <stdio.h>
int main()
{
    int number;
    printf("Enter an integer: ");
    scanf("%d", &number);

    // True if the remainder is 0
    if(number % 2 == 0)
    {
        printf("%d is an even integer.", number);
    }
    else
    {
        printf("%d is an odd integer.", number);
    }

    return 0;
}
*/


// if...else if
/* #include <stdio.h>
int main ()
{
    int number1, number2;
    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    //checks if the two integers are equal
    if(number1 == number2)
    {
        printf("Result: %d = %d", number1,number2);    
    }
    else if(number1 > number2)
    {
        printf("Result: %d > %d", number1,number2);
    }
    else
    {
        printf("Result: %d < %d",number1,number2);
    }

    return 0;
}
*/


// Nested if...else
// It is possible to include an if...else statement inside the body of another if...else statement.
// This program given below relates two integers using either <,> and = similar to the if...else ladder's example. However, we will use a nested if...else statement to solve this problem.
#include <stdio.h>
int main()
{
    int number1, number2;
    printf("Enter two integers. ");
    scanf("%d %d", &number1, &number2);

    if(number1 >= number2)
    {
        if(number1 == number2){
            printf("Result: %d = %d", number1,number2);
        }
        else {
            printf("Result: %d > %d", number1, number2);
        }
    }
    else {
            printf("Result: %d < %d", number1,number2);
         }

    return 0;
}



/*
C for Loop -  In programming, a loop is used to repeat a block of code until the specified condition is met.
C programing has three types of loops:
1.for loop
2. while loop
3.do...while loop

for loop syntax
for(initializationStatement; testExpression. updateStatement)
{
    // statements inside the body of loop
}

*/

#include <stdio.h>

int main(){
    int i;

    for(i = 1; i < 11; ++i)
    {
        printf("%d ", i);
    }

    return 0;
}