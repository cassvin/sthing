#include <stdio.h>

/*  大端编码，高位数据存放于低位地址，
 *  低位数据存放与高位地址，
 *  使得数据在内存中是顺序排放。
 */

int endian()
{
  union {
    unsigned int a;
    unsigned char b;
  } c;
  c.a = 1;
  return (c.b == 1);
}

int main(void)
{
  if (endian())
    printf("Little endian!\n");
  else
    printf("Big endian!\n");
  return 0;
}
