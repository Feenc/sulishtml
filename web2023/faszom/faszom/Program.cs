using System.Security.Cryptography.X509Certificates;

Console.WriteLine("Hello, World!");
/*Kerj be 3 szamot es ird ki a legnagyobbat, kerj be egy szamot es
 * egy betut  es annyiszor irasd ki amennyi szamot bekertel, kerj be 2 szamot es a ket szam negyzeteinek az osszeget szamold
 * es irasd ki, ket szam kozti szamok negyzetenek osszege, nezz utanna hogyan kell negyzetgyokot vonni */
Console.WriteLine("Kérem, adjon meg három számot:");
Console.Write("Első szám: ");
int szam1 = int.Parse(Console.ReadLine());

Console.Write("Második szám: ");
int szam2 = int.Parse(Console.ReadLine());

Console.Write("Harmadik szám: ");
int szam3 = int.Parse(Console.ReadLine());       
int legnagyobb = Math.Max(szam1, Math.Max(szam2, szam3));
Console.WriteLine("A legnagyobb szám: " + legnagyobb);

//2.feladat
Console.Write("Kérem, adjon meg egy számot: ");
int szam = int.Parse(Console.ReadLine());

Console.Write("Kérem, adjon meg egy betűt: ");
char betu = char.Parse(Console.ReadLine());

for (int i = 0; i < szam; i++)
{
    Console.Write(betu);
}



