import csv
import pandas as pd

# I'll reintroduce the main function to wrap the execution in a standard format.

def convert_ysv_to_csv_direct(ysv_file_path, csv_file_path):
    """
    Convert a YSV (YAML-like structured with spaces for hierarchy) file to a CSV file.
    The CSV will be flattened with columns representing hierarchical paths.

    Args:
    ysv_file_path (str): Path to the input YSV file.
    csv_file_path (str): Path to the output CSV file.
    """
    # Read YSV file
    with open(ysv_file_path, 'r') as file:
        data = file.read()

    # Process YSV to CSV format in a structured DataFrame
    def ysv_to_structured_csv(data):
        """Convert ysv data to a structured DataFrame for CSV output."""
        rows = []
        current_path = []
        prev_indent = 0

        for line in data.strip().splitlines():
            # Determine indentation based on leading spaces
            indent = len(line) - len(line.lstrip())
            line = line.strip()
            key, value = [item.strip() for item in line.split(":", 1)]
            value = value.strip('"')  # Remove any surrounding quotes from value

            # Adjust the path based on indentation level
            if indent > prev_indent:
                current_path.append(key)  # Going deeper, add key to path
            elif indent < prev_indent:
                level_difference = (prev_indent - indent) // 2  # Assuming 2-space indentation per level
                current_path = current_path[:-(level_difference + 1)]
                current_path.append(key)  # Replace current key in path
            else:
                if current_path:
                    current_path.pop()  # Remove the last key if on the same level
                current_path.append(key)

            # Populate row data with the full path as headers
            row_data = {path: "" for path in ["api_keys", "service_name", "key", "active"]}  # Reset for new row format
            for i, path_key in enumerate(current_path):
                row_data[path_key] = value if i == len(current_path) - 1 else ""

            # Append the row to the rows list
            rows.append(row_data.copy())

            # Update previous indentation
            prev_indent = indent

        # Create a DataFrame from the rows list
        df = pd.DataFrame(rows).fillna("")
        return df

    # Convert to DataFrame and clean up to CSV format
    df = ysv_to_structured_csv(data)
    df = df.replace("", pd.NA).apply(lambda x: x.dropna().reset_index(drop=True))  # Shift up non-empty values
    df = df.ffill()  # Fill in remaining NaNs with last valid value

    # Save to CSV
    df.to_csv(csv_file_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
    print(f"Conversion complete: {ysv_file_path} -> {csv_file_path}")

def main():
    """Main function to execute YSV to CSV conversion with predefined paths."""
    ysv_file_path = 'sample.ysv'  # Input YSV file path
    csv_file_path = 'converted_sample.csv'  # Output CSV file path
    convert_ysv_to_csv_direct(ysv_file_path, csv_file_path)

# Execute main function if this script is run directly
if __name__ == "__main__":
    main()
