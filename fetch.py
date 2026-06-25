import ssl
from Bio import Entrez, SeqIO
import csv

# 🔧 Fix SSL issue
ssl._create_default_https_context = ssl._create_unverified_context

Entrez.email = "your_email@example.com"


def calculate_gc(sequence):
    """
    Function to calculate GC content of a sequence
    """
    seq = str(sequence).upper()
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)


def fetch_sequences(query, max_results=10, output_file="sequences.fasta", csv_file="metadata.csv"):

    print("Step 1: Searching NCBI...")

    search_handle = Entrez.esearch(
        db="nucleotide",
        term=query,
        retmax=max_results
    )

    search_results = Entrez.read(search_handle)
    search_handle.close()

    ids = search_results["IdList"]

    print("IDs found:", ids)

    if not ids:
        print("No sequences found!")
        return 0

    print("Step 2: Fetching sequences...")

    fetch_handle = Entrez.efetch(
        db="nucleotide",
        id=ids,
        rettype="fasta",
        retmode="text"
    )

    sequences = list(SeqIO.parse(fetch_handle, "fasta"))
    fetch_handle.close()

    print("Number of sequences fetched:", len(sequences))

    print("Step 3: Saving FASTA file...")
    SeqIO.write(sequences, output_file, "fasta")

    print("Step 4: Saving metadata CSV...")

    # 📊 Create CSV file
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(["ID", "Description", "Length", "GC_Content"])

        # Write data for each sequence
        for seq in sequences:
            writer.writerow([
                seq.id,
                seq.description,
                len(seq.seq),
                calculate_gc(seq.seq)
            ])

    print("Metadata saved as:", csv_file)

    return len(sequences)