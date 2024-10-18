import requests

def get_movie_details(query):
    api_key = "008a1e00964e16e10f2921fcd4c916a6"
    url = f"https://api.themoviedb.org/3/search/movie"
    
    # Parameters for the API request
    params = {
        'api_key': api_key,
        'query': query,
        'language': 'en-US',
        'page': 1,
        'include_adult': False  # This avoids adult content by default
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response
        
        # Check if any movies were found
        if 'results' in data and data['results']:
            for movie in data['results']:
                title = movie.get('title', 'No title available')
                release_date = movie.get('release_date', 'No release date available')
                overview = movie.get('overview', 'No overview available')
                rating = movie.get('vote_average', 'No rating available')
                
                print(f"Movie Title: {title}")
                print(f"Release Date: {release_date}")
                print(f"Overview: {overview}")
                print(f"Rating: {rating}\n{'-' * 40}\n")
        else:
            print("No movies found for your query.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    user_query = input("What movie are you looking for? ")
    get_movie_details(user_query)

if __name__ == "__main__":
    main()
