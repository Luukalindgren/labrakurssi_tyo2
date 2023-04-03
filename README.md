# Discord-botti

Discord-botti joka generoi OpenAI:n tekoälyn avulla kuvia. Syötteeksi voi antaa niin monta sanaa kuin haluaa, tekoäly ei ymmärrä suomea.

# Käyttöohjeet:
1. Kloonaa repo tietokoneellesi
2. Asenna tarvittavat kirjastot: "pip install discord.py python-dotenv openai"
3. Tee itsellesi .env -tiedosto, johon lisätään: "DISCORD_TOKEN", "DISCORD_GUILD" ja "OPENAI_API_KEY"
4. Aja bot.py tiedosto ja botti on käytössä.

--------------------!HUOM!--------------------

Nämä .env tiedoston ympäristömuuttujat ovat yksityisiä


# Käytössä olevat komennot:
  - !help     (Listaa käytettävät komennot ja niiden kuvaukset)
  - !sup      (Testikomento, joka vain lähettää viestin)
  - !coinflip (Heittää kolikkoa: Heads, Tails and on its side)
  - !image <input>  (Kutsuu OpenAI kuva generaattoria, palauttaa sen luoman kuvan annetun syötteen mukaan)


# Esimerkkejä:
![image](https://user-images.githubusercontent.com/70708962/229514079-d1b7fddb-7f0f-4878-9752-35f486aa08b4.png)
![image](https://user-images.githubusercontent.com/70708962/229514107-a98c4616-606a-46ca-b618-589c459bc492.png)
![image](https://user-images.githubusercontent.com/70708962/229514202-4b4a26dc-790e-4264-b2f6-99469f47c569.png)
