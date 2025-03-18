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
        ocr_text, _ = generate_highlighted_text(df['input_text'].iloc[index], df['target_text'].iloc[index])
        post_text, _ = generate_highlighted_text(df['predicted_text'].iloc[index], df['target_text'].iloc[index])
        # Ground truth is plain text without highlighting
        gt_text = df['target_text'].iloc[index]
        
        image_src = get_image_as_base64(df['path'].iloc[index])
        
        processed_data.append({
            'index': index,
            'image': image_src,
            'pre_cer': f"{df['pre_cer'].iloc[index]*100:.2f}%",
            'post_cer': f"{df['post_cer'].iloc[index]*100:.2f}%",
            'ocr_text': ocr_text,
            'post_text': post_text,
            'gt_text': gt_text
        })
    
    # Create the fragment HTML - no DOCTYPE, html, head, or body tags
    fragment_html = """
    <style>
        .widget-container {
            font-family: Arial, sans-serif;
            max-width: 100%;
            margin: 0 auto;
            padding: 10px;
        }
        .nav-buttons {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
            align-items: center;
            flex-wrap: wrap;
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
            height: 200px; /* Fixed height for image container */
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .image-container img {
            max-width: 100%;
            max-height: 200px;
            object-fit: contain;
        }
        .compare-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            table-layout: fixed; /* Fixed layout to maintain consistent width */
        }
        .compare-table td {
            border: 1px solid #ddd;
            padding: 8px;
            vertical-align: middle;
        }
        .label-column {
            width: 100px; /* Fixed width for label column */
            background-color: paleturquoise;
            font-weight: bold;
        }
        .text-column {
            width: calc(100% - 100px);
            word-wrap: break-word; /* Allow text to wrap */
        }
        .text-row:nth-child(even) .text-column {
            background-color: lavender;
        }
        .metrics-table {
            margin-top: 20px;
        }
        .legend span {
            margin-right: 15px;
        }
        .text-container {
            overflow-x: auto;
        }
        /* Make text cells consistent height */
        .text-cell {
            min-height: 24px;
            line-height: 1.5;
        }
        /* Mobile responsive styles */
        @media (max-width: 768px) {
            .label-column {
                width: 80px;
                font-size: 14px;
                padding: 6px;
            }
            .text-column {
                width: calc(100% - 80px);
                font-size: 14px;
            }
            .nav-buttons {
                justify-content: center;
            }
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
        
        <!-- Text comparison first, as requested, with no headers -->
        <div class="text-container">
            <table class="compare-table">
                <tr class="text-row">
                    <td class="label-column">OCR Output</td>
                    <td class="text-column" id="ocr-text"></td>
                </tr>
                <tr class="text-row">
                    <td class="label-column">Post Corrected</td>
                    <td class="text-column" id="post-text"></td>
                </tr>
                <tr class="text-row">
                    <td class="label-column">Ground Truth</td>
                    <td class="text-column" id="gt-text"></td>
                </tr>
            </table>
        </div>
        
        <!-- Metrics table moved below text comparison -->
        <table class="compare-table metrics-table">
            <tr>
                <td class="label-column">CER Before</td>
                <td class="text-column" id="pre-cer"></td>
            </tr>
            <tr>
                <td class="label-column">CER After</td>
                <td class="text-column" id="post-cer"></td>
            </tr>
            <tr>
                <td class="label-column">Legend</td>
                <td class="text-column legend">
                    <span style="color:blue;font-weight:bold">Blue</span>: Extra 
                    <span style="color:red;font-weight:bold">Red</span>: Missing 
                    <span style="color:yellow;background-color:#eee;font-weight:bold">Yellow</span>: Replaced
                </td>
            </tr>
        </table>
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
                
                // Use innerHTML for OCR and post-corrected to properly render highlights
                document.getElementById('ocr-text').innerHTML = item.ocr_text;
                document.getElementById('post-text').innerHTML = item.post_text;
                
                // Use textContent for ground truth (no highlighting)
                document.getElementById('gt-text').textContent = item.gt_text;
                
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
    
    print(f"Fragment saved at: {fragment_path}")

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