# AI Transcript – Lab 3: Sensor Data Visualization

This transcript documents the AI-assisted interactions used during the development of Lab 3. Only technical interactions related to code, debugging, documentation, Git/GitHub workflow, and assignment requirements are included.

---

## Turn 1 — Understanding assignment requirements
**User Prompt:**  
I’m confused about what exactly needs to be submitted for Lab 3. What files do I need, and what will the TAs check?

**AI Response:**  
You need a public GitHub repo containing:  
- lab3_sensor_plots.ipynb (3 plots)  
- generate_plots.py (with NumPy-style docstrings)  
- sensor_plots.png  
- README.md (installation, usage, AI disclosure)  
- .gitignore  
- 5+ atomic commits with descriptive messages  

TAs will check: plot quality, docstring quality, README clarity, commit history, AI transcript, and AI disclosure.

---

## Turn 2 — Writing and fixing Python code
**User Prompt:**  
I need help writing the Python script that generates the plots. How should I structure generate_plots.py?

**AI Response:**  
Create a script with three functions: one for the scatter plot, one for the histogram, and one for the boxplot. Import matplotlib and numpy. Each function should load the data, generate the plot, label axes, add a title, and save the figure. Include a main() function that calls all three plot functions.

---

## Turn 3 — Adding NumPy-style docstrings
**User Prompt:**  
Can you help me write NumPy-style docstrings for my functions?

**AI Response:**  
Use this structure for each function:
def scatter_plot(data):
"""
Generate a scatter plot of the sensor data.

Parameters
----------
data : array-like
The input sensor data.

Returns
-------
None
Saves the plot as a PNG file.
"""

Repeat this format for the histogram and boxplot functions.

---

## Turn 4 — Jupyter notebook help
**User Prompt:**  
How do I display the saved PNG image inside my notebook?

**AI Response:**  
Use:
from IPython.display import Image
Image(filename="sensor_plots.png")

Place this after running your script so the PNG is generated first. Add markdown cells explaining each plot and your analysis.

---

## Turn 5 — README creation
**User Prompt:**  
I need help writing my README. What should it include?

**AI Response:**  
Your README should contain:  
- Project description  
- Installation instructions (Python, matplotlib, numpy)  
- Usage instructions (`python generate_plots.py`)  
- How to view the notebook  
- AI disclosure describing how Copilot assisted with debugging, docstrings, and explanations

---

## Turn 6 — Git/GitHub workflow for lab files
**User Prompt:**  
How do I add and push my files to GitHub?

**AI Response:**  
Use:
git add .
git commit -m "Add Lab 3 files"
git push

Make sure your repo has the correct structure and all required files. Keep commits atomic and descriptive.

---

## Turn 7 — Preparing final submission
**User Prompt:**  
What do I still need to finish before submitting?

**AI Response:**  
You need:  
- Public repo link  
- PR link  
- AI transcript  
- Confirm 5+ commits  
- Confirm README, docstrings, and plots meet rubric requirements

---

# Summary
AI assistance (Microsoft Copilot) was used for:
- Debugging Python code  
- Explaining errors  
- Writing docstrings  
- Writing README sections  
- Guiding Git/GitHub workflow  
- Understanding assignment requirements  

All code was reviewed and understood before submission.


