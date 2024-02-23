//kerj be egy szot es ellenorizzetek h szo e es ezt karakterenkent alitsa elo visszafele es irasd ki
//ha kesz akkor kettesevel megforditani
//ha ezis kesz akkor kerjetek be egy szoveget es melyik betubol hany db van irasd ki 
/*
Console.Write("Kérem, adjon meg egy szót: ");
string szo = Console.ReadLine();

if (aszo(szo))
{
    Console.WriteLine($"A megadott '{szo}' egy érvényes szó.");
}
else
{
    Console.WriteLine($"A megadott '{szo}' nem egy érvényes szó.");
}
    

    static bool aszo(string szo)
{
    foreach (char karakter in szo)
    {
        if (!((karakter >= 'a' && karakter <= 'z') || (karakter >= 'A' && karakter <= 'Z')))
        {
            return false;
        }
    }
    return true;
}
*/
Console.Write("Krek egy szót: ");
string Be = Console.ReadLine();
bool joE = true;
string jok = "qwertzuiopőúöüóasdfghjkléáűíyxcvbnm-";
for (int i = 0; i < Be.Length; i++)
{
    if (jok.IndexOf(Be[i]) < 0)
    {
        Console.Write("Nem szó!");
        joE = false;
        break;
    }
}
if (joE)
{
    Console.WriteLine("{0}, jó szó!", Be);
}
string forditott = "";
for (int i = Be.Length-1; i >= 0; i--)
{
    forditott += Be[i];
}
Console.Write("A fordított szó: {0}", forditott);

forditott = "";
for (int i = 0; i < Be.Length; i++)
{
    forditott += Be[Be.Length -1 - i];
}
Console.WriteLine(forditott);

forditott = "";