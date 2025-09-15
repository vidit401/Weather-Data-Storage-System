# Weather Record ADT
class Record:
    def __init__(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature

    def __str__(self):
        return f"{self.date} | {self.city} | {self.temperature}°C"


class WeatherSystem:
    def __init__(self, years, cities):
        self.city_index = {city: i for i, city in enumerate(cities)}
        self.year_index = {year: i for i, year in enumerate(years)}
        self.data = [[None for _ in range(len(cities))] for _ in range(len(years))]
        self.cities = cities
        self.years = years

    def add_record(self, year, city, temperature):
        if year in self.year_index and city in self.city_index:
            self.data[self.year_index[year]][self.city_index[city]] = temperature
            print("Inserted", temperature, "for", city, "in", year)

    def remove_record(self, year, city):
        if year in self.year_index and city in self.city_index:
            self.data[self.year_index[year]][self.city_index[city]] = None
            print("Deleted record for", city, "in", year)

    def get_record(self, city, year):
        if year in self.year_index and city in self.city_index:
            return self.data[self.year_index[year]][self.city_index[city]]
        return None

    def show_by_years(self):
        print("Row-Major Access:")
        for i, year in enumerate(self.years):
            for j, city in enumerate(self.cities):
                print(f"{year}, {city}: {self.data[i][j]}")

    def show_by_cities(self):
        print("Column-Major Access:")
        for j, city in enumerate(self.cities):
            for i, year in enumerate(self.years):
                print(f"{year}, {city}: {self.data[i][j]}")

    def show_available(self):
        print("Sparse Data Records:")
        for i, year in enumerate(self.years):
            for j, city in enumerate(self.cities):
                if self.data[i][j] is not None:
                    print(f"{year}, {city}: {self.data[i][j]}")

    def show_complexity(self):
        info = {
            "add_record": "O(1) time, O(1) space (direct indexing)",
            "remove_record": "O(1) time, O(1) space",
            "get_record": "O(1) time, O(1) space",
            "show_by_years": "O(n*m) time, O(1) space",
            "show_by_cities": "O(n*m) time, O(1) space",
            "storage": f"O(n*m) space where n={len(self.years)}, m={len(self.cities)}"
        }
        return info


def main():
    years_text = input("Enter years (comma-separated, e.g., 2022,2023,2024): ")
    years = [int(y.strip()) for y in years_text.split(",") if y.strip().isdigit()]
    cities_text = input("Enter cities (comma-separated, e.g., Delhi,Mumbai,Chennai): ")
    cities = [c.strip() for c in cities_text.split(",") if c.strip()]
    system = WeatherSystem(years, cities)

    while True:
        print("\nMenu:")
        print("1) Add data")
        print("2) Remove data")
        print("3) Get data")
        print("4) Show data by years")
        print("5) Show data by cities")
        print("6) Show available data")
        print("7) Show complexity info")
        print("8) Exit program")
        choice = input("Enter your choice (1-8): ").strip()
        if choice == "1":
            try:
                year = int(input("Enter year: "))
                city = input("Enter city: ").strip()
                temperature = float(input("Enter temperature: "))
                system.add_record(year, city, temperature)
            except Exception as e:
                print("Invalid input:", e)
        elif choice == "2":
            try:
                year = int(input("Enter year: "))
                city = input("Enter city: ").strip()
                system.remove_record(year, city)
            except Exception as e:
                print("Invalid input:", e)
        elif choice == "3":
            try:
                year = int(input("Enter year: "))
                city = input("Enter city: ").strip()
                result = system.get_record(city, year)
                if result is not None:
                    print(f"Temperature for {city} in {year}: {result}")
                else:
                    print("No record found.")
            except Exception as e:
                print("Invalid input:", e)
        elif choice == "4":
            print("\n--- Row Major ---")
            system.show_by_years()
        elif choice == "5":
            print("\n--- Column Major ---")
            system.show_by_cities()
        elif choice == "6":
            print("\n--- Sparse Data ---")
            system.show_available()
        elif choice == "7":
            print("\n--- Complexity Analysis ---")
            for k, v in system.show_complexity().items():
                print(k, ":", v)
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()