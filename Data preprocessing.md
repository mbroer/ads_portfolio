
<h2><b>4. Data preprocessing</b></h2>
<h3>4.1 Data exploration</h3>

<h4>4.1.1 FoodBoost csv merge</h4>

<b>Beschrijving</b><br>
Toen we voor het eerst begonnen met het FoodBoost project, stonden alle datasets los van elkaar, hierdoor was het dus lastig om een goed inzicht te krijgen in hoe alles nou in elkaar zat. Je had bijvoorbeeld het ingrediënten bestand waar elk ingrediënt van elk recept onder elkaar stond. Hierdoor kreeg je een bestand van 72000 rows. Hiervoor heb ik een python script gemaakt die alle informatie van het recept op 1 row zet en de data squished in lijsten. Hierdoor was het vooral voor de groep (die toen nog niet veel ervaring had met het joinen van tables etc) een stuk makkelijker om echt te kunnen beginnen met het FoodBoost project.
<br><br>
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
  [Notebook](https://github.com/mbroer/ads_portfolio/blob/main/notebooks/foodboost/join_all_csv.ipynb)<br><br>
  [CSV bestand](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/food_merge_all.csv)<br><br>
Screenshot resultaat:
  ![Screenshot Resultaat](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/merged.png)
  
  </details>
    
<h3>4.2 Data cleansing</h3>

<h4>4.2.1 FoodBoost simulated users</h4>

Ik ben begonnen met het opschonen van de bestaande dataframes, te zien in [ads_cleaner.py](https://github.com/mbroer/ads_portfolio/blob/main/apps/foodboost/simulated%20users/ads_cleaner.py).  Ik heb onnodige kolommen gedropt, zoals stars, url en image. Hierna heb ik dezelfde logica gebruikt als in het vorige hoofdstuk om deze dataframes op elkaar te joinen. Ook heb ik ervoor gezorgd dat kolommen die meerdere keren voorkwamen te droppen.<br>
Outliers heb ik handmatig verwijderd, dit waren bijvoorbeeld recepten waarvan ingrediënten niet klopte, denk hierbij aan een ingrediënt met de string: "ham en kaas" (2 ingredienten in 1 ingredient). Values met HTML heb ik vervangen door lege string values. Zelfde geldt voor speciale tekens zoals '(, ), {, }, [, ], +, & ' etc.

<h4>4.2.2 FoodBoost ingredieënten groeperen</h4>
Om zoveel mogelijk onnodige data te verwijderen om de beste resultaten te krijgen heb ik voor de ingredieënten het volgende gedaan:

* String manipulation:
    - Woorden zoals 'grote', 'middengrote', 'kleine' zijn eruitgehaald. 
    - Spaties eruitgehaald, rede is dat sommige packages 1 woord eruit haalde en die een 100% match gaven terwijl het woord ervoor of erna de context van het ingredieënt kompleet veranderde.
    - HTML verwijderd.
    - Leestekens verwijderd.
* Duplicate ingredients verwijderd.
* Dataset naar het Engels vertaald.
    - Omdat sommige ingrediënten foutief werden samen gevoegd, bijvoorbeeld 'spruitjes' en 'uitjes', was het mijn idee om de dataset naar het Engels te vertalen en de functie nog een keer eroverheen te laten lopen, alleen de woorden die dan in het engels en nederlands overeenkwamen zouden dan worden gegroepeerd.
 
<h3>4.3 Data preparation</h3>
Zoals in 4.2.1 vermeld, heb ik outliers van de dataframes handmatig verwijderd, onnodige kolommen gedropt, dupes te verwijderen etc.

<h4>4.3.1 FoodBoost simulated users</h4>

  <b>Beschrijving</b><br>
  Ons doel voor het FoodBoost project was om te kijken of een persoon een recept wel of niet lekker zou vinden, om hiervoor een model te maken hadden we dus bestaande informatie nodig om het model te kunnen trainen en testen, een oplossing die ik had bedacht was om een applicatie te schrijven die gebruikers op een semi realistische manier favoriete recepten kan genereren.
  
[Applicatie source code](https://github.com/mbroer/ads_portfolio/tree/main/apps/foodboost/simulated%20users)
  
Hierna heb ik utility functies geschreven om makkelijk informatie uit die dataframes te kunnen halen. Denk hierbij het omzetten van een dataframe row in een object, of een functie om alle informatie van een recept op te halen via een ID. Ook een zoek algoritme om makkelijk informatie op te kunnen halen
  
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
Output gegenereerde gebruiker<br>
![Gegenereerde user](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/user_gen.png)    
    Gesorteerd op favorite descending ~8000 rows
    
    
[Code voor een andere user-generation notebook](https://github.com/mbroer/ads_portfolio/blob/main/notebooks/foodboost/Simulated_Users.ipynb)
    
  </details>

<h4>4.3.2 FoodBoost CSV naar Json</h4>
  <b>Beschrijving</b><br>
  Voor het FoodBoost project moest ik voor mijn applicatie een csv bestand omzetten naar json, dit was gelukkig vrij simpel en kon met een file reader simpel mijn csv omzetten zodat ik een json bestand in kon laden en dan via het ID van het recept, de beschrijving van dat recept kon ophalen.
  
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
    %%%link naar notebook
    %%%img resultaat
    
  </details>
  
<h4>4.3.3 FoodBoost Ingredient Groeperen</h4>
  <b>Beschrijving</b><br>
  Tijdens het foodboost project kwamen we erachter dat het model veel moeite had om voorspellingen te maken, een gebruiker die veel recepten met tomaat lekker vond, zou een lage score geven aan een recept waar ook tomaat in zit, maar dan met een andere naam. Een voorbeeld hiervan is een user met favoriete recepten zoals: tomatensalade, tomatensoep, plakken tomaat en komkommer, en dan een voorspelling op bijvoorbeeld het gerecht gesneden tomaat. Hier gaf het model aan dat de gebruiker gesneden tomaat niet lekker zou vinden. Na discussie gingen wij ervan uit als projectgroep dat het model de correlatie tussen tomaten en tomaat niet kon vinden.

Een oplossing die we hadden verzonnen is om te proberen zoveel mogelijk ingredienten te groeperen in categorieën, dus tomaat, tomaten, tomaatje, tomatenstukes = categorië tomaat.

Ik heb hier geprobeerd een groepeer script voor te maken die automatisch ingredieënten groepeerd in categorieën.
  
 De Eerste poging was om simularity score te geven aan hoe erg een string op een andere lijkt. Hiervoor gebruiktte ik de package FuzzyWuzzy. Deze package kan kijken hoeveel een string op een andere string lijkt op basis van stopwords verkleinwoorden etc.
 <br>
 Mijn aanpak was om de lijst van ingredienten te sorteren van klein naar groot (aantal letters). Dat deed ik zodat ik maar 1x door de lijst moest loopen. De eerste groeping method was om te kijken of een woord in een ander wordt zit, dus in dit geval zou 'tomaat' de eerste key zijn, en de checkworden de andere 7000 ingredienten.
 zodra er een match plaats vindt wordt de andere key bijvoorbeeld 'tomaatstukjes' worden weggehaald. Ook haalde ik bij alle ingredienten de verkleinwoorden eruit zoals 'tje', 'en' etc.
 Hiermee kon ik over 7000 ingredienten loopen in een paar seconde, en halveerde ik de lijst van ingredienten in groepen. 
  
Ingredieënten gegroepeerd op bloem:
[Notebook](https://github.com/mbroer/ads_portfolio/blob/main/notebooks/foodboost/groups.ipynb)
  
Ik vond halvering wel oké, maar vond dat het nog beter kon.
Omdat de meeste systemen voor string manipulation alleen werken voor de engelse taal, was de eerste stap om de strings te vertalen naar het engels,
hiervoor heb ik een script gemaakt die via de google translate api de ingredieënten vertaald van het Nederlands naar het Engels:

<details>
<summary><i>Code, bestanden, resultaten</i></summary>
    
<h5>resultaat</h5>
    
De code voor dit script ben ik helaas verloren.
Het was niet al te veel code, ik laadde alle ingredienten van het CSV in, en stuurde deze naar de google translate api.
    
[Translated ingredients CSV](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/translated_ingredients.csv)
    
</details>
  
Met deze strings heb ik onderzoek gedaan naar hoe deze het beste zouden kunnen worden gecombineerd in groups. Hier heb ik gebruik gemaakt van kmeanas clusters. Met behuld van TfidfVectorizer kon ik de ingredienten omzetten naar tf-idf feature vectors, deze heb ik gefit, en getrained. met de predict kon ik voor elk ingredienten een label maken voor de behorende cluster. Met een object map heb ik daarna de ingredienten terug gezet naar de originele ingredienten.
Hier moest ik nog meer onderzoek naar doen om dit goed werkend te krijgen maar we gingen over naar een ander systeem. Dit is dus niet gebruikt voor ons project, maar hiermee heb ik wel meer kennis opgedaan van kmeans.
  
</details>

<h4>4.4 Data explanation</h4>

<h5>4.4.1 Foodboost</h5>

Een voorbeeld van gecreërde data van mijn user-generation programma:
![image](https://user-images.githubusercontent.com/83411588/214786219-620b4feb-91e1-4c71-ba89-e51fc1337c4c.png)

De dataset is van één gebruiker, met alle recepten als rijen. De door de gebruiker 10 gekozen favoriete recepten staan bovenaan, vandaar de perfecte scores van 1.
Voor dit voorbeeld heb ik een lage score gehanteerd van .3, je kan dus zien bij index 16, dat de tags en ingriedient scores best overeenkomen met wat er in de favoriete gerechten van de gebruiker zit, vandaar dat deze dan ook als favoriet wordt aangeduid. de mean score is de mean van tag en ingr score, deze moet hoger of gelijk zijn aan de input score om een favoriet recept te worden.

<h5>4.4.2 Containers</h5>

Een voorbeeld van de data die het PPO model genereerd voor het indelen van de containers:

![image](https://user-images.githubusercontent.com/83411588/214776663-104e37ca-ec91-47ac-b28d-e0a661c14d88.png)

De nummers 1, 2 en 3 tonen een container aan en bij welk schip deze hoort.
De 0 in deze matrix staat voor een lege plek.
De eerste array, [3,3,3,0,0] staat voor één stapel aan containers, dus 3 containers op elkaar, met 2 lege plekken erboven.
Deze stapel staat op de x=0, y=0 cooridinaten. De volgende array, [3, 3, 3, 3, 3] staat voor de volgende rij, dus x=0 en y=1.
In 2e matrix, 1e array, [1, 1, 1, 1, 1] staat voor de volgende kolom x=1.





<h4>4.5 Data visualization (exploratory)</h4>

<h4>4.5.1 Containers</h4>
In het voorbeeld van 4.4 wordt de matrix gevisualiseerd als:

![image](https://user-images.githubusercontent.com/83411588/214777781-dd012a4d-0945-416c-9219-4561b34b0f1c.png)


<h4>4.5.2 Foodboost app</h4>
Onze groep wilde voor het foodboost project iets visueels maken om uiteindelijk de ouput van het model te kunnen laten zien.
Hiervoor heb ik in mijn visuele applicatie een functie geschreven die via de index van een recept dat netjes in een lijst kan zetten.
Hij pakt de huidige dag, en vanaf daar zet het alle gerechten voor die week in een lijst<br>
  
![menu](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/overzicht.png)
    
<h4>4.5.4 Foodboost confusion matrix</h4>

Een visualisatie van de confusion matrix voor het voorspellen van favoriete recepten:<br>

[Notebook](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/usergen.ipynb)
 
    
<h4>4.5.5 Containers app</h4>
    <h4>Beschrijving</h4>
  Bij de start van het container project kwam onze groep er snel achter dat het zeer lastig was om een goed beeld te krijgen van wat er nou precies gebeurde, we hadden   een matrix van een grid van containers voorbeeld:<br>
    
[ 0,0,1,<br>
  1,2,1,<br>
  1,0,2 ]<br>
    
  Dit was één laag van containers, en ik zag al gelijk dat dit een probleem zou gaan worden met meerdere containers met meerdere stapels containers. Hierdoor kwam ik met het idee om een applicatie te bouwen om de containers in een grid te kunnen visualiseren in een 3d omgeving. Om dit zo makkelijk mogelijk te maken voor de rest van de projectgroep wilde ik deze applicatie maken in python, ik heb dus gekozen om met de vPython library te werken. vPython is een basic package waar je een 3d omgeving kan maken en een aantal shapes in kunt 'spawnen' op coordinaten. vPython is een verouderde package dus er zaten limitaties op wat ik kon doen. Een snel voorbeeld is dat het onmogelijk is om verschillende textures te gebruiken op één object, hierdoor kon ik niet een rechthoek maken met 5 verschillende container textures (top, bottom, sides, front, back). Hiervoor moest ik dus 6 wall objects maken elk met een eigen texture, deze objecten moesten daarna in de juiste coordinaten worden gezet om het weer een rechthoek te maken.
  
  De source code van de app is hier te vinden: [GitHub](https://github.com/mbroer/ads_portfolio/tree/main/apps/cofano)
  
<h3>Screenshot applicatie</h3>
   
![Screenshot app](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/app.png)
   
<h3>Applicatie features</h3>
	  
<h4>Visualiseren van output model</h4>
Waar onze projectgroep het meeste aan had, was het visualiseren van de output van ons model, in het begin was het simpel om dit handmatig te doen met een 3x3 en 3x3 grid, maar toen we gingen testen op grids van 5x8x5 werd dit onmogelijk. Ik heb toen een feature gemaakt die gemakkelijk een array kan omzetten naar een 3d visualisatie:<br>
	  
<img src="https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/Screenshot_20230125_105724_WhatsApp.jpg" width="250" height="500">
<br>resultaat:<br>
<img src="https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/IMG-20230124-WA0000.jpg" width="500" height="250">
	  
<h4>Scenario’s inladen en opslaan.</h4>
De applicatie kan een scenario inladen en opslaan via json
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/json.png)
    
<h4>Containers handmatig verplaatsen</h4>
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/v1.png)
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/v2.png)
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/v3.png)
    
<h4>visualisatie grid</h4>
Toont de bounds van plekken waar containers op de “juiste” plek staan, in dit geval dus een 3x3x3 grid
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/grid.png)
    
<h4>Grid x-y-z coordinaten</h4>
Toont de coordinaten van lege plekken in x,y,z formaat, hiermee kun je makkelijker een beeld krijgen van het huidige veld, bijvoorbeeld in plaats van “we willen de container van schip 2 die op rij 0 kolom 1 van de 3e array zetten op rij 2 kolom 1 in de 1e array”, kun je nu zeggen we willen de blauwe container naar plek 2,1,0 krijgen.
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/grid2.png)
    

<h4>Informatie inzien</h4>
Door oven een container te hover met je muis en dan op de ‘i’ toets te drukken krijg je een label overzicht met informatie van die container:
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/info1.png)
    
Hier krijg je te zien wat het id van de container is, van welk schip het is, de positie, de score, of deze container op een valide plek staat (in dit geval binnen het grid en of deze niet in de lucht zweeft), en of deze container kan worden verplaatst. In dit voorbeeld kan de geselecteerde container niet worden verplaatst, en de zwarte containers zijn de containers waardoor de container niet kan worden verplaatst, in dit geval dus de containers 1 laag naar beneden aan de lange zijde, en de container die boven op de geselecteerde container staat.
In dit voorbeeld kun je zien dat een zwevende container niet op een valide place staat:
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/info2.png)
    
Met de force validate knop kun je snel alle fout geplaatste containers tonen:
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/info3.png)
    
  Andere features waar de applicatie over beschikt zijn:
-	Het onzichtbaar maken van stapels containers om makkelijker inzicht te krijgen op de lager eronder.
-	Alle container labels aan en uit zetten
-	Container selecteren via dropdown (zodat je een container in het midden van een volle grid ook nog kan manipuleren)
-	Realtime scenario saving en loading zodat je niet elke keer de applicatie opnieuw hoeft op te starten, je hoeft alleen op reload scenario te drukken en alles wordt gerefreshed.
-	Force validation dropdown zodat je ook verstopte containers die op een foute plek staan kunt vinden.
-	Low detail mode voor als je honderden containers wilt inladen, wordt er alleen een basic box met een kleur ingeladen in plaats van 6 wall objects met texture en normal maps.
-	Keyboard controls voor viewpoint

  </details>
</details>
    
    

## [&#8592; Terug naar index](https://github.com/mbroer/ads_portfolio/blob/main/README.md)
