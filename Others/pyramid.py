def createPyramid(no):
    if not no == 1 or no == no:
        print("*")


no = int(input("Enter a number: "))
createPyramid(no=no)

'''
#include <stdio.h>

int main()
{
    int number,i,j;
    int space;
    printf("Enter a numner: ");
    scanf("%d",&number);
    for (i=1;i<=number;i++)
    {
        if(i==number || i==1|| i==2)
        {   space=number-i;
            for(j=1;j<=space;j++){
                printf(" ");
            }
            for(j=1;j<=i;j++)
            {
                printf("* ");
            }
        }
        else
        {
            space=number-i;
            for(j=1;j<=space;j++){
                printf(" ");
            }
            for(j=1;j<=i;j++){
                space=j;
                if(j==1 || j==i)
                {
                    printf("* ");
                }
                else{
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    return 0;
}

'''
