<h2><b>2. Predictive Analytics</b></h2>

<h3>2.1 Selecting a Model</h3>
In dit hoofdstuk beschrijf ik een aantal modellen die gedurende de minor zijn gebruikt.
	
<h4>2.1.1 Foodboost</h4>
Voor het Foodboost project hebben we gebruik gemaakt van de volgende modellen:
* MatrixFactorization, voor het recommender systeem.
	Hiervoor is gekozen omdat het vaak gebruikt wordt voor het maken van recommender systemen. Dit komt omdat het effectief grote en schaarse data kan verwerken. Door de users en recepten in het product te decompenseren als user-item, kan de matrix de onderliggende patronen en relaties vastleggen. Dit kan leiden tot betere generalisatie en betere voorspellingen, zelfs als deze geen interactiegeschiedenis hebben.<br>
Over het algemeen is MatrixFactorization een krachtige techniek die een recommendersysteem en aanbevelingen van hoge kwaliteit kan produceren.
	
* SVM, om te proberen om de ingrediënten en tags te groeperen via categorie.
* Logistic regression, ook om te proberen om ingrediënten en tags te groeperen

	
	<h4>2.1.2 Cofano</h4>
	* Reinforcement learning model
	
<h3>2.2 Configuring a Model</h3>
    

<h3>2.3 Training a Model</h3>

<h3>2.4 Evaluating a Model</h3>
	
<h4>2.4.1 FoodBoost</h4>
Voor het foodboost project zijn de volgende evaluatie technieken toegepast:
	
	* Leave One Out
	* K-Nearestneighbor clustering
	
	%%%cofano, hoe ik met mijn visualisatie app het model evalueer.
	
<h3>2.5 Visualizing the outcome of a model (explanatory)</h3>
	
<h4>Foodboost app</h4>
	%%%
  Onze groep wilde voor het foodboost project iets visueels maken voor
  
<h4>Containers app</h4>
  
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
