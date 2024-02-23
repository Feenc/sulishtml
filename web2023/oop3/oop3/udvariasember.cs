using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oop3
{
    internal class udvariasember:ember
    {
        public udvariasember(string vNev,string kNev):base(vNev,kNev)
        {

        }
        public void koszon()
        {
            Console.WriteLine("Szia uram!");
        }
        public void koszonNevvel()
        {
            Console.WriteLine("Szia uram!{0} vagyok!",teljesNev);
        }
    }

}
