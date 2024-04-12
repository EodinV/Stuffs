#include <stdio.h>
#include <string.h>
#include <stdint.h>

#define MAX_ARR 256

int IICSA()
{
    int i = 0;
    uint32_t roll;
    uint32_t shift;
    char yepno;
    int numstr[MAX_ARR];
    char string[MAX_ARR];
    printf("Enter your problem: ");
    fgets(string, MAX_ARR, stdin);
    printf("\nDo you know R/S? y/n: ");
    fgets(yepno, MAX_ARR, stdin);
    if (yepno == "Y" || yepno == "y")
    {
        printf("Enter roll: ");
        scanf("%u", roll);
        printf("Enter shift: ");
        scanf("%u", shift);
        for (i = 0; i < strlen(string); i++)
        {
            
        }
        //remember if roll becomes bigger than 123 or 255 
        
        /* ask for R/S and do all dechiffring */
    }
    else
    {
        for (i = 0; i < strlen(string); i++)
        {
            /* code */
        }
        //remember if roll becomes bigger than 123 or 255
        //double forloop for roll and shift, list in list ROLL, SHIFT, (text)
        /* bruteforce it and print all possible */
    }
    

}



int main()
{
    return 0;
}