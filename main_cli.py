import argparse
from downloader.fetch import fetch_sequences

def main():
    print("=== NCBI Sequence Downloader (CLI Mode) ===")

    parser = argparse.ArgumentParser(
        description="Download FASTA sequences from NCBI"
    )

    parser.add_argument(
        "-q", "--query",
        required=True,
        help="Search term (e.g. BRCA1 human)"
    )

    parser.add_argument(
        "-n", "--number",
        type=int,
        default=10,
        help="Number of sequences to download"
    )

    parser.add_argument(
        "-o", "--output",
        default="output.fasta",
        help="Output FASTA file name"
    )

    args = parser.parse_args()

    print(f"Query: {args.query}")
    print(f"Number of sequences: {args.number}")
    print(f"Output file: {args.output}")

    count = fetch_sequences(
        args.query,
        args.number,
        args.output,
        "metadata.csv"
    )

    print(f"\nDownloaded {count} sequences successfully!")

if __name__ == "__main__":
    main()