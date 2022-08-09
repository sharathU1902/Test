#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void Delay(int n)
{
    for(int i=0;i<32767;i++)
    for(int j=0;j<=32767;j++)
    {}
}
int choice,k,i=0;
unsigned long amount =100000, deposite, withdraw;
char transaction ='y',display;
char password[10],card[20],scancard[20]="XXXX1234";
char c=' ',ATMpin='1234';
void main()
{
    printf("\nPlase insert a ATM card:\n");
    gets(card);
    if(strcmp(card,scancard)==0)
    {
        printf("\nEnter a PIN:");
        while (i<4)
        {
        password[i]= getch();
        c=password[i];
        if(c==3) 
        break;
        else
        printf("*");
        i++;
        }
        printf("\n\nPlese wait Transaction is in Processing");
        Delay(10000);
    do
    {
        printf("\nWelcome to SBI bank ATM"); 
        Delay(10000);
        printf("\n1.Check the balance\n 2.Withdraw cash\n 3.Deposit cash\n 4.Quit\n"); 
        /* 1. option for check the balence
           2. option for withdraw cash
           3. option for deposite cash
           4. exit*/
        printf("\nEnter your choice:");   
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("\nAvailable Balance is: %lu",amount);
            break;
        case 2:
            label: printf("\nEnter the Amount to Withraw:");
            scanf("%lu",&withdraw);
            if(withdraw>amount-500)
            {
                printf("\nPlease wait Transaction is in Processing");
                Delay(10000);

                printf("\nInsufficient Balence");
            }
            else if(withdraw%100!=0) 
            {
                printf("\nPlease Enter the amount in multiples of 100: ");
                goto label;
            }
            else
            {
            amount=amount-withdraw;
            printf("\nPlease wait Transaction is in Processing");
            Delay(10000);

            printf("\nPlease collect Your cash");
            Delay(10000);

            printf("\n DO you want to display your amount(Y/N)");
            fflush(stdin);
            scanf("%c",&display);

            if(display=='y'|| display=='Y')
            printf("\nAvailable balence: %lu",amount);
            else
            printf("Thanks For using SBI ATM services");
            exit(1);
            }
            break;

        case 3:
            printf("\nEnter the amount to deposite:\n");
            scanf("%lu",&deposite);

            amount=amount+deposite;

            printf("\nYour Balence:%lu",amount);
        break;
        case 4:
            printf("\nThanks for using SBI ATM services");
            exit(1);
        break;

        default:
            printf("\nEnter valid option");
            break;
        }
        printf("\nDo you want Another transcation(Y/N):");
        fflush(stdin);
        scanf("%c",&transaction);
        if(transaction=='n'|| transaction=='N')
        {
            k=1;
        }

    } while (!k);
    printf("\nThanks for using SBI ATM services");
    }
    else
    {
        printf("Please Insert a Valid card");
    }

}