using fogado;
List<adatok> foglalasok = new List<adatok>();
StreamReader olvas = new StreamReader("fogado.txt");
while (!olvas.EndOfStream)
{
    string sor = olvas.ReadLine();
    foglalasok.Add(new adatok(sor));
}
olvas.Close();
Console.WriteLine("2.feladat");
Console.WriteLine("A foglalasok szama: {0}.",foglalasok.Count());

Console.WriteLine("3.feladat");
Console.Write("Adjon meg egy nevet: ");
string nev=Console.ReadLine();

int darab =0;
for (int i = 0; i < foglalasok.Count(); i++)
{
    if (foglalasok[i].nev== nev)
    {
        darab++;
    }
}
if (darab > 0)
{
    Console.WriteLine("{0} néven {1} idopontfoglalas van.", nev, darab);
}
else
{
    Console.WriteLine("A megadott néven nincs idopont foglalas.");
}

Console.WriteLine("4.feladat");
Console.Write("Adjon meg egy érvényes időpontot(pl. 17:10):");
string idopont=Console.ReadLine();
List<string>nevek = new List<string>();
for (int i = 0; i < foglalasok.Count; i++)
{
    if (idopont == foglalasok[i].idopont)
    {
        nevek.Add(foglalasok[i].nev);
    }
}

nevek.Sort();
for (int i = 0;i<nevek.Count ; i++)
{
    Console.WriteLine(nevek[i]);
}
File.WriteAllLines(idopont.Replace(":", "") + ".txt", nevek);