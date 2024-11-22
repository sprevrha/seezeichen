"""
Support script for github workflow to display GitHub milestones automatically in the README file
Author: Sven Prevrhal
Date: 2024-11-22
"""
import json

# Load milestones from the JSON file
with open('milestones.json', 'r', encoding='utf-8') as f:
    milestones = json.load(f)

# Generate the milestones section as a checklist
MILESTONE_SECTION = "## Milestones\n\n"
for milestone in milestones:
    status = "[x]" if milestone['state'] == 'closed' else "[ ]"
    MILESTONE_SECTION += f"- {status} **{milestone['title']}**: {milestone['description']} (Due: {milestone['due_on']})\n"

# Read the current README file
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

# Replace the old milestones section with the new one
new_readme_content = readme_content.split('## Milestones')[0] + MILESTONE_SECTION

# Write the updated content back to the README file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme_content)
