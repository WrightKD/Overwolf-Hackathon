from fastapi import FastAPI
import uvicorn
import cassiopeia as cass

cass.set_riot_api_key("API-KEY")

api = FastAPI()

@api.get("/summoner/match/{region}/{username}")
async def get_summoner_match(region, username):

    match_history = cass.get_summoner(name=username, region=region).match_history
    return match_history[0].id

if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)