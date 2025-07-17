# Rethinking Scene Segmentation. Advancing Automated Detection of Scene Changes in Literary Texts
## Manual and automated scene change annotation of US American popular fiction

This study explores scene change detection in 20th-century US-American romance fiction using manual annotations and automated methods. Manually annotated novels build the training data for fine-tuning an English BERT USE model, yielding promising preliminary results for automated text segmentation in computational literary studies.

### This repository accompanies the paper contributions to NAACL-SIGHUM 2025, Albuquerque, NM, and to ADHO annual conference DH2025, Lisbon.

Svenja Guhr, Huijun Mao, Fengyi Lin, Alexander Sherman, Mark Algee-Hewitt (2025): Scene Change Detection in 20th-Century US-American Romance Fiction. Book of Abstracts of the DH2025, Annual Conference of ADHO, 14.-18.07.2025, Lisbon. 

Svenja Guhr, Huijun Mao, and Fengyi Lin (2025). Rethinking Scene Segmentation. Advancing Automated Detection of Scene Changes in Literary Texts. In Proceedings of the 9th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature (LaTeCH-CLfL 2025), pages 79–86, Albuquerque, New Mexico. Association for Computational Linguistics. https://aclanthology.org/2025.latechclfl-1.8/

Svenja Guhr, Huijun Mao, and Fengyi Lin (2025). Rethinking Scene Segmentation. Advancing Automated Detection of Scene Changes in Literary Texts. The 9th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature, NAACL25 (SIGHUM LaTeCH-CLfL 2025), Poster. Zenodo. https://doi.org/10.5281/zenodo.15281018.

It contains the preprocessing Python scripts and the model used to automate the scene segmentation of our US romance novel corpus.
Since we are working with copyrighted texts, the annotated novels cannot be made publicly available.

Please find the referenced guidelines for the manual annotation process in Gius, E., Sökefeld, C., Dümpelmann, L., Kaufmann, L., Schreiber, A., Guhr, S., Wiedmer, N., & Jannidis, F. (2021). Guidelines for Detection of Scenes (1.0). Zenodo. https://doi.org/10.5281/zenodo.4457176

The paper describes work in progress and does not provide a final solution for reliable scene segmentation, but rather proposes new approaches to the task and obtains promising results for approximating scene change positions in six-sentence segments, contributing a new perspective to the discourse on meaningful literary text segmentation for CLS.
