"""
This script reads an Excel file, generates a profiling report using ydata_profiling, 
and saves the report as an HTML file.

Modules:
    pandas as pd: Used for data manipulation and analysis.
    ydata_profiling: Generates profile reports from a pandas DataFrame.

Functions:
    None

Usage:
    1. Ensure the Excel file "listado_activos.xlsx" is located in the root directory of the script.
    2. Run the script. It will generate an HTML profiling report of the data in the Excel file.

Workflow:
    1. Import the required modules.
    2. Load the data from the Excel file "listado_activos.xlsx" into a pandas DataFrame.
    3. Create a ProfileReport object with the DataFrame, setting the title to "Scan Inicial listado_activos" 
       and disabling interactions and correlations.
    4. Save the profiling report as an HTML file named "reporte_listado_activos.html".
    5. Print a message indicating that the process has finished.

Example:
    $ python profiling_report.py

    This will generate an HTML file "reporte_listado_activos.html" containing the profiling report of the data.

Notes:
    - Ensure the ydata_profiling package is installed. You can install it via pip:
      $ pip install ydata-profiling
    - The script assumes the Excel file "listado_activos.xlsx" is in the same directory as the script. 
      Modify the file path if it is located elsewhere.
"""
import pandas as pd
from ydata_profiling import ProfileReport

# Load data from Excel file into a pandas DataFrame
df = pd.read_excel("/listado_activos.xlsx")

# Create a profile report of the DataFrame
profile = ProfileReport(df, title="Scan Inicial {0}".format("listado_activos"), interactions=None, correlations=None)

# Save the profile report as an HTML file
profile.to_file("reporte_{0}.html".format("listado_activos"))

# Print a message indicating the process is finished
print("Process finished.")
