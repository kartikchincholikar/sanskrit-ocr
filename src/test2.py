import pandas as pd
import difflib
import io
import base64
import json
from PIL import Image

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
    for index in range(min(10, len(df))):
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
    
    # Create the fragment HTML - no DOCTYPE, html, head, or body tags
    fragment_html = """
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
        .nav-button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 4px;
        }
        .nav-button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
        .nav-button:hover:not(:disabled) {
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
        .compare-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        .compare-table th, .compare-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        .compare-table th {
            background-color: paleturquoise;
        }
        .compare-table tr:nth-child(even) {
            background-color: lavender;
        }
        .legend span {
            margin-right: 15px;
        }
        .text-container {
            overflow-x: auto;
        }
    </style>

    <div class="widget-container">
        <h2 id="ocr-title">Text Comparison - Index: 0</h2>
        
        <div class="nav-buttons">
            <button id="prev-button" class="nav-button">Previous</button>
            <span id="index-display">Item 1 of DATA_LENGTH</span>
            <button id="next-button" class="nav-button">Next</button>
        </div>
        
        <div class="image-container">
            <img id="line-image" src="" alt="Line Image">
        </div>
        
        <table class="compare-table">
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
            <table class="compare-table">
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
        (function() {
            // Data is embedded directly in the HTML
            const data = DATA_PLACEHOLDER;
            let currentIndex = 0;
            
            function updateDisplay() {
                const item = data[currentIndex];
                document.getElementById('ocr-title').textContent = `Text Comparison - Index: ${item.index}`;
                document.getElementById('index-display').textContent = `Item ${currentIndex + 1} of ${data.length}`;
                document.getElementById('line-image').src = item.image;
                document.getElementById('pre-cer').textContent = item.pre_cer;
                document.getElementById('post-cer').textContent = item.post_cer;
                
                // Use innerHTML to properly render the HTML within the spans
                document.getElementById('ocr-text').innerHTML = item.ocr_text;
                document.getElementById('gt-text').innerHTML = item.gt_text;
                document.getElementById('post-text').innerHTML = item.post_text;
                document.getElementById('gt-text2').innerHTML = item.gt_text2;
                
                // Update button states
                document.getElementById('prev-button').disabled = (currentIndex === 0);
                document.getElementById('next-button').disabled = (currentIndex === data.length - 1);
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
            
            // Set up event listeners
            document.getElementById('prev-button').addEventListener('click', previousItem);
            document.getElementById('next-button').addEventListener('click', nextItem);
            
            // Initialize display
            document.addEventListener('DOMContentLoaded', function() {
                updateDisplay();
            });
            
            // Initialize immediately as well (in case script runs after DOM is loaded)
            updateDisplay();
        })();
    </script>
    """
    
    # Replace placeholders with actual data
    fragment_html = fragment_html.replace('DATA_PLACEHOLDER', json.dumps(processed_data))
    fragment_html = fragment_html.replace('DATA_LENGTH', str(len(processed_data)))
    
    # Create full HTML version for direct viewing
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>OCR Text Comparison Widget</title>
    </head>
    <body>
        {fragment_html}
    </body>
    </html>
    """
    
    # Save as fragment
    fragment_path = 'C:\\Users\\intro\\Documents\\sanskrit_ocr_paper\\distill-blog-template\\src\\fragments\\ocr.html'
    with open(fragment_path, 'w', encoding='utf-8') as f:
        f.write(fragment_html)
    
    # # Save full HTML version for direct viewing
    # full_path = 'C:\\Users\\intro\\Documents\\sanskrit_ocr_paper\\distill-blog-template\\src\\fragments\\text_comparison_widget_full.html'
    # with open(full_path, 'w', encoding='utf-8') as f:
    #     f.write(full_html)
    
    print(f"Fragment saved at: {fragment_path}")
    # print(f"Full HTML version saved at: {full_path}")

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
if __name__ == "__main__":
    create_static_text_comparison_widget()