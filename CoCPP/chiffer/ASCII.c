#include <stdio.h>
#include <string.h>
#include <stdint.h>

#define MAX_ARR 256



int ASCII()
{
    int i = 0;
    uint32_t roll;
    uint32_t shift;
    int numstr[MAX_ARR];
    char string[MAX_ARR];
    printf("Enter CodePhrase: ");
    fgets(string, MAX_ARR, stdin);
    printf("Enter Roll <= 9: ");
    scanf("%u", &roll);
    printf("Enter Shift <= 9: ");
    scanf("%u", &shift);
    printf("Roll %u, Shift %u\n", roll, shift);
    printf("Code is: ");

    for (i = 0; i < strlen(string); i++)
    {
        
        if (string[i] > 0)
        {
            numstr[i] = string[i];
            if (numstr[i] != 10)
            {
                numstr[i] += roll;
                if (numstr[i] > 126)
                {
                    numstr[i] = numstr[i] - 126;
                }
                if (numstr[i] > 255)
                {
                    numstr[i] = numstr[i] - 255;
                }
                if (numstr[i] < 32)
                {
                    numstr[i] = numstr[i] + 32;
                }
                printf("%c", numstr[i]);

                
                roll += shift; 
            }
            
            
        }else
        {
            printf("NULL");
        }
        
        
        
    }
    
    
}


int main()
{
    ASCII();
    return 0;
}