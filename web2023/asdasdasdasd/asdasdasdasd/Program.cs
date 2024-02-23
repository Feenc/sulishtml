using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace asdasdasdasd
{
    class Program
    {
        static void Main(string[] args)
        {
            //kerj be 2 jegyu szamot addig csinald amig nem lesz 2 jegyu ird ki hogy ez 2 jegyu szam oszthato e kettovel es ezt 5-szor futtasd le 
            Console.Write("Kérek egy ketjegyu szamot: ");
            int szam = Convert.ToInt32(Console.ReadLine());
            while (szam.ToString().Length != 2)
            {
                return szam % 2 == 0;
            }

            }
        }
    }

