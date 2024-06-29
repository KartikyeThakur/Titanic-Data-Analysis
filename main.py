import pandas as pd
from pandas_profiling import ProfileReport


def load_data(file_path):
    """
    Load the dataset from the given file path.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)


def display_dataframe(df, title="DataFrame"):
    """
    Display the first few rows of the DataFrame with a title.

    Parameters:
    df (DataFrame): The DataFrame to display.
    title (str): The title for the DataFrame display.
    """
    print(f"\n{title}:")
    print(df.head())


def clean_data(df):
    """
    Identify and clean missing values in the DataFrame.

    Parameters:
    df (DataFrame): The original DataFrame with potential missing values.

    Returns:
    DataFrame, Series: Cleaned DataFrame and a Series with the count of missing values per column.
    """
    # Identify missing values
    missing_values_count = df.isnull().sum()
    print("\nMissing Values in Each Column:")
    print(missing_values_count)

    # Replace missing values with a placeholder
    df_cleaned = df.fillna("Not Available")

    return df_cleaned, missing_values_count


def generate_profile_report(df, report_title, output_file):
    """
    Generate and save a profile report for the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to profile.
    report_title (str): Title for the profile report.
    output_file (str): The file path to save the report.
    """
    profile = ProfileReport(df, title=report_title, explorative=True)
    profile.to_file(output_file=output_file)


def save_missing_values_summary(missing_values_count, output_file):
    """
    Save the summary of missing values to a text file.

    Parameters:
    missing_values_count (Series): Series with the count of missing values per column.
    output_file (str): The file path to save the summary.
    """
    with open(output_file, "w") as file:
        file.write("Missing Values in Each Column:\n")
        file.write(missing_values_count.to_string())
    print(f"\nMissing values summary saved to '{output_file}'")


def main():
    # Load the dataset
    file_path = '/content/titanic.csv'  # Update this path to the location of your CSV file
    df = load_data(file_path)

    # Display the original dataframe
    display_dataframe(df, title="Original DataFrame")

    # Clean the data
    df_cleaned, missing_values_count = clean_data(df)

    # Display the cleaned dataframe
    display_dataframe(df_cleaned, title="Cleaned DataFrame")

    # Generate the profile report using the cleaned data
    generate_profile_report(df_cleaned, "Titanic Dataset Profile Report", "titanic.html")

    # Save the summary of missing values
    save_missing_values_summary(missing_values_count, "missing_values_summary.txt")


if __name__ == "__main__":
    main()