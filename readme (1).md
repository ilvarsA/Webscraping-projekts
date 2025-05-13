# Auto izdevīguma meklētājs

## Projekta uzdevums

Lai automātiski apmeklētu visus ss.lv transporta sadaļas sludinājumus paņemot 5 izdevīgākās automašīnas, katrā kategorijā (no katras markas) salīdzinot tās ražošanas gadu un cenu (gads / cena). Mērķis ir atrast vislabāko vērtību attiecībā pret to vecumu un cenu.

## Webscraping

Sākuma lapā tiek attēlotas dažādas automašīnu kategorijas, piemēram, pēc markas (BMW, Audi, Toyota u.c.). Lapa tiek ielādēta ar requests.get(), un tās HTML struktūra tiek pārveidota analizējamā formātā ar BeautifulSoup.

## Pārlūko katru automašīnu kategoriju (līdz 42 kategorijām).

Pēc sākotnējās lapas ielādes tiek meklēti HTML elementi ar klasi a_category, kas satur saites uz dažādām automašīnu kategorijām (markām). Tiek iegūtas saites (href) uz šīm kategorijām, un programma pēc tam apmeklē katru no šīm kategorijām, līdz 42, jo mājaslapā ir nevajadzīgas kategorijas, kuras nav sadalītas pēc markām.
Katrā kategorijā ir lapa, kura satur sludinājumu sarakstu no kurienes programma ņem datus.

## Apstrādā katru sludinājumu, iegūstot automašīnas cenu un ražošanas gadu.

Katras kategorijas lapā tiek meklēti elementi ar klasi <ins>msg2</ins>, kas pārstāv atsevišķus sludinājumus. No katra sludinājuma tiek izgūta saite uz attiecīgo sludinājuma lapu. Ar atsevišķu requests.get() tiek ielādēta šī lapa. No lapas tiek paņemta - cena: elements ar klasi ads_price. Ražošanas gads: elements ar ID tdo_18 konkrēts ss.lv lapas struktūrā. Abas vērtības tiek apstrādātas ar re.sub(), lai paņemtu tikai ciparus. Rezultātā tiek iegūti int tipa dati — price un year.

## Aprēķina "score" (gads / cena) katram auto.

Aprēķina vērtību katrai automašīnai ar formulu: score = year / price. Jo lielāks rezultāts, jo labāk, izdevīgāk un ja mazāks tad tieši pretēji, neizdevīgs.

## Izvada top 5 izdevīgākos automobiļus katrā kategorijā.

Pēc visu datu apstrādes un saglabāšanas, programma:
Izmanto sorted() funkciju, lai sakārtotu visus auto pēc score vērtības dilstošā secībā.
Atlasīti tiek pirmie pieci ieraksti ([:5]).
Izvadīts:
Sludinājuma URL;
Gads;
Cena;
Aprēķinātais score ar 5 zīmīgajiem cipariem aiz komata.


## Izmantotās Bibliotēkas

 **requests**  
  Tiek izmantota HTTP pieprasījumu veikšanai, lai iegūtu mājaslapas HTML saturu. 
**BeautifulSoup (no bs4)**  
  Šī bibliotēka ļauj viegli analizēt HTML struktūru. Tā tiek izmantota, lai python "saprastu" un analizētu mājaslapas saturu.
 **urllib.parse (urljoin)**  
  Apvienot saites ar bāzes URL, veidojot pilnas saites uz detalizētajām lapām.
 **re**  
  Lietota, lai attīrītu skaitliskos datus no teksta.


## Pašu definētas datu struktūras

```
results[detail_url] = {
    "price": price,
    "year": year,
    "score": score
}
```
