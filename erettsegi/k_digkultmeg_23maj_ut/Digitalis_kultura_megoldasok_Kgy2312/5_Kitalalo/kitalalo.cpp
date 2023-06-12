#include <iostream>
#include <ctime>
using namespace std;

int main(){
    setlocale(LC_ALL,"");
    srand(time(NULL));
    int db, tsz=0;
    string szavak[15]={"fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"};
    string szo=szavak[rand()%15];
    string tipp, eredmeny;
    while (db<6 && tipp!="stop"){
        cout<<"Kérem a tippet: "; cin>>tipp;
        db=0; eredmeny="";
        for(int i=0;i<6;i++)
            if (szo[i]==tipp[i]){
                    eredmeny+=tipp[i];
                    db++;
                }
                else eredmeny+='.';
        if (tipp!="stop")cout<<"Az eredmény: "<<eredmeny<<endl<<endl;
        tsz++;
    }
    if (db==6) cout<<tsz<<" tippeléssel sikerült kitalálni."<<endl;
    return 0;
}
