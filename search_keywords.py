import pandas as pd
from acora import AcoraBuilder

# Yes, it's a bit hard-coded right now
file_path = 'data/Filtered_Assistance_PrimeAwardSummaries_2025-01-31_H17M26S25_1.csv'
# columns_to_read = ['award_id_fain', 'prime_award_base_transaction_description']

keyword_categories = ['status', 'race', 'gender', 'social_justice', 'environmental_justice']

DESCRIPTION_FIELD = 'prime_award_base_transaction_description'
ID_FIELD = 'award_id_fain'

# Load grants data from file
df = pd.read_csv(file_path)# , usecols=columns_to_read)

# Load keyword lists from file
keyword_lists = {}
for keyword_category in keyword_categories:
    with open('keywords/{}'.format(keyword_category)) as keywords_file:
        keywords = list(map(lambda s: s.strip(), keywords_file.readline().strip().split(';')))
        keyword_lists[keyword_category] = keywords

# Build keyword indices using acora (Aho-Corasick) library
keyword_indices = {}
for category, keywords in keyword_lists.items():
    builder = AcoraBuilder(keywords)
    ac_index = builder.build()
    keyword_indices[category] = ac_index

# Find and record all the matches for each category in the project descriptions
matches = {category: [] for category in keyword_categories}
for idx, proposal in df.iterrows():
    text = proposal[DESCRIPTION_FIELD]
    proposal_id = proposal[ID_FIELD]
    # matches[proposal_id] = []
    for category, keyword_idx in keyword_indices.items():
        match_list = ''
        result = keyword_idx.findall(text)
        if result:
            # print("{}: {}".format(category, result))
            result_strings_concat = ','.join([r[0] for r in result])
            # print(result_strings_concat)
            match_list = '\"{}\"'.format(result_strings_concat)
        matches[category].append(match_list)

# Stick the matches on to the dataframe
for category, match_col in matches.items():
    df["{}_matches".format(category)] = match_col

# Write new CSV file that includes the string matches for each category
df.to_csv('keyword_matches.csv', index=False)

