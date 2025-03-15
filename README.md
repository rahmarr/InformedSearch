# Membuat struktur folder
import os

base_dir = "praktikum_search_algorithm"
uninformed_dir = os.path.join(base_dir, "uninformed_search")
informed_dir = os.path.join(base_dir, "informed_search")

# Membuat folder jika belum ada
os.makedirs(uninformed_dir, exist_ok=True)
os.makedirs(informed_dir, exist_ok=True)

# Membuat README.md untuk informed_search
readme_content = """# Praktikum Algoritma Pencarian (Search Algorithms)

## Deskripsi
Repository ini berisi implementasi berbagai algoritma pencarian dalam **Python**, khususnya **Informed Search**, yaitu:

- **Greedy Best-First Search**: Algoritma pencarian heuristik yang memilih jalur berdasarkan perkiraan jarak terpendek ke tujuan.
- **A* Search**: Algoritma pencarian yang menggabungkan pendekatan UCS dan Greedy Best-First Search untuk menemukan jalur optimal.

## File dalam Folder `informed_search/`
- `greedy_best_first.py` → Implementasi Greedy Best-First Search
- `a_star_tree.py` → Implementasi A* Tree Search
- `a_star_graph.py` → Implementasi A* Graph Search

## Cara Menjalankan di Google Colab
1. **Clone repository ini ke Google Colab atau komputer lokal**
2. Jalankan masing-masing script Python untuk melihat hasil pencarian

"""

with open(os.path.join(informed_dir, "README.md"), "w") as f:
    f.write(readme_content)

print("Struktur folder dan README.md untuk informed_search telah dibuat.")
