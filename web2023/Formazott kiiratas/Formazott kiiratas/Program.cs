// See https://aka.ms/new-console-template for more information
/*Console.WriteLine("szoveg {0:0.00%} szoveg {1,10}---", 12, 3.4);
int a = 12;
double b = 3.4;
Console.WriteLine($"a szoveg {a} szoveg {b}");
Console.WriteLine("{0,10}", 1);
Console.WriteLine("{0,10}", 10);
Console.WriteLine("{0,10}", 100);
Console.WriteLine("{0,10}", 1000);

int a = 3;
int b = 4;
double c=Math.Sqrt(a*a + b*b);

Console.WriteLine(c);
for (int i = 1; i < 20; i++)
{
    for (int k = 0; k < 20; k++)
    {
        c=Math.Sqrt(a*a + b*k);
        if (c % 0 == 0)
        {
            Console.WriteLine("{0} {1}{2}",i,k,c);
        }
*/
for (int m = 1; m <= 10; m++)
{
double negyzetgyok = Math.Sqrt(m);
Console.WriteLine($"Az {m}. egész szám négyzetgyöke: {negyzetgyok:F2}");
}