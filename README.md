# ted-cruz-dei-anal
Replicating data analysis from the U.S. Senate Committee on Commerce, Science, and Transportation [report on DEI](https://www.commerce.senate.gov/services/files/4BD2D522-2092-4246-91A5-58EEF99750BC).

## Keywords
The `keywords` folder contains semicolon-delineated files listing the keywords/phrases corresponding to each DEI "category" identified in the report. 

These are copy-pasted from Appendix B in the report. However, I fixed a small number of apparent typos in the keyword lists before uploading; It remains to be determined if those typos were intentional or mistaken, as the report claims that inclusion of some typos in keywords was intentional.

## Data
You can download the grants data with categorized keyword matches from the given lists [here](https://www.cs.cmu.edu/~slab/keyword_matches.csv) (csv format). Matching was performed using the provided `search_keywords.py` script.

You can download the raw(-ish) grants data (csv format) [here](https://www.cs.cmu.edu/~slab/Filtered_Assistance_PrimeAwardSummaries_2025-01-31_H17M26S25_1.csv).

Following the methodology described in Appendix A to the best of my ability, I did a search on [usaspending.gov](usaspending.gov) for grants from the NSF limited to the dates: January 21, 2021 -- April 4, 2024. 
<img width="1445" alt="image" src="https://github.com/user-attachments/assets/495911ff-cade-4077-bbe9-70c6901c7afa" />

This results in 57,438 results. Further filtering by the `award_base_action_date` by the January 21, 2021 -- April 4, 2024 results in 38,148 rows. This does not equal the 32,198 rows described in the report, however this could be explained by additional data being uploaded to usaspending.gov after the original query used for constructing the report, and ours. TBD.  
