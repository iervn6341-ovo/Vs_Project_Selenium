#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main()
{
    srand(time(NULL)); //設定亂數種子
    char card[13];
    card[0] = 'A';
    card[1] = '2';
    card[2] = '3';
    card[3] = '4';
    card[4] = '5';
    card[5] = '6';
    card[6] = '7';
    card[7] = '8';
    card[8] = '9';
    card[9] = 'T';
    card[10] = 'J';
    card[11] = 'Q';
    card[12] = 'K';
    char color[4][10] = {"clubs", "diamond", "heart", "spade"};
    int cardarr[52] = {0};
    int temp, count = 0;
    for (int i = 0; i < 52; i++)
    {
        cardarr[i] = i + 1; //填入1~52張卡
    }
    for (int i = 0; i < 1000; i++)
    {
        int randa = rand() % 52;
        int randb = rand() % 52;
        temp = cardarr[randa];
        cardarr[randa] = cardarr[randb];
        cardarr[randb] = temp;
    }
    int sortstr[4][13] = {0};
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 13; j++)
        {
            sortstr[i][j] = cardarr[i * 13 + j];
        }
    }
    /*for (int i = 0; i < 4; i++)
    {
        printf("玩家  ");
        printf("%d", i + 1);
        for (int j = 0; j < 13; j++)
        {
            printf("%s %c ", color[cardarr[i * 13 + j] % 4], card[cardarr[i * 13 + j] / 4]); // 印出排序前排組
        }
        printf("\n");
    }*/
    for (int i = 0; i < 4; i++) //排序
    {
        for (int j = 0; j < 13;)
        {
            if (sortstr[i][j] < sortstr[i][j + 1])
            {
                j += 1;
            }
            else if (sortstr[i][j] > sortstr[i][j + 1])
            {
                temp = sortstr[i][j];
                sortstr[i][j] = sortstr[i][j + 1];
                sortstr[i][j + 1] = temp;
                j = 0;
            }
        }
    }
    for (int i = 0; i < 4; i++)   //check sort
    {
        for (int j = 0; j < 13;j++)
        {
            printf("%d  ",sortstr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    for (int i = 0; i < 4; i++)
    {
        printf("Player");
        printf("%d ", i + 1);
        for (int j = 0; j < 13; j++)
        {
            printf("%s %c ", color[sortstr[i][j] % 4], card[sortstr[i][j] / 4]); // 印出排序後排組
        }
        printf("\n");
    }
    return 0;
}
