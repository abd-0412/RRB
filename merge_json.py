import json
import os

root = r'C:\Users\ABDUL\Downloads\rrb-project'
main_file = os.path.join(root, 'part01.json')

# Load original 100 questions
with open(main_file, 'r', encoding='utf-8') as f:
    final_list = json.load(f)

# Load and append chunks
for i in range(1, 6):
    chunk_path = os.path.join(root, f'scratch_chunk_{i}.json')
    with open(chunk_path, 'r', encoding='utf-8') as f:
        chunk_data = json.load(f)
        final_list.extend(chunk_data)

# Write final consolidated file
with open(main_file, 'w', encoding='utf-8') as f:
    json.dump(final_list, f, indent=2)

print(f"Merge complete. Total questions: {len(final_list)}")
