//kerj be szavakat amik szavak legyen tehat nelegyen benne specialis karakter es ezeket szavankent irjuk bele egy fileba
string betuk = "qwertzuiopőúöüóasdfghjkléáűíyxcvbnm-";
string beSzo = "mindegymi";
string gyujto = "";
while (beSzo!="")
{
    bool joSzo = true;
    Console.Write("Kérek egy szot: ");
    beSzo = Console.ReadLine();
    for (int i = 0; i < beSzo.Length; i++)
    {
        if (betuk.IndexOf(beSzo[i]) == -1)
        {
            joSzo = false;
            Console.WriteLine("Nem jo szo");
            break;
        }

    }
    if (joSzo)
    {
        gyujto += beSzo+" ";
    }
}
Console.WriteLine( gyujto );
string[] darabok=gyujto.Trim().Split(' ');
StreamWriter ir= new StreamWriter("szavak.txt");
for (int i = 0;i < darabok.Length; i++)
{
    Console.WriteLine(darabok[i]);
}
ir.Close();