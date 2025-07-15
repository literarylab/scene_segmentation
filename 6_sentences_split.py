import os
import re
import pandas as pd
import spacy

# Load the English model from spaCy
nlp = spacy.load("en_core_web_md")

# Define the folder containing the text files
folder_path = "combined_training_set"

# Regular expression patterns to remove
patterns = [r'\n\d+\n[A-Z ]+\n', r'-\n']
#patterns = [r'Chapter \d+', r'Chapter [A-Z]*', r'\*+', r'Prologue', r'Epilogue']

def clean_text(text):
    if isinstance(text, str):
        for pattern in patterns:
            text = re.sub(pattern, '', text)
    return text.strip()

def read_texts_from_folder(folder_path):
    """Reads all .txt files from the given folder and returns a dictionary with file names as keys and contents as values."""
    texts = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):  # Process only .txt files
            with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as file:
                texts[file_name] = file.read()
    return texts

def split_into_sentences(text):
    """Splits text into individual sentences using spaCy."""
    doc = nlp(text)
    return [clean_text(sent.text) for sent in doc.sents if clean_text(sent.text)]

def create_six_sentence_segments(sentences):
    """Creates segments of 6 sentences each using a sliding window."""
    segments = [
        " ".join(sentences[i:i + 6]) 
        for i in range(0, len(sentences), 6)  # Step of 6 for non-overlapping segments
    ]
    return segments

def process_scene_changes(segments):
    """Processes scene changes by detecting '#####' markers and updating segments."""
    processed_segments = []
    flag_next = False
    
    for segment in segments:
        if flag_next:
            scene_change = "yes"
            flag_next = False  # Reset flag
        elif re.search(r"#{5}", segment):
            scene_change = "yes"
            flag_next = True  # Mark the next segment
        else:
            scene_change = "no"
        
        segment_cleaned = re.sub(r"#{5}", "", segment).strip()
        processed_segments.append({"Segment": segment_cleaned, "scene-change": scene_change})
    
    return processed_segments

def process_folder_to_segments(folder_path, output_folder=None):
    """Processes all text files in a folder, splits them into 6-sentence segments, and processes scene changes."""
    texts = read_texts_from_folder(folder_path)
    for file_name, text in texts.items():
        sentences = split_into_sentences(text)
        segments = create_six_sentence_segments(sentences)
        processed_segments = process_scene_changes(segments)
        
        df = pd.DataFrame(processed_segments)
        
        # Save the DataFrame to an Excel file
        if output_folder:
            os.makedirs(output_folder, exist_ok=True)
            output_file = os.path.join(output_folder, f"{file_name}_segments.xlsx")
        else:
            output_file = f"{file_name}_segments.xlsx"
        
        df.to_excel(output_file, index=False, engine='openpyxl')  # Save as Excel
        print(f"Processed and saved: {output_file}")

# Example usage
folder_path = '/Users/sguhr/Desktop/Arbeitslaptop/TU_Darmstadt/2023:24/Stanford24/Dime_Novel_Project/20250715_men_made_in_america_txt/cleaned/cleaned/20250715_cleaned_MMinAm'  # Replace with your folder path
output_folder = "/Users/sguhr/Desktop/Arbeitslaptop/TU_Darmstadt/2023:24/Stanford24/Dime_Novel_Project/BERTmodel/20250313_SIGHMU_Try_Scene_Change/segmented_39_Men_made_in_A"  # Output folder for Excel Sheets

# Process the folder and save results
process_folder_to_segments(folder_path, output_folder=output_folder)
