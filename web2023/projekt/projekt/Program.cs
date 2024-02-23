using System;
string[] hosszusag = {"mm","cm","dm","m","km" };
int[] hosszusagValto = { 10, 10,10, 1000, 1 };
string[] terulet = { "mm2", "cm2", "dm2", "m2", "km2" };
int[] teruletValto = { 100, 100, 100, 1000000, 1 };
string[] tomeg = { "ml", "g", "dkg", "kg", "q", "t" };
int[] tomegValto = { 1000,10,100,1000, 1 };

bool jo = false;

string forrasMertekegyseg = "";
double szam = 0;

string[] egyseg = { };
int[] valto= { };

while (!jo)
{
    jo = true;
    Console.Write("Mit valtsak at? (pl.: 12,4 cm): ");
    string be = Console.ReadLine();

    string[] darab = be.Split(' ');
    if(darab.Length != 2)
    {
        jo = false;
        continue;    
    }
   
    try
    {
        szam = Convert.ToDouble(darab[0]);
    }
    catch (Exception)
    {
        Console.WriteLine("Nem jo formatum! Legyen ilyen: (pl.: 12.2 kg)");
        jo = false;
        continue;

    }
    Console.WriteLine(szam);

    if (hosszusag.Contains(darab[1]))
    {
        forrasMertekegyseg = darab[1];
        egyseg = hosszusag;
        valto = hosszusagValto;
    }
    else if (terulet.Contains(darab[1]))
    {
        forrasMertekegyseg = darab[1];
        egyseg = terulet;
        valto = teruletValto;
    }
    else if (tomeg.Contains(darab[1]))
    {
        forrasMertekegyseg = darab[1];
        egyseg = tomeg;
        valto = tomegValto;
    }
    else
    {
        Console.WriteLine("Nem jo mertekegyseg!");
        jo = false;
        continue;
    }
}
Console.WriteLine("Mire szeretned atvaltani?");
for (int i = 0; i < egyseg.Length; i++)
{
    Console.WriteLine(egyseg[i]);

}

string valasz = "";
while(!egyseg.Contains(valasz))
{
    Console.Write("Valassz: ");
    valasz = Console.ReadLine();
}
int index1 = Array.IndexOf(egyseg,forrasMertekegyseg);
int index2 = Array.IndexOf(egyseg, valasz);

int szorzo = 1;

double eredmeny = 0;
if (index1 < index2)
{
    for (int i = index1; i < index2; i++)
    {
        szorzo = szorzo * valto[i];
    }
    Console.WriteLine(szorzo);
    eredmeny = szam / szorzo;
}
else
{
    for (int i = index2; i < index1; i++)
    {
        szorzo = szorzo * valto[i];
    }
    Console.WriteLine(szorzo);
    eredmeny= szam * szorzo;
}
Console.WriteLine("{0} {1}={2} {3} ", szam,forrasMertekegyseg,eredmeny,valasz);



