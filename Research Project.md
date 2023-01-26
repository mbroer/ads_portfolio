<h2><b>1. Research project</b></h2>

<h3>1.1 Task definition</h3>
    
<h4>1.1.1 Foodboost</h4>
Tijdens het Foodboost project heeft onze projectgroep zich bezig gehouden met het voorspellen of een eindgebruiker een gerecht wel of niet lekker zou vinden, met als einddoel om een applicatie te maken die een gebruiker kon helpen een weekmenu samen te stellen voor zijn noddigheden, bijvoorbeeld een dieetdoel. Het is namelijk zeer lastig voor iemand om zelf een gevarieerd weekmenu samen te stellen, dit komt omdat de meeste mensen maar 6/7 favoriete gerechten hebben die ze willen eten. Dit wilde onze groep oplossen met een applicatie. 
<br>
In deze applicatie zouden restricties zitten zoals allergiën, of het een hoofdgerecht/ dessert is (thema zoals sinterklaas/ halloween), of voorkeuren zoals geen zout. De hoofdvraag gedurende het project was: <b>Hoe kunnen we een app maken waarmee gebruikers een persoonlijk advies krijgen wat ze deze week gaan eten, zodat ze makkelijker tot een betere keuze kunnen komen.</b><br>
	
De deelvragen voor het foodboost project waren:
1. Hoe moeten we een app maken om gebruikers hun favoriete recepten te laten selecteren?
2. Welke methodes kunnen we gebruiken om te voorspellen of de eindgebruiker een recept wel of niet lekker gaat vinden?
3. Kunnen we ingredienten groeperen voor betere voorspellingen?
    
Mijn persoonlijke einddoel was om uiteindelijk de applicatie te bouwen, met het model draaiend op de achtergrond.
Deze applicatie is gerealiseerd, zonder communicatie met het uiteindelijke model, omdat hier geen tijd meer voor was.
Deze applicatie heb ik zelfstandig gemaakt.

De sourcecode van de applicatie is hier terug te vinden:
[GitHub](https://github.com/mbroer/ads_portfolio/tree/main/apps/foodboost/quiz) <br>
[Demo app: (.mp4 download)](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/Untitled.mp4)
            
<h4>1.1.2 Containers</h4>
Tijdens het Container project heeft onze projectgroep zich bezig gehouden met onderzoeken en ontwikkelen van een schaalbare methode om een optimale indeling van containers op een grid te genereren. Het schaalbare gedeelte is nodig omdat het model ook moet werken bij grotere kades of in een situatie wanneer er met meer container wordt gewerkt dan verwacht. De hoofdvraag gedurende dit project was: <b>Hoe kunnen we met een lijst van containers, een model trainen om die in de beste opstelling neer te zetten op de kade, zodat de stackers, met zo min mogelijk verplaatsingen, de containers naar de schepen kunnen verplaatsen.</b>
    
De deelvragen voor het containers project waren:
1. Welke methode is hiervoor het beste?
2. Kunnen we dit schaalbaar maken?
3. Hoe kunnen we de opstelling van het model evalueren?
4. Hoe gaan we de uitkomst visualiseren?

<h3>1.2 Evaluation</h3>
    
<h4>1.2.1 Foodboost app</h4>
Mijn persoonlijke eindproduct voor dit product, namelijk de quiz applicatie, kan verbeterd worden in de toekomst door het uiteindelijke model te implementeren in de applicatie. Op dit moment geeft de applicatie een pseudo-random lijst terug, gebaseerd op het thema van de gerechten die je hebt geselecteerd. De reden hiervoor is dat het model niet optijd af was om dit te implementeren in de applcatie voor de externe presentatie. Om dit te realiseren zou het model aangepast moeten worden zodat het een x aantal recepten kan accepteren en op basis daarvan de index terugstuurd naar de applicatie, zodat deze die kan tonen.
	
Een algemene aanbeveling zou kijken hoe we de restricities in het model kunnen verwerken, zoals allergieën, of voorkeuren.	
	
<h4>1.2.2 Foodboost user-gen</h4>
De foodboost user-gen applicatie kan worden verbeterd door een GUI in de applicatie te bouwen. Nu is het nog een command line applicatie. Ook kan het groepeer gedeelte voor de ingredieënten verbeterd worden door te onderzoeken of FuzzyWuzzy hier wel de beste oplossing voor is, en of de simularity score wel optimaal is.
    
<h4>1.2.3 Containers app</h4>
De visuele container applicatie kan op meerdere manieren worden verbeterd.
1) Automatisch inladen van output van het model.
Als we nu output van het model visueel willen zien, moeten we de output van het model, bijvoorbeeld:<br>

		array([[[3,3,3],
			[3,3,0],
			[3,0,0]],

			[[1,1,1],
			[1,0,0],
			[1,1,0]],

			[[2,2,2],
			[2,2,2],
			[0,0,0]]]
		)

kopieëren en plakken in een inputbox van de applicatie.
    Als het model en de applicatie gekoppeld zouden worden zou dit automatisch ingeladen kunnen worden zodat dat tijd zou besparen.
2) Tijdlijn voor elke stap die het model zet.
De applicatie zou een stuk geadvanceerder zijn als je bij elke stap van het model de output zou kunnen zien om te evalueren of het model goed werkt. Hiervoor zou je nu voor elke stap een nieuwe scenario moeten maken.
Ik zou dit zelf doen door containers te verplaatsen, hiervoor is al een moves field aangemaakt in de scenario json's

<h3>1.3 Conclusions</h3>
	
<h4>1.3.1 Foodboost</h4>
De conclusies voor het foodboost project waren:
	
<b>1. Hoe moeten we een app maken om gebruikers hun favoriete recepten te laten selecteren?</b><br>
Gedaan via een quiz-applicatie. Je krijgt steeds 4 recepten op je scherm, daarvan klik je er één aan, en na x keer selecteren krijg je je weekmenu te zien. Deze applicatie is gemaakt in VUE, hiervoor is gekozen omdat ik al ervaring had met dat framework, en vanwege de realtime page updates die het ondersteund.
	
<b>2. Welke methodes kunnen we gebruiken om te voorspellen of de eindgebruiker een recept wel of niet lekker gaat vinden?</b><br>
Er is een model gemaakt dat op basis van een paar keukens (bijvoorbeeld italiaans, hollands) recepten kan aanraaden aan een user die deze lekker zal vinden. Dit model was voor 99% accuraat.

<b>3. Kunnen we ingredienten groeperen voor betere voorspellingen?</b><br>
Met behulp van string matching algoritmes en logistic regression konde we meer dan de helft van de ingredieënten groeperen, of dit nut heeft gehad op het model is niet te zeggen, want hier is niet verder aan gewerkt.
    

<h4>1.3.2 Containers</h4>
De conclusies voor het container project waren:

<b>1. Welke methode is hiervoor het beste?</b><br>
Wij hebben uiteindelijk een PPO model gebruikt om de indelingen te genereren, zoals ik in een ander hoofdstuk vertel, was PPO een stuk sneller dan het A2C model (te zien aan de fps van de iteraties), en gaf het ook betere resultaten.<br>
<b>Het PPO model kon in 350k timesteps en 334 seconde de optimale opstelling van een 3x3x3 grid genereren</b>

![image](https://user-images.githubusercontent.com/83411588/214798355-47ef6c6b-e143-41fb-8c2a-d14ef923c497.png)
<br>De loss van het model:<br>
![image](https://user-images.githubusercontent.com/83411588/214798423-24be5320-3dbb-4c69-a187-3ad0e8fac3e2.png)


<b>2. Kunnen we dit schaalbaar maken?</b><br>
Het is gelukt om de grid van 2x2 naar 3x3 naar 3x3x3 te krijgen. Verder is er getest met een 5x5x8 grid, dat ook functioneel was. Dus het antwoord hierop is ja, echter is het maken van een groter grid wel een stuk langzamer.

<b>3. Hoe kunnen we de opstelling van het model evalueren?</b><br>
Dit is gedaan met reward/penalties. Op het einde deden we een handmatige evaluatie om te kijken of containers niet op de verkeerde plekken stonden, dus of er geen containers in elkaar stonden, deze niet zweefde etc. 

<b>4. Hoe gaan we de uitkomst visualiseren?</b><br>
Mijn persoonlijke eindproduct was het realiseren van een applicatie die visueel het resultaat van het model kon laten zien.
Deze applicatie heb ik zelfstandig gemaakt. Hier wordt in een later hoofdstuk grondig over uitgelegd.
    
De sourcecode van de applicatie is hier terug te vinden:
[GitHub](https://github.com/mbroer/ads_portfolio/tree/main/apps/cofano)

<h3>1.4 Planning</h3>
Ik heb gedurende de projecten gebruik gemaakt van de scrumtool Trello, Ik heb geprobeerd iedereen in de projectgroep aan te moedigen om ook van deze tool gebruik te maken, maar dit is alleen gedurende het eerste project gedaan. Ik ben wel gebruik blijven maken van het scrumboard gedurende het tweede project.<br>
	
Verder zijn wij als groep elke maandag en woensdag fysiek op de HHS in Den Haag bij elkaar gekomen, en vrijdag in Delft, om aan de projecten te werken.<br>

Hieronder staan alle scrum tickets op mijn naam die ik heb afgerond. Bij de meeste tickets heb ik een beschrijving van een paar zinnen zodat andere projectleden een beter inzicht kregen van waar ik mee bezig was.</br></br>

  <details>
    <summary><h4>Tickets week 1 tm 5</h4></summary>
    
![Week 1 tot en met 5](https://github.com/mbroer/ads_portfolio/blob/main/scrum/1-5.png)
    
  </details>
  

  <details>
    <summary><h4>Tickets week 6 tm 10</h4></summary>
    
![Week 6 tot en met 10](https://github.com/mbroer/ads_portfolio/blob/main/scrum/6-10.png)
    
  </details>
  

  <details>
    <summary><h4>Tickets week 11 tm 16</h4></summary>
    
![Week 11 tot en met 16](https://github.com/mbroer/ads_portfolio/blob/main/scrum/11-16.png)
  
<h4>Opmerking week 14</h4>
  Ik had een leuke stageplek gevonden die mij zeer goed financieel wilden compenseren, hiervoor moest ik een applicatie maken om mijn kennis te laten zien voordat ze me de stageplek konden geven. Hiervoor had ik een week de tijd en heb dus (met begrip van de groep) deze week niet aan het project gewerkt om 100% van mijn tijd in deze applicatie te kunnen steken. (En ja ik heb de stageplek gekregen.)
  
</details> 

## [&#8592; Terug naar index](https://github.com/mbroer/ads_portfolio/blob/main/README.md)
