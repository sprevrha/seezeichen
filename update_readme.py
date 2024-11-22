"""
Support script for github workflow to display GitHub milestones automatically in the README file
Author: Sven Prevrhal
Date: 2024-11-22
"""
import json

def load(json_file):
    """
        Load JSON file
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        milestones = json.load(f)
    return milestones

def convert_to_md(milestones):
    """
        Generate the milestones section as a checklist
    """
    milestones_section = ""
    for milestone in milestones:
        status = "[x]" if milestone['state'] == 'closed' else "[ ]"
        milestones_section += f"- {status} [#{milestone['number']}][{milestone['html_url']}] **{milestone['title']}**,  (due: {milestone['due_on']})\n"
    return milestones_section

def main():
    """
    Main 
    """
    end_comment = '<!-- MILESTONES END -->'
    heading = '## Milestones'
    
    new_milestones = load('milestones.json')
    new_milestones_md = convert_to_md(new_milestones)
    
    # Read the current README file
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Split the README content to find the milestones section
    before_milestones, _, after_begin_comment = readme_content.partition(heading)  
    _, _, rest_of_readme = after_begin_comment.partition(end_comment) 
    
    # Combine the content with the updated milestones section
    new_readme_content = before_milestones + heading + '\n' + new_milestones_md + end_comment + '\n' + rest_of_readme

    # Write the updated content back to the README file
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme_content)
    
if __name__ == "__main__":
    main()
