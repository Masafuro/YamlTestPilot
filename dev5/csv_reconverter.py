import pandas as pd

def convert_csv_to_ysv_no_duplicates(csv_file_path, ysv_file_path):
    """
    Convert a CSV file with hierarchical columns into a YSV file, avoiding duplicate parent entries.

    Args:
    csv_file_path (str): Path to the input CSV file.
    ysv_file_path (str): Path to the output YSV file.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Prepare lines for the YSV content
    ysv_lines = []
    indent_base = "  "  # Define a base indent (2 spaces)
    previous_values = {}  # Track previous row values to avoid duplicates

    # Iterate over each row in the DataFrame
    for _, row in df.iterrows():
        for column in df.columns:
            value = row[column]
            if pd.notna(value):  # Only add non-empty values
                # Determine the level of indentation based on column position
                level = df.columns.get_loc(column)
                indent = indent_base * level

                # Check if the current value is the same as in the previous row for the same column
                if previous_values.get(column) != value:
                    # Format line as "key: value" with appropriate indentation
                    ysv_lines.append(f"{indent}{column}: {value}")

                # Update previous values for this column
                previous_values[column] = value

    # Write the YSV content to the specified file
    with open(ysv_file_path, 'w') as file:
        file.write("\n".join(ysv_lines))
    
    print(f"Conversion complete: {csv_file_path} -> {ysv_file_path}")

def main():
    """Main function to execute CSV to YSV conversion with predefined paths, avoiding duplicate parents."""
    csv_file_path = 'converted_sample.csv'  # Input CSV file path
    ysv_file_path = 'reconstructed_sample.ysv'  # Output YSV file path
    convert_csv_to_ysv_no_duplicates(csv_file_path, ysv_file_path)

# Execute main function if this script is run directly
if __name__ == "__main__":
    main()
