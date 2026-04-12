#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

typedef struct Vector
{
    float val;
    struct Vector *next;
}point;

int Vectors = 1;

point *get_vector(void)
{
    int n;
    printf("Enter the size of vector %d : ",Vectors);
    scanf("%d",&n);
    point *p = malloc(sizeof(point));
    point *head = p;

    for (int i = 0;i<n;i++)
    {
        printf("Enter the value of the %d Dimension: ",i+1);
        scanf("%f",&p->val);
        if (i==n-1)
        break;
        point *temp = malloc(sizeof(point));
        p->next = temp;
        p = p->next;
    }
    Vectors++;
    p->next = NULL;
    
    return head;
}

void print_vector(point *head)
{
    point *pin = head;

    while(pin)
    {
        printf("%f ",pin->val);
        pin = pin->next;
    }
    printf("\n");
}

bool check_len(point *vec1,point *vec2)
{

    point *head = vec1;
    point *head2 = vec2;
    
    while(head && head2)
    {
        head = head->next;
        head2 = head2->next;

    }
    
    return ! head && ! head2;
}

point *add(point *top1,point *top2)
{
    if (!check_len(top1,top2))
    {
        printf("Size not compatible");
        return NULL;
    }
    
    point *head = malloc(sizeof(point));
    point *curr = head;
    
    while(top1 && top2)
    {
        curr->val = top1->val + top2->val;
        top1 = top1->next;
        top2 = top2->next;
        
        if(!(top1 && top2))
        break;
        
        curr->next = malloc(sizeof(point));
        curr = curr->next;
    }
    
    curr->next = NULL;
    return head;
}

point *scale(point *top,int num)
{
    point *head = malloc(sizeof(point));
    point *curr = head;
    
    while(top)
    {
        curr->val = top->val * num;
        top = top->next;

        if(!(top))
        break;

        curr->next = malloc(sizeof(point));
        curr = curr->next;
    }
    
    curr->next = NULL;
    return head;
}

point *sub(point *top1,point *top2)
{
    point *new = scale(top2,-1);
    point *ans = add(top1,new);
    return ans;
}

float dot(point *top1,point *top2)
{
    int ans = 0;
    while(top1 && top2)
    {
        ans += top1->val * top2->val;
        top1 = top1->next;
        top2 = top2->next;
    }
    
    return ans;
    
}

float mag(point *top)
{
    float ans = 0.0;
    while(top)
    {
        ans += top->val * top->val;
        top = top->next;
    }
    return sqrt(ans);
}


point *norm(point *top)
{
    point *head = malloc(sizeof(point));
    point *curr = head;
    
    float num = mag(top);
    while(top)
    {
        curr->val = top->val/num;
        top = top->next;

        if(!(top))
        break;

        curr->next = malloc(sizeof(point));
        curr = curr->next;
        
    }
    curr->next = NULL;
    return head;
}

bool is_equal(point *top1,point *top2)
{
    if (!check_len(top1,top2))
    {
        return false;
    }
    
    while(top1 && top2)
    {
        if (top1->val != top2->val)
        return false;
        top1 = top1->next;
        top2 = top2->next;
    }
    return true;
}
int main(void)
{
    
    point *top = get_vector();
    point *top2 = get_vector();
    point * sum = add(top,top2);

    print_vector(sum);
    print_vector(sub(top,top2));
    print_vector(scale(top,2));
    printf("%f\n",dot(top,top2));

    printf("%.3f\n",mag(top2));
    print_vector(norm(top));
    
    printf("%s",is_equal(top,top2)?"True":"False");
}