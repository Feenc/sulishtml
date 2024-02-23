using helsinki1952;
using System.ComponentModel.Design;
using System.Diagnostics;

List<adatok> eredmenyek =new List<adatok>();

StreamReader olvas = new StreamReader("helsinki.txt");
while (!olvas.EndOfStream)
{
    string sor = olvas.ReadLine();
    eredmenyek.Add(new adatok(sor));    
}
olvas.Close();
Console.WriteLine("3.feladat:");
Console.WriteLine("Pontszerzo helyezesek: {}",eredmenyek.Count());

Console.WriteLine("4.feladat");
int[] ermekszama =new int[7];
for (int i = 0; i < eredmenyek.Count; i++)
{
    ermekszama[eredmenyek[i].helyezes]++;
}
Console.WriteLine("Arany: {0}", ermekszama[1]);
Console.WriteLine("Ezüst: {0}", ermekszama[2]);
Console.WriteLine("Bronz: {0}", ermekszama[3]);



