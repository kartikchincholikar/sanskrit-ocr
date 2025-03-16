import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import difflib
import numpy as np
import matplotlib.image as mpimg
from PIL import Image
import io
import base64

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

def create_text_comparison_widget(df):
    """Create an interactive text comparison widget using Plotly"""
    
    # Get the first item to initialize the widget
    index = 0
    
    # Process the data
    ocr_text, gt_text = generate_highlighted_text(df['input_text'].iloc[index], df['target_text'].iloc[index])
    post_text, gt_text2 = generate_highlighted_text(df['predicted_text'].iloc[index], df['target_text'].iloc[index])
    
    # Get image as base64
    image_src = get_image_as_base64(df['path'].iloc[index])
    
    # Create the figure
    fig = make_subplots(
        rows=3, cols=1,
        row_heights=[0.5, 0.2, 0.3],
        specs=[[{"type": "image"}], [{"type": "table"}], [{"type": "table"}]],
        vertical_spacing=0.05
    )
    
    # Add image
    fig.add_trace(
        go.Image(source=image_src),
        row=1, col=1
    )
    
    # Add info table
    fig.add_trace(
        go.Table(
            header=dict(
                values=["Metric", "Value"],
                fill_color="paleturquoise",
                align="left",
                font=dict(size=14)
            ),
            cells=dict(
                values=[
                    ["CER Before Post Correction (%)", "CER After Post Correction (%)", "Legend"],
                    [
                        f"{df['pre_cer'].iloc[index]*100:.2f}%", 
                        f"{df['post_cer'].iloc[index]*100:.2f}%",
                        "<span style='color:blue'>Blue</span>: Extra | <span style='color:red'>Red</span>: Missing | <span style='color:yellow'>Yellow</span>: Replaced"
                    ]
                ],
                fill_color="lavender",
                align="left",
                font=dict(size=12),
                height=30
            )
        ),
        row=2, col=1
    )
    
    # Add text comparison table
    fig.add_trace(
        go.Table(
            header=dict(
                values=["Type", "Text"],
                fill_color="paleturquoise",
                align="left",
                font=dict(size=14)
            ),
            cells=dict(
                values=[
                    ["OCR Output", "Ground Truth", "Post Corrected", "Ground Truth"],
                    [
                        ocr_text, 
                        gt_text,
                        post_text,
                        gt_text2
                    ]
                ],
                fill_color="lavender",
                align="left",
                font=dict(size=12),
                height=30
            )
        ),
        row=3, col=1
    )
    
    # Layout
    fig.update_layout(
        height=800,
        width=1200,
        title_text=f"Text Comparison - Index: {index}",
        margin=dict(l=20, r=20, t=60, b=20),
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                buttons=[
                    dict(
                        args=[{"title": f"Text Comparison - Index: {max(0, index-1)}"}, 
                              {"source": [get_image_as_base64(df['path'].iloc[max(0, index-1)])]}],
                        label="Previous",
                        method="update"
                    ),
                    dict(
                        args=[{"title": f"Text Comparison - Index: {min(len(df)-1, index+1)}"}, 
                              {"source": [get_image_as_base64(df['path'].iloc[min(len(df)-1, index+1)])]}],
                        label="Next",
                        method="update"
                    ),
                ],
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ]
    )
    
    return fig



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

# Main function to create and save the widget
def create_and_save_widget():
    df = load_data()
    fig = create_text_comparison_widget(df)
    
    # Save the interactive widget as an HTML fragment
    fig.write_html(
        "ocr.html",
        include_plotlyjs=False,
        full_html=False,
        config={
            'displayModeBar': False,
            'responsive': True,
            'scrollZoom': False,
        }
    )
    
    print("Widget saved as ocr.html")
    return fig

# Create and display the widget
fig = create_and_save_widget()
fig.show()  # This will display the figure in Jupyter notebook