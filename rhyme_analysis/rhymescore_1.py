# -*- coding: utf-8 -*-
"""RhymeScore_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DO35GiefYGRduV6b2sADmuyVCMDZhFyo
"""

import ipywidgets as widgets
from IPython.display import display, HTML
import nltk
from nltk.corpus import cmudict, stopwords

# Download necessary NLTK data
nltk.download('cmudict', quiet=True)
nltk.download('stopwords', quiet=True)

# Initialize CMU Pronouncing Dictionary and stopwords
cmu_dict = cmudict.dict()
stop_words = set(stopwords.words('english'))

# Define colors for highlighting
colors = ['#dfba24', '#d87e3b', '#57d0ca', '#ca3e6b', '#278fbd', '#a5bb51',
          '#7c8bc5', '#fdc47c', '#ab4097', '#54aa00', '#51a587', '#ffb0b1',
          '#d4cb8b', '#d27481', '#b15fc1']

# Function to get phonemes for a word
def get_phonemes(word):
    try:
        return cmu_dict[word.lower()][0]
    except KeyError:
        return []

# Function to calculate phoneme similarity
def phoneme_similarity(phoneme1, phoneme2):
    min_length = min(len(phoneme1), len(phoneme2))
    matches = sum(1 for i in range(1, min_length + 1) if phoneme1[-i] == phoneme2[-i])
    return matches / min_length if min_length > 0 else 0

# Function to determine if two phonemes are near rhymes
def is_near_rhyme(phoneme1, phoneme2):
    similarity = phoneme_similarity(phoneme1, phoneme2)
    return similarity >= 0.5

# UI Components
text_input = widgets.Textarea(value='', placeholder='Type your text here...', description='Text:', layout={'width': '100%', 'height': '100px'})
analyze_button = widgets.Button(description="Analyze Rhymes")
highlight_style_dropdown = widgets.Dropdown(options=['Background', 'Phonemes'], value='Background', description='Highlight Style:')
word_selector = widgets.Dropdown(options=[], description='Select Word:', disabled=True)
analysis_mode_toggle = widgets.ToggleButtons(options=['Full Text', 'Word'], description='Analysis Mode:', value='Full Text')
output_area = widgets.Output()

# Global storage for analysis results
global_rhymes_for_word = {}
global_words_count = 0
global_full_rhyme_score = 0

# Analyze text callback function
def analyze_text_callback(b):
    global global_rhymes_for_word, global_words_count, global_full_rhyme_score
    text = text_input.value.strip()
    words = text.split()
    global_words_count = len(words)
    phonemes = [get_phonemes(word) for word in words]
    global_rhymes_for_word = {word: [] for word in words}
    rhyme_scores = [0] * len(words)

    for i, word_i in enumerate(words):
        for j, word_j in enumerate(words):
            if i != j and (phonemes[i] == phonemes[j] or is_near_rhyme(phonemes[i], phonemes[j])):
                global_rhymes_for_word[word_i].append(word_j)
                rhyme_scores[i] += 1 if word_j not in stop_words else 0.5  # Half score for stopwords

    global_full_rhyme_score = sum(rhyme_scores)
    word_selector.options = words  # Update dropdown options after analysis

    update_display()

# Function to update text display based on analysis mode and selected word
def update_display(selected_word=None):
    selected_word = word_selector.value if analysis_mode_toggle.value == 'Word' and not word_selector.disabled else None
    avg_rhyme_score = global_full_rhyme_score / global_words_count if global_words_count > 0 else 0
    display_html = ""

    for word in text_input.value.strip().split():
        color = colors[hash(word) % len(colors)]
        if analysis_mode_toggle.value == 'Full Text' or word == selected_word or word in global_rhymes_for_word.get(selected_word, []):
            if highlight_style_dropdown.value == 'Background':
                display_html += f'<span style="background-color: {color};">{word}</span> '
            else:  # Phonemes highlighting
                display_html += f'<span style="color: {color};">{word}</span> '
        else:
            display_html += word + " "

    with output_area:
        output_area.clear_output()
        display(HTML(f"<div style='white-space: pre-wrap; max-width: 800px;'>{display_html.strip()}</div>"))
        display(HTML(f"<p>Total Words: {global_words_count}</p>"))
        display(HTML(f"<p>Full Rhyme Score: {global_full_rhyme_score}</p>"))
        display(HTML(f"<p>Average Rhyme Score: {avg_rhyme_score:.2f}</p>"))

# Toggle handling for analysis mode changes
def handle_analysis_mode_change(change):
    word_selector.disabled = (change.new == 'Full Text')
    update_display()

analyze_button.on_click(analyze_text_callback)
word_selector.observe(lambda change: update_display(change['new']), names='value')
highlight_style_dropdown.observe(lambda _: update_display(), names='value')
analysis_mode_toggle.observe(handle_analysis_mode_change, names='value')

# Layout setup to display UI components
display_widgets = widgets.VBox([text_input, analyze_button, analysis_mode_toggle, highlight_style_dropdown, word_selector])
display(display_widgets)
display(output_area)