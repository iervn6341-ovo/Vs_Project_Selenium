#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int arr[], int n)
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < i; ++j)
        {
            if (arr[j] > arr[i])
            {
                int temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
    for (int i = 0; i < 9; i++)
    {
        printf("%d\n", arr[i]);
    }
}

int main()
{
    int arr[10] = {5, 7, 2, 8, 4, 6, 3, 8, 7};
    int temp;
    /*for (int i = 0; i < 9; i++)
    {
        if (arr[i] > arr[i + 1])
        {
            temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
            i = 0;
        }
    }*/
    bubble_sort(arr, 9);
}