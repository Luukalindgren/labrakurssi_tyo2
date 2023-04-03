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
