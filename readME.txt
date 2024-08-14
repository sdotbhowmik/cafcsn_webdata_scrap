1) datafile.xlsx should be empty before run the script.
2) datafile.xlsx must be closed in office program.
3) provide the required credential (email, password) in config.py
4) define the number page available in the system.
5) Run them command as follows

    #run command to get data in console along with excel
    pytest mainBOT\test_bot.py -s --maximize

    #For running operation in headless mode
    pytest mainBOT\phase1.py -s --headless

    pytest mainBOT\phase2.py -s --headless


Phase 1: Code to Collect All IDs
Phase 2: Code to Fetch Details and Update Excel


How It Works:
Phase 1: The script logs in, navigates to the Customers section, and collects all customer IDs, saving them into an Excel file.
Phase 2: The script logs in, reads the IDs from the Excel file, retrieves the customer details for each ID, and updates the Excel file with this information.
This approach allows for greater flexibility and easier troubleshooting

Phase 1: Collect All IDs and Store in Excel
Log in to the system.
Navigate to the Customers section.
Collect all the customer IDs across all pages.
Store these IDs in the first column of an Excel sheet.
Phase 2: Fetch Details for Each ID and Update Excel
Read the Excel sheet to get the list of IDs.
For each ID, navigate to the corresponding details page.
Fetch the required data (e.g., customertype, firstname, etc.) for each ID.
Update the Excel sheet with the fetched data.
