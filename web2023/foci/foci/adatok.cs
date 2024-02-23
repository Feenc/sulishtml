using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace foci
{
    internal class adatok
    {
        public int fordulo;
        public int hazaiGol;
        public int vendegGol;
        public int hazaiFelido;
        public int vendegFelido;
        public string hazaiCsapat;
        public string vendegCsapat;

        public adatok(string sor)
        {
            string[] vag = sor.Split(" ");                      
            fordulo = int.Parse(vag[0]);            
            hazaiGol = int.Parse(vag[1]);
            vendegGol = int.Parse(vag[2]);
            hazaiFelido = int.Parse(vag[3]);
            vendegFelido = int.Parse(vag[4]);
            hazaiCsapat = vag[5];
            vendegCsapat = vag[6];

        }

    }
}
