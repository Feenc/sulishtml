using System;

Console.Write("Kérek egy szamot: ");
double szam=Convert.ToDouble(Console.ReadLine());
while (szam % 1.2 >= 0.01)
{
    Console.Write("Kérek egy szamot: ");
    szam=Convert.ToDouble(Console.ReadLine()); 
}
int szam2 = (int)szam;
Console.WriteLine(szam2);