import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import difflib
import numpy as np
import matplotlib.image as mpimg
from PIL import Image
import io
import base64
import json
import os

BASE_PATH = "C:\\Users\\intro\\Documents\\sanskrit_ocr_paper\\distill-blog-template\\assets\\post-correction\\"

def generate_highlighted_text(line1, line2):
    """Generate HTML for highlighted text comparison"""
    diff = list(difflib.ndiff(line1, line2))
    
    highlighted_line1 = []
    highlighted_line2 = []
    
    i = 0
    while i < len(diff):
        if diff[i].startswith('- ') and i+1 < len(diff) and diff[i+1].startswith('+ '):
            # Replace operation
            highlighted_line1.append(f'<span style="background-color:yellow;font-weight:bold">{diff[i][2:]}</span>')
            highlighted_line2.append(f'<span style="background-color:yellow;font-weight:bold">{diff[i+1][2:]}</span>')
            i += 2
        elif diff[i].startswith('- '):
            # Delete operation
            highlighted_line1.append(f'<span style="background-color:lightblue;font-weight:bold">{diff[i][2:]}</span>')
            highlighted_line2.append(f'<span style="background-color:lightblue;font-weight:bold"> </span>')
            i += 1
        elif diff[i].startswith('+ '):
            # Insert operation
            highlighted_line1.append(f'<span style="background-color:lightcoral;font-weight:bold"> </span>')
            highlighted_line2.append(f'<span style="background-color:lightcoral;font-weight:bold">{diff[i][2:]}</span>')
            i += 1
        elif diff[i].startswith('  '):
            # Unchanged characters
            highlighted_line1.append(f'{diff[i][2:]}')
            highlighted_line2.append(f'{diff[i][2:]}')
            i += 1
        else:
            # Skip '?' lines
            i += 1
    
    return ''.join(highlighted_line1), ''.join(highlighted_line2)

def get_image_as_base64(image_path):
    """Convert image to base64 string for embedding in HTML"""
    try:
        # Handle different path formats
        parts = image_path.split('/')
        if len(parts) > 4:
            # Adjust path similar to the original code
            parts = parts[4:]
            relative_path = '/'.join(parts)
        else:
            relative_path = image_path
            
        # Try to open the image
        with Image.open(BASE_PATH+relative_path) as img:
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
    except Exception as e:
        print(f"Error loading image: {e}")
        # Return a placeholder if image loading fails
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="

def create_static_text_comparison_widget():
    """Create a static HTML widget that works on GitHub Pages"""
    
    # Load the data
    df = load_data()
    
    # Pre-process data for all indices
    processed_data = []
    # for index in range(len(df)):
    for index in range(10):
        ocr_text, gt_text = generate_highlighted_text(df['input_text'].iloc[index], df['target_text'].iloc[index])
        post_text, gt_text2 = generate_highlighted_text(df['predicted_text'].iloc[index], df['target_text'].iloc[index])
        
        image_src = get_image_as_base64(df['path'].iloc[index])
        
        processed_data.append({
            'index': index,
            'image': image_src,
            'pre_cer': f"{df['pre_cer'].iloc[index]*100:.2f}%",
            'post_cer': f"{df['post_cer'].iloc[index]*100:.2f}%",
            'ocr_text': ocr_text,
            'gt_text': gt_text,
            'post_text': post_text,
            'gt_text2': gt_text2
        })
    
    # Create HTML with JavaScript for client-side navigation
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .widget-container {
                font-family: Arial, sans-serif;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .nav-buttons {
                margin-bottom: 20px;
                display: flex;
                gap: 10px;
            }
            button {
                padding: 8px 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 4px;
            }
            button:hover {
                background-color: #45a049;
            }
            .image-container {
                margin-bottom: 20px;
                text-align: center;
            }
            .image-container img {
                max-width: 100%;
                max-height: 400px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }
            th {
                background-color: paleturquoise;
            }
            tr:nth-child(even) {
                background-color: lavender;
            }
            .legend span {
                margin-right: 15px;
            }
            .text-container {
                overflow-x: auto;
            }
        </style>
    </head>
    <body>
        <div class="widget-container">
            <h2 id="title">Text Comparison - Index: 0</h2>
            
            <div class="nav-buttons">
                <button onclick="previousItem()">Previous</button>
                <span id="index-display">Item 1 of DATA_LENGTH</span>
                <button onclick="nextItem()">Next</button>
            </div>
            
            <div class="image-container">
                <img id="line-image" src="" alt="Line Image">
            </div>
            
            <table>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>CER Before Post Correction</td>
                    <td id="pre-cer"></td>
                </tr>
                <tr>
                    <td>CER After Post Correction</td>
                    <td id="post-cer"></td>
                </tr>
                <tr>
                    <td>Legend</td>
                    <td class="legend">
                        <span style="color:blue;font-weight:bold">Blue</span>: Extra 
                        <span style="color:red;font-weight:bold">Red</span>: Missing 
                        <span style="color:yellow;background-color:#eee;font-weight:bold">Yellow</span>: Replaced
                    </td>
                </tr>
            </table>
            
            <div class="text-container">
                <table>
                    <tr>
                        <th>Type</th>
                        <th>Text</th>
                    </tr>
                    <tr>
                        <td>OCR Output</td>
                        <td id="ocr-text"></td>
                    </tr>
                    <tr>
                        <td>Ground Truth</td>
                        <td id="gt-text"></td>
                    </tr>
                    <tr>
                        <td>Post Corrected</td>
                        <td id="post-text"></td>
                    </tr>
                    <tr>
                        <td>Ground Truth</td>
                        <td id="gt-text2"></td>
                    </tr>
                </table>
            </div>
        </div>

        <script>
            // Data is embedded directly in the HTML
            const data = DATA_PLACEHOLDER;
            let currentIndex = 0;
            
            function updateDisplay() {
                const item = data[currentIndex];
                document.getElementById('title').textContent = `Text Comparison - Index: ${item.index}`;
                document.getElementById('index-display').textContent = `Item ${currentIndex + 1} of ${data.length}`;
                document.getElementById('line-image').src = item.image;
                document.getElementById('pre-cer').textContent = item.pre_cer;
                document.getElementById('post-cer').textContent = item.post_cer;
                
                // Use innerHTML to properly render the HTML within the spans
                document.getElementById('ocr-text').innerHTML = item.ocr_text;
                document.getElementById('gt-text').innerHTML = item.gt_text;
                document.getElementById('post-text').innerHTML = item.post_text;
                document.getElementById('gt-text2').innerHTML = item.gt_text2;
            }
            
            function previousItem() {
                if (currentIndex > 0) {
                    currentIndex--;
                    updateDisplay();
                }
            }
            
            function nextItem() {
                if (currentIndex < data.length - 1) {
                    currentIndex++;
                    updateDisplay();
                }
            }
            
            // Initialize display
            updateDisplay();
        </script>
    </body>
    </html>
    """
    
    # Replace placeholders with actual data
    html = html.replace('DATA_PLACEHOLDER', json.dumps(processed_data))
    html = html.replace('DATA_LENGTH', str(len(processed_data)))
    
    # Ensure directory exists
    # os.makedirs('fragments', exist_ok=True)
    
    # Save the full HTML file for testing
    # with open('C:\\Users\\intro\\Documents\\sanskrit_ocr_paper\\distill-blog-template\\src\\fragments\\ocrfull.html', 'w', encoding='utf-8') as f:
    #     f.write(html)
    
    # Extract just the body content for the fragment
    start_idx = html.find('<div class="widget-container">')
    end_idx = html.find('</body>')
    fragment = html[start_idx:end_idx]
    
    # Add the necessary styles and scripts
    styles = html[html.find('<style>'):html.find('</style>') + 8]
    scripts = html[html.find('<script>'):html.find('</script>') + 9]
    
    fragment = styles + fragment + scripts
    
    # Save as fragment
    with open('C:\\Users\\intro\Documents\\sanskrit_ocr_paper\\distill-blog-template\\src\\fragments\\ocr.html', 'w', encoding='utf-8') as f:
        f.write(fragment)
    
    print("Widget saved as fragments/text_comparison_widget.html")
    print("Full HTML version saved as fragments/text_comparison_widget_full.html")

# Load the data
def load_data():
    fold_1_path = BASE_PATH+'outputs\\experiment_1\\test_fold_1\\'
    fold_2_path = BASE_PATH+'outputs\\experiment_1\\test_fold_2\\'
    fold_3_path = BASE_PATH+'outputs\\experiment_1\\test_fold_3\\'
    
    try:
        # Load and combine the results from all folds
        csv_file_path_1 = fold_1_path + 'analysis.csv'
        csv_file_path_2 = fold_2_path + 'analysis.csv'
        csv_file_path_3 = fold_3_path + 'analysis.csv'
        
        df_1 = pd.read_csv(csv_file_path_1, delimiter=';', encoding='utf-8')
        df_2 = pd.read_csv(csv_file_path_2, delimiter=';', encoding='utf-8')
        df_3 = pd.read_csv(csv_file_path_3, delimiter=';', encoding='utf-8')
        
        # Combine all dataframes
        df = pd.concat([df_1, df_2, df_3], axis=0, ignore_index=True)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        # Return example data if loading fails
        return pd.DataFrame({
            'input_text': ['abcdefg', 'testing12', 'hello world'],
            'target_text': ['abxcefh', 'testing123', 'helo world'],
            'predicted_text': ['abxcefh', 'testing123', 'hello world'],
            'pre_cer': [0.14, 0.11, 0.09],
            'post_cer': [0.0, 0.0, 0.09],
            'path': ['example/path.png', 'example/path2.png', 'example/path3.png']
        })

# Run the function to create the widget
create_static_text_comparison_widget()