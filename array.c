#include<stdio.h>
void main()
{
   int a[5] = {5, 1, 15, 20, 25};
   int i, j, m;
   i = ++a[1];
   printf("%d %d\n",i, a[1]);
   j = a[1]++;
   printf("%d %d\n", i, a[1]);
   m = a[++i];
   printf("%d %d %d", i, j, m);
   printf("\n");
   for (int k = 0; k < 5; k++)
   {
      /* code */
      printf("%d ", a[k]);
   }
   
}