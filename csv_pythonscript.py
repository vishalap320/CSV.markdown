import pandas as pd
import os

def convert_excel_to_markdown_files(file_path, output_dir):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Make sure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Iterate through each row and create a markdown file
        for idx, row in df.iterrows():
            raw_text = row['Raw Text']
            filename = f"thought_{idx+1:04d}.md"  # thought_0001.md to thought_1000.md
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(raw_text)

        print(f"Successfully created {len(df)} markdown files in: {output_dir}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    excel_path = "C:\\Users\\Shifu05\\Downloads\\stream_of_thoughts (1).csv"
    output_directory = "C:\\Users\\Shifu05\\Documents\\stream_thoughts.md"
    convert_excel_to_markdown_files(excel_path, output_directory)

    