#include <stdio.h>

#define MAX_ARR 25

int main()
{
    char text = "";

    printf("Write text: ");
    fgets(text, MAX_ARR, stdin);
    printf("%c, %d", text, text);

    return 0;
}