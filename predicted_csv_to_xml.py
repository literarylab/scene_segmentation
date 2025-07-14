import pandas as pd
import os
import re
from lxml import etree

def insert_scene_change(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return ' '.join(sentences[:3]) + ' <scene-change/> ' + ' '.join(sentences[3:])

def convert_csv_to_tei(csv_path, output_dir=None):
    df = pd.read_csv(csv_path)

    if "Segment" not in df.columns or "predictions" not in df.columns:
        raise ValueError("CSV must contain 'Segment' and 'predictions' columns.")

    base_filename = os.path.splitext(os.path.basename(csv_path))[0]
    
    # Determine output file location
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        xml_filename = os.path.join(output_dir, base_filename + ".xml")
    else:
        # Write XML to same folder as input CSV
        xml_filename = os.path.join(os.path.dirname(csv_path), base_filename + ".xml")

    # Start building XML
    NSMAP = {None: "http://www.tei-c.org/ns/1.0", "xs": "http://www.w3.org/2001/XMLSchema"}
    TEI = etree.Element("TEI", nsmap=NSMAP)
    
    # Header
    teiHeader = etree.SubElement(TEI, "teiHeader")
    fileDesc = etree.SubElement(teiHeader, "fileDesc")
    titleStmt = etree.SubElement(fileDesc, "titleStmt")
    title = etree.SubElement(titleStmt, "title")
    title.text = base_filename + ".xml"

    # Body
    text_el = etree.SubElement(TEI, "text")
    body = etree.SubElement(text_el, "body")
    body_title = etree.SubElement(body, "title")
    body_title.text = base_filename

    # Process rows
    for _, row in df.iterrows():
        segment_text = str(row["Segment"])
        prediction = int(row["predictions"])

        if prediction == 1:
            processed = insert_scene_change(segment_text)
        else:
            processed = segment_text

        parts = processed.split('<scene-change/>')

        if len(parts) == 1:
            seg = etree.SubElement(body, "seg")
            seg.text = parts[0]
        else:
            seg1 = etree.SubElement(body, "seg")
            seg1.text = parts[0]

            scene_el = etree.SubElement(body, "scene-change")

            seg2 = etree.SubElement(body, "seg")
            seg2.text = parts[1]

    # Save file
    tree = etree.ElementTree(TEI)
    tree.write(xml_filename, encoding="UTF-8", xml_declaration=True, pretty_print=True)
    print(f"✅ TEI XML saved to:\n{xml_filename}")

# Example usage
csv_file_path = "/Users/sguhr/Desktop/Arbeitslaptop/TU_Darmstadt/2023:24/Stanford24/Dime_Novel_Project/BERTmodel/20250313_SIGHMU_Try_Scene_Change/predicted_39_Men_made_in_A/Nebraska_predicted_without_deletion_threashold_0.65.csv"
convert_csv_to_tei(csv_file_path)
