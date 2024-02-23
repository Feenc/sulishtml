int valasztas = Convert.ToInt32(Console.ReadLine());

switch (valasztas)
{
    /*case 1:
        Console.Write("Kérem, adjon meg egy számot: ");
        double szam = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("A megadott szám: " + szam);
        break;

    case 2:
        Console.Write("Kérem, adjon meg az első számot: ");
        double szam1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Kérem, adjon meg a második számot: ");
        double szam2 = Convert.ToDouble(Console.ReadLine());

        double kulonbseg = szam1 - szam2;
        Console.WriteLine("A két szám különbsége: " + kulonbseg);
        break;

    case 3:
        Console.Write("Kérem, adjon meg az első tizedestört számot: ");
        double tizedesSzam1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Kérem, adjon meg a második tizedestört számot: ");
        double tizedesSzam2 = Convert.ToDouble(Console.ReadLine());

        double szorzat = tizedesSzam1 * tizedesSzam2;
        Console.WriteLine("A két tizedestört szám szorzata: " + szorzat);
        break;

    case 4:
        Console.Write("Kérem, adjon meg az első számot: ");
        double elsoSzam = Convert.ToDouble(Console.ReadLine());

        Console.Write("Kérem, adjon meg a második számot: ");
        double masodikSzam = Convert.ToDouble(Console.ReadLine());

        double nagyobb = Math.Max(elsoSzam, masodikSzam);
        Console.WriteLine("A nagyobb szám: " + nagyobb);
        break;
    */


    case 5:
        Console.Write("Kérem, adjon meg az első számot: ");
        int a = Convert.ToInt32(Console.ReadLine());

        Console.Write("Kérem, adjon meg a második számot: ");
        int b = Convert.ToInt32(Console.ReadLine());

        if (b == 0)
        {
            Console.WriteLine("A második szám nem lehet 0!");
        }
        else
        {
            double tortErtek = (double)a / b;
            Console.WriteLine($"{a} / {b} = {tortErtek}");
        }
        break;

    default:
        Console.WriteLine("Érvénytelen választás!");
        break;
}
