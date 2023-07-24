from django.shortcuts import render
import aiohttp
import time, requests
import _asyncio
# import time, _asyncio
# Create your views here.


# def example(request):
#     # start_time = time.perf_counter()
#     starting_time=time.time()
    
#     pokemon_data=[]

#     for num in range(1, 101):
#         url =f"https://pokeapi.co/api8/v2/pokemon/{num}"
#         res=requests.get(url)
#         pokemon = res.json()
#         pokemon_data.append(pokemon["name"])
    
#     count = len(pokemon_data)
#     total_time = time.time() - starting_time

#     return render(
#         request, "index.html",
#         {"data": pokemon_data, "count": count,"time": total_time},
#     )

# --------------------------------------

# async def example(request):
#     starting_time = time.time()
#     pokemon_data = []

#     async with aiohttp.ClistenSession() as session:
#         for num in range(1, 101):
#             pokemon_url =f"https://pokeapi.co/api/v2/pokemon/{num}"
#             async with session.set(pokemon_url) as res:
#                 pokemon =await res.json()
#                 pokemon_data.append(pokemon['name'])

#     count = len(pokemon_data)
#     total_time = time.time() - starting_time

#     return render (
#         request, "index.html",
#         {"data": pokemon_data, 
#          "count":count, "time":total_time},
#     )
 
# ------------------------------------------
async def get_pokemon(session, url):
    async with session.get(url) as res:
        pokemon_data = await res.json()
        return pokemon_data



async def example(request):

    starting_time = time.time()

    actions=[]
    pokemon_data=[]

    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            actions.append(_asyncio.ensure_future(get_pokemon(session, url)))
            # actions.append(asyncio.ensure_future(get_pokemon(session, url))) tutorial ahs asyncio wihtout the underscore has in this comment 

        pokemon_res = await _asyncio.gather(*actions)

    count= len(pokemon_data)
    total_time = time.time() - starting_time

    return render(
        request, 
        "index.html",
        {"data": pokemon_data, "count": count, "time": total_time}
    )



# ------------------------------------------

# async def example(request):
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://catfact.ninja/fact") as res:
#             data = await res.json()
#             print(data)
        
#     return render(
#         request, 
#         "index.html",
#         {"data": data},
#     )
