import csv

def display_high_scores(file):
    """Reads and displays the top scores from the CSV file."""
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            scores = sorted(reader, key=lambda x: int(x[1]), reverse=True)
            print("\nTop Scores:")
            for name, score in scores[:10]:
                print(f"{name}: {score}")
    except FileNotFoundError:
        print("No scores found. Play a game to generate scores.")

def export_scores(file):
    """Exports scores to a CSV file."""
    try:
        with open(file, 'r') as f:
            data = f.readlines()
        with open("exported_scores.csv", 'w') as f:
            f.writelines(data)
        print("Scores exported successfully!")
    except FileNotFoundError:
        print("No scores to export.")