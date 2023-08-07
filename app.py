import streamlit as st

titels = ['munten','kraaien','wijn','konijnen','schoolfeest']

tabs = st.tabs(titels)

opgave = ["Ik heb 40 muntstukken in mijn portemonnee. Het zijn munten van 20 cent en munten van 1 euro. Het totale bedrag dat deze munten waard zijn is 25,60 euro. Hoeveel 1-euro en hoeveel 20-cent munten heb ik?",
          """Achter in mijn tuin zitten een vast aantal kraaien (k) op een vast aantal paaltjes (p)
Als op elk paaltje één kraai zit, zijn er 20 kraaien over.
Als de kraaien een beetje sociaal zijn gaan ze met z'n tweeën op een paaltje zitten.
In dat geval blijven  er 10 paaltjes leeg.
Hoeveel kraaien en hoeveel paaltjes heb ik in mijn tuin?""",
    """Vijf flessen whisky en acht flessen wijn kosten samen 146 euro.
Vier flessen whisky en twee flessen wijn kosten samen 86 euro. 
Hoeveel kost een fles whisky?""", 
"""De buurman van Jolanda heeft een groot hok in zijn tuin met een boel kippen en konijnen. Jolanda is aan het tellen geweest en heeft ontdekt dat er in het hok  108 poten rondlopen en dat er 39 koppen zijn. Hoeveel konijnen en hoeveel kippen zijn er?""",
"""Voor het komende schoolfeest is de leerlingenvereniging kaartjes aan het verkopen. Kaartjes voor leerlingen kosten  €2,50 en kaartjes voor ouders kosten €4,00. Na een poosje komen ze er achter dat eigenlijk niemand heeft bijgehouden hoeveel kaartjes van elke soort zijn verkocht. Het enige dat de verkopers kunnen melden is dat er in totaal 80 kaartjes zijn verkocht voor samen €242,00.
Hoeveel van elke soort zijn er verkocht?"""]

oplossingen = [{'1 euro':22, '20 cent':8},
               {'kraaien':60, 'paaltjes':40},
               {'wijn':7, 'wisky':18},
               {'konijnen':15,'kippen':24},
               {'kinderen':52,'ouders':28}]

for i in range(len(opgave)):
    with tabs[i]:
        my_titel = titels[i]
        deze_opgave = opgave[i]
        my_oplossing = oplossingen[i]

        st.write(deze_opgave)
        x_key, y_key = my_oplossing.keys()
        x = st.slider(x_key, min_value=0, max_value=100)
        y = st.slider(y_key, min_value=0, max_value=100)

        if x == my_oplossing[x_key] and y == my_oplossing[y_key]:
            st.balloons()

