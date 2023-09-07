using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace elso
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("halogeci");
            int szam = 6;
            Console.WriteLine(szam);
            int szam2 = -2;
            Console.WriteLine(szam2);
            double szam3 = 3.98;
            Console.WriteLine(szam3);
            char betu = 'c';
            Console.WriteLine(betu);
            Console.WriteLine((char)betu + 2);
            Console.WriteLine(10 / 3);
            int a;
            a = 4;
            if (a > 2)
            {
                Console.WriteLine("Nagyobb");
            }
            else if(a<2)
            {
                Console.WriteLine("Kisebb");
            }
            else if (a % 2 == 0)
            {
                Console.WriteLine("Paros");
            }
            else
            {
                Console.WriteLine("Egyenlo");
            }

            switch (a)
            {
                case 1:
                    Console.WriteLine("egy");
                    break;
                case 2:
                    Console.WriteLine("ketto");
                    break;
                case 3:
                    Console.WriteLine("harom");
                    break;
                case 4:
                    Console.WriteLine("negy");
                    break;
                default:
                    Console.WriteLine("valami mas");
                    break;
            }
        }
    }
}
