class Program
{
    static void Main()
    {
        int szam;

        do
        {
            Console.Write("Kérem, adjon meg egy számot: ");
        } while (!int.TryParse(Console.ReadLine(), out szam) || szam % 9 != 0);

        Console.WriteLine($"{szam} osztható 9-tel.");

        if (szam % 5 == 0)
        {
            Console.WriteLine($"{szam} osztható 5-tel is.");
        }
        else
        {
            Console.WriteLine($"{szam} nem osztható 5-tel.");
        }
    }
}
