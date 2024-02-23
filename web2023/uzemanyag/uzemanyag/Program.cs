using uzemanyag;
List<adatok> valtozasok = new List<adatok>();
StreamReader olvas = new StreamReader("uzemanyag.txt");
while (!olvas.EndOfStream)
{
    valtozasok.Add(new adatok(olvas.ReadLine()));
}
olvas.Close();
Console.WriteLine("3.feladat: ");
Console.WriteLine("Valtozasok szama: {0}.",valtozasok.Count());
adatok minimum = valtozasok[0];
for (int i = 0; i < valtozasok.Count; i++)
{
    if (valtozasok[i].kulonbseg() < minimum.kulonbseg())
    {
        minimum = valtozasok[i];
    }
}
Console.WriteLine("4.feladat: a legkissebb kulonbseg: {0}.",minimum.kulonbseg());

int db =0;
for (int i = 0;i < valtozasok.Count; i++)
{
    if (minimum.kulonbseg() == valtozasok[i].kulonbseg())
    {
        db++;
    }
}
Console.WriteLine("5.feladat: a legkissebb kulonbseg elofordulasa: {0}.",db);

bool volt=false;
for (int i = 0; i < valtozasok.Count; i++)
{
    if (DateTime.IsLeapYear(valtozasok[i].datum.Year))
    {
        if (valtozasok[i].datum.Month == 2 && valtozasok[i].datum.Day == 24)
        {
            volt = true;
            break;
        }
    }
}
if (volt)
{
    Console.WriteLine("6.feladat: Volt valtozas szokonapon.");
}
else
{
    Console.WriteLine("6.feladat: Nem volt valtozas szokonapon.");
}