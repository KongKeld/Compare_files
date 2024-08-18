def compare_files_unordered(file1, file2):
  """Sammenligner to tekstfiler og returnerer True, hvis indholdet er det samme,
  bortset fra rækkefølgen.

  Args:
    file1: Navnet på den første tekstfil.
    file2: Navnet på den anden tekstfil.

  Returns:
    True, hvis filerne har samme indhold, ellers False.
  """

  with open(file1, 'r') as f1, open(file2, 'r') as f2:
    set1 = set(line.strip() for line in f1)
    set2 = set(line.strip() for line in f2)

  return set1 == set2

# Angiv den fulde sti til filerne
base_path = "D:\\GIT\\Compare_files\\"
file1 = base_path + "fil1.txt"
file2 = base_path + "fil2.txt"

if compare_files_unordered(file1, file2):
  print("Filerne har samme indhold, bortset fra rækkefølgen.")
else:
  print("Filerne har forskelligt indhold.")