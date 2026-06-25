 ?? NCBI Sequence Downloader
A Python-based bioinformatics tool that automatically retrieves nucleotide sequences from the NCBI database and saves them in FASTA format along with metadata.
 ?? Features
 ?? Search NCBI using gene names or keywords
 ?? Download multiple FASTA sequences automatically
 ?? Export metadata (ID, description, length, GC content) to CSV
 ?? Built using Biopython
 ?? Supports both CLI and interactive modes
 ?? Project Structure

ncbi_sequence_downloader/
??? downloader/
?     ??? __init__.py
?     ??? fetch.py
?
??? main_cli.py
??? main_interactive.py
??? results/
??? requirements.txt
??? README.md
 ?? Installation

```bash
pip install biopython

 ? Usage
 CLI Mode
```bash
python main_cli.py -q "BRCA1 human" -n 5 -o brca1.fasta
 Interactive Mode

```bash
python main_interactive.py

 ?? Output
All results are saved in the `results/` folder:
 FASTA file (sequence data)
 metadata.csv (ID, description, length, GC content)

 ?? Technologies Used

 Python
 Biopython
 NCBI Entrez API

 ?? Future Improvements
 Add organism filtering
 Add progress bar
 Add error handling and retry system
 Convert to web app / mobile app

 ????? Author

James Justin Egahi
Bioinformatics Enthusiast | Computational Biology Learner
