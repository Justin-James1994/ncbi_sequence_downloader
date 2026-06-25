from downloader.fetch import fetch_sequences

def main():
    print("=== NCBI Sequence Downloader (Interactive Mode) ===")

    query = input("Enter gene or search term: ")

    while True:
        try:
            number = int(input("Enter number of sequences: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    output = input("Enter output FASTA file name (e.g. mydata.fasta): ")

    print("\nProcessing...\n")

    count = fetch_sequences(
        query,
        number,
        output,
        "metadata.csv"
    )

    print(f"\nDownloaded {count} sequences successfully!")

if __name__ == "__main__":
    main()