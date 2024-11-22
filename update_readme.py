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
milestones_section = "## Milestones\n\n"
for milestone in milestones:
    status = "[x]" if milestone['state'] == 'closed' else "[ ]"
    milestones_section += f"- {status} **{milestone['title']}**: {milestone['description']} (Due: {milestone['due_on']})\n"

# Read the current README file
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

# Split the README content to find the milestones section
before_milestones, _, after_milestones = readme_content.partition('## Milestones')

# Combine the content with the updated milestones section
new_readme_content = before_milestones + milestones_section + after_milestones.split('\n', 1)[1]

# Write the updated content back to the README file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme_content)
