import os
import re

# Folder containing the .txt files
input_folder = "/Users/sguhr/Desktop/Arbeitslaptop/TU_Darmstadt/2023:24/Stanford24/Dime_Novel_Project/20250715_men_made_in_america_txt/cleaned/cleaned"
output_folder = os.path.join(input_folder, "cleaned")

os.makedirs(output_folder, exist_ok=True)

# Helper regex
uppercase_line = re.compile(r"^[A-Z0-9 .,:'’\-]+$")

def clean_text(text):
    # 1. Remove hyphenation across line breaks: "cul-\nminated" → "culminated"
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)

    # 2. Replace single line breaks within paragraphs with a space
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    # 3. Fix OCR errors: Sbe → She, sbe → she
    text = text.replace("Sbe", "She").replace("sbe", "she")

    # 4. Split into lines for filtering
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if re.match(r'^\d+$', stripped):  # Only digits → remove
            continue
        if stripped.isupper() and len(stripped) > 2:  # ALL-CAPS → remove
            continue
        cleaned_lines.append(line)

    # 5. Join cleaned lines
    text = '\n'.join(cleaned_lines)

    # 6. Normalize double single quotes to one double quote
    text = text.replace("''", '"')

    # 7. Collapse multiple blank lines to a single one
    text = re.sub(r'\n{2,}', '\n', text)

    return text.strip()






# Loop through all .txt files
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as infile:
            raw_text = infile.read()

        cleaned = clean_text(raw_text)

        with open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as outfile:
            outfile.write(cleaned)

print("✅ Cleaning completed. Cleaned files are in:", output_folder)
