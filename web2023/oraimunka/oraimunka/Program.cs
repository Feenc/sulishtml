using System;

class Program
{
    static void Main()
    {        
        int[,] szorzotabla = new int[5, 5];

        for (int sor = 0; sor < 5; sor++)
        {
            for (int oszlop = 0; oszlop < 5; oszlop++)
            {
                szorzotabla[sor, oszlop] = (sor + 1) * (oszlop + 1);
            }
        }        
        Console.Write("Kerem adjon meg egy szamot: ");
        int szam = Convert.ToInt32(Console.ReadLine());       
        Console.WriteLine($"A szorzotabla a {szam} szammal:");
        for (int sor = 0; sor < 5; sor++)
        {
            for (int oszlop = 0; oszlop < 5; oszlop++)
            {
                int eredmeny = szam * szorzotabla[sor, oszlop];
                Console.Write($"{eredmeny}\t");
            }
            Console.WriteLine();
        }
        Console.ReadLine();
    }
}
