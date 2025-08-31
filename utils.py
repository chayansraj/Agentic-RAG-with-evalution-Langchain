import os
from dotenv import load_dotenv, find_dotenv

def set_api_key(var):
    try:
        
        # Load the .env file
        env_path = find_dotenv()
        
        # If the .env file is not found, raise an error
        if not env_path:
            raise FileNotFoundError('.env file not found')

        # Load the .env file
        load_dotenv(env_path, override=True)

        # Get the API key from the .env file
        api_key = os.environ.get(var)

        # If the API key is not found, raise an error
        if not api_key:
            raise KeyError(f'{var} not found in .env file')
        
        print(f"API key found in .env file for {var}")
        print("API key set successfully.")
        return api_key
        

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")