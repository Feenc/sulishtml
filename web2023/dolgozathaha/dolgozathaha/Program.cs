StreamReader beolvas = new StreamReader("adathalmaz.csv");
string sor = beolvas.ReadLine();
if (sor != null)
{
    string[] vag = sor.Split(",");
    List<int> sorszam = new List<int>();
    sorszam.Add(Convert.ToInt32(vag[0]));
    Console.WriteLine(sorszam.Count);
}