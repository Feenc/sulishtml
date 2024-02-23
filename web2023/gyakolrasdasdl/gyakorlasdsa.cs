using System;

static int[] GenerateRandomNumbers()
{
    Random random = new Random();
    int[] eredmeny = new int[10000];

    for (int i = 0; i < result.Length; i++)
    {
        eredmeny[i] = random.Next(1000, 10000);
    }

    return eredmeny;
}
//Keszits egy fuggvenyt ami visszaad egy 10000 tagu 4jegyu pozitiv szamokat tartalmazo tombot. 
//Keressetek meg az olyan pontosan 3tagu szakaszokat amik egymastol maximum 10 tavolsagra vannak