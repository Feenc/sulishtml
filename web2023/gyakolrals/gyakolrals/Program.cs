/*int szam;
 bool ervenyesSzam = false;

 do
 {
     Console.Write("Kérem, adja meg a számot: ");
     string input = Console.ReadLine();
     if (int.TryParse(input, out szam))
     {
         ervenyesSzam = true;
     }
     else
     {
         Console.WriteLine("Érvénytelen bemenet. Kérem, adjon meg egy érvényes számot.");
     }
 } while (!ervenyesSzam);

 string[] szovegek = new string[szam];


 for (int i = 0; i < szam; i++)
 {
     Console.Write($"Kérem, adja meg a {i + 1}. szöveget: ");
     szovegek[i] = Console.ReadLine();
 }

 string leghosszabbSzo = LeghosszabbSzo(szovegek);

 Console.WriteLine($"A leghosszabb szó: {leghosszabbSzo}");
}

static string LeghosszabbSzo(string[] szovegek)
{
 string leghosszabbSzo = "";

 foreach (string szo in szovegek)
 {
     if (szo.Length > leghosszabbSzo.Length)
     {
         leghosszabbSzo = szo;
     }
 }

 return leghosszabbSzo;
}
}

if(szavak[i]) az aktualis elem indexe az az i


string[] szavak = new string[] { "alma", "körte", "ananász", "narancs", "banán", "narancs" };
string[] rovid = new string[szavak.Length];
string[] hosszu = new string[szavak.Length];
int rovidIndex = 0;
int hosszuIndex = 0;
for (int i = 0; i < szavak.Length; i++)
{
if (szavak[i].Length <= 5)
{
 rovid[rovidIndex] = szavak[i];
 rovidIndex++;
}
else
{
 hosszu[hosszuIndex] = szavak[i];
 hosszuIndex++;
}

}
foreach (string i in rovid)
{
Console.WriteLine(i);
}
foreach(string i in hosszu)
{
Console.WriteLine(i);
}
//HF:Ne legyen hezag
*/
int[] szamok=new int[1000];
Random rnd = new Random();
for (int i = 0; i < szamok.Length; i++)
{
    szamok[i] = rnd.Next(100,999);
}
foreach (int i in szamok)
{
    Console.WriteLine(i);
}   