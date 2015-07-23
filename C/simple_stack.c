#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENTS 10
#define TRUE 1
#define FALSE 0

struct array_stack
{
	int top;
	int capacity;
	int *array;
} *s;

int isEmpty()
{
	return (s->top == -1);
}

int isFull()
{
	return (s->top == s->capacity -1);
}

void push(int data)
{
	if (isFull())
	{
		printf("\tStack overflow.\n");
	}
	else
	{
		s->array[++s->top] = data;
	}
}

int pop()
{
	if (isEmpty())
	{
		printf("Empty Stack.\n");
		return 0;
	}
	else
	{
		return (s->array[s->top--]);
	}
}

int main()
{
	s = (struct array_stack *)malloc(sizeof(struct array_stack));
	s->capacity = MAX_ELEMENTS;
	s->top = -1;
	s->array = malloc(s->capacity * sizeof(int));
	int option,data;

	while(TRUE)
	{
		printf("1: isEmpty()\n2: isFull()\n3: push(...)\n4: pop()\n5: Exit\n");
		if((scanf("%d",&option)) == 1)
		{
		    if (option==1)
		    {
			printf("\t%d\n",isEmpty());
		    }
		    else if (option==2)
		    {
			printf("\t%d\n",isFull());
		    }
		    else if (option==3)
		    {
			printf("\t");
			scanf("\t%d",&data);
			push(data);
		    }
		    else if (option==4)
		    {
			printf("\t%d\n",pop());
		    }
		    else if (option==5)
		    {
			break;
		    }
		}
		else
		{
		    printf("Bad input.Quitting.\n");
		    break;
		}
	}

}
