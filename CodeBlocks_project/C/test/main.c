/*
   testcase{
		2*x^4+2*x^3+3*x^2+7*x^1+1
		4*x^4+1*x^3+6*x^2+9*x^1+11

   }
 */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct linklist_{
	int inte;
	int exp;
	struct linklist_ *next;
}linklist_;
int main(){
	//var_init
	char input1[30],input2[30];
	int count=0,max_exp=0;
	struct linklist_ *first,*second,*third,*fourth,*fifth;
	first = malloc(sizeof(linklist_));
	second = malloc(sizeof(linklist_));
	third = malloc(sizeof(linklist_));
	fourth = malloc(sizeof(linklist_));
	fifth = malloc(sizeof(linklist_));

	{
		first -> next = second;
		second -> next = third;
		third -> next = fourth;
		fourth -> next = fifth;
		fifth -> next = NULL;

		first -> inte = 0;
		first -> exp = 0;
		second -> inte = 0;
		second -> exp = 0;
		third -> inte = 0;
		third -> exp = 0;
		fourth -> inte = 0;
		fourth -> exp = 0;
		fifth -> inte = 0;
	}

	struct linklist_ *point_list;
	point_list = first;

	printf("第一個多項式:");
	scanf("%s",input1);

	while(1){
		if(input1[count] == '\0'){
			break;
		}
		if(input1[count] == '*'){
			point_list -> inte = input1[count-1] -48;
		}
		if(input1[count] == '^'){
			point_list -> exp = input1[count+1] -48;
		}
		count ++;
		if(point_list -> inte !=0 && point_list -> exp != 0){
			point_list = point_list -> next;
		}
	}
	count = 0;
	point_list = first;
    printf("\n%d\n",point_list -> inte);
	printf("第二個多項式:");
	scanf("%s",input2);

	while(1){
		if(input2[count] == '\0'){
			break;
		}
		if(input2[count] == '*' ){
			if(input2[count+3] != point_list -> exp + '0'){
				printf("輸入與第一個多項式不同的指數，請重新執行程式 !");
				return -1;
			}
			printf("\n%d\n",point_list -> inte);
			point_list -> inte = point_list + input2[count-1] -48;
			printf("\n%d\n",point_list -> inte);
		}

		count ++;
		if(input2[count] == '+'){
			point_list = point_list -> next;
		}
	}
	point_list = first;
	//printf("%d", point_list -> inte);
	//printf("%d * x ^ %d + %d * x ^ %d + %d * x ^ %d + %d * x ^ %d + %d", first -> inte , first -> exp , second -> inte , second -> exp , third -> inte , third -> exp , fourth -> inte , fourth -> exp , fifth -> inte );

	return 0;
}
