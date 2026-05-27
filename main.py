from src import load_data
from src import zones

def main():
    data = load_data.load_activity("data/activity.csv")
    mittelwert, maximum = load_data.get_stats(data)
    print(f"Mittelwert: {mittelwert}, Maximum: {maximum}")

    #zones.plot_zones(data)

if __name__ == "__main__":
    main()