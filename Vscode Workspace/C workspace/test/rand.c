#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    //srand(time(NULL));
    int a[10001];
    int count = 0;
    for (int i = 0; i < 1000; i++)
    {
        a[i] = (rand() % 101);
        if (a[i] == 100)
        {
            count++;
        }
    }
    printf("%d", count);
}
