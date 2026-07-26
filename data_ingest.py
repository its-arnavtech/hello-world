import pandas as pd
import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_api_data(url: str) -> pd.DataFrame:
    """Fetch JSON data from an API and return a pandas DataFrame."""
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    df = pd.json_normalize(data)
    return df


def main() -> None:
    df = fetch_api_data(API_URL)
    print("Loaded DataFrame:")
    print(df.head())

    # Example: select only users in a specific city
    if "address.city" in df.columns:
        city_df = df[df["address.city"] == "South Christy"]
        print("\nUsers in South Christy:")
        print(city_df)

    # Save to CSV if needed
    df.to_csv("api_users.csv", index=False)
    print("\nSaved API data to api_users.csv")


if __name__ == "__main__":
    main()
