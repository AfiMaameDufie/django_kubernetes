from django.shortcuts import render
import requests

def cat_meme_generator(request):
    # The Cat API endpoint for random cat memes
    api_url = "https://api.thecatapi.com/v1/images/search"

    # Make a request to the API
    response = requests.get(api_url)

    # Parse the JSON response
    if response.status_code == 200:
        cat_meme_url = response.json()[0]['url']
    else:
        cat_meme_url = None

    # Render the template with the cat meme URL
    return render(request, 'cat_meme_generator/cat_meme_generator.html', {'cat_meme_url': cat_meme_url})
