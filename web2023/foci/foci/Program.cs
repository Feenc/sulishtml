using foci;

List<adatok> merkozesek = new List<adatok>();
StreamReader olvas = new StreamReader("meccs.txt");
olvas.ReadLine();
while (!olvas.EndOfStream)
{
    string sor = olvas.ReadLine();
    merkozesek.Add(new adatok(sor));
}
olvas.Close();
//Console.Write("Fordulo szama: ");
//Console.ReadLine();
Console.WriteLine("{0}-{1}: {2}-{3} ", merkozesek[5].hazaiCsapat, merkozesek[6].vendegCsapat, merkozesek[1].hazaiGol, merkozesek[2].vendegGol);

           
