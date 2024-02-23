namespace oop3
{
    internal class ember
    {
        public string keresztNev;
        public string vezetekNev;
        public string teljesNev
        {
            get { return vezetekNev + "" + keresztNev; }
        }
        public ember(string vNev)
     