using System.Security.Cryptography;

int[] tombkeszit(int darab,int legkisebb,int legnagyobb)
{
    int[] tomb=new int[darab];
    Random rand=new Random();
    for (int i = 0; i < tomb.Length; i++)
    {
        tomb[i]=rand.Next(legkisebb,legnagyobb+1);
    }
    return tomb;        
}
int[] szamok = tombkeszit(1000, 100, 999);

int parosDb = 0;
for(int i=0; i < szamok.Length; i++)
{
    if (szamok[i] % 2 == 0)
    {
        parosDb++;
    }
}
Console.WriteLine("A szamok kozott {0} paros es {1} paratlan van.",parosDb,szamok.Length,parosDb);
bool vanEgyenloSzomszedos=false;
for( int i=0;i < szamok.Length ; i++)
{
    if (szamok[i] == szamok[i - 1])
    {
        vanEgyenloSzomszedos = true;
        //break;
        Console.WriteLine("Egyenlo: {0}. és {1} {2} = {3}", i - 1, i, szamok[i-1],szamok[i]);
    }
}
if (vanEgyenloSzomszedos)
{
    Console.WriteLine("Van egyenlo szomszedos elem");
}
else
{
    Console.WriteLine("Nincs egyenlo szomszedos elem");
}
void szakasz2(int[] szamTomb)
{
    int kezd = 0;
    int veg = 0;
    int maxKezd = 0;
    int maxVeg = 0;

    for (int i = 1; i < szamTomb.Length; i++)
    {
        if (szamok[i - 1] < szamok[i])
        {

        }
        else
        {
            veg = i - 1;
            if (veg - kezd + 1 > maxVeg - maxKezd + 1)
            {
                maxKezd = veg;
                maxVeg = veg;
            }
            kezd= i;
        }
    }
    Console.Write("A legnagyobb novekvo szamsorozat {0} elemu. ", maxVeg-maxKezd+1);
    for(int i = maxKezd; i <= maxVeg+1; i++)
    {
        Console.Write("{0}", szamTomb[i]);
    }
    Console.WriteLine();
}
szakasz2(szamok);
