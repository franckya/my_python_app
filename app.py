import requests

def get_random_gif(api_key):
    url = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        gif_url = data['data']['image_original_url']
        return gif_url
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GIF from Giphy API: {e}")
        return None

def main():
    giphy_api_key = 'YOUR_GIPHY_API_KEY'  # Replace with your actual Giphy API key
    gif_url = get_random_gif(giphy_api_key)
    if gif_url:
        print(f"Random GIF URL: {gif_url}")

if __name__ == "__main__":
    main()

