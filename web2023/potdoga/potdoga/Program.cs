using System;
using System.IO;

class Program
{
    static void Main()
    {
        string[] sorok = File.ReadAllLines("jarmu.txt");

        Console.WriteLine("Fájl tartalma:");
        foreach (var sor in sorok)
        {
            Console.WriteLine(sor);
        }

    }
}   
