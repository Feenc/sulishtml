#3jegyu szam bekeres
szam="12"
while len(szam) !=3:
    szam=input("Kérek egy 3 jegyü számot: ")

szam=int(szam)
if szam%12==0:
    print("oszthato")
print(szam)
#hf: kerjetek be egy aszamot es irjatok ki prim tenyezos szorzatta



szoveg="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus volutpat, turpis eget hendrerit consequat, magna magna fringilla nisl, eget condimentum metus mauris vitae nunc. Praesent porta luctus nulla sed bibendum. Maecenas nec ornare turpis. Mauris sit amet suscipit dui, quis congue erat. Pellentesque auctor nisl tortor. Aenean bibendum velit lectus, eget mollis lacus ullamcorper sit amet. Sed libero massa, molestie sit amet accumsan at, malesuada non lorem. Sed non porta ex. Mauris congue, mauris id finibus euismod, diam nisl accumsan ante, at fringilla massa felis id leo. Phasellus pretium ante in libero euismod, sit amet varius neque tincidunt. Vivamus pulvinar malesuada ex, id euismod lorem auctor sit amet. Duis iaculis molestie neque, sed faucibus nisi consequat tristique. Vestibulum justo ligula, efficitur fringilla sodales vulputate, interdum in diam."

betu="i"
print(len(szoveg.split(" ")))
szoveg2=szoveg.replace("i","I")
print(szoveg2)
