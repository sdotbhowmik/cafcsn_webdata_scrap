Here’s the updated `readME.txt` file with instructions on installing dependencies from the `requirements.txt` file and the necessary SeleniumBase commands:

---

# ReadMe - Customer Data Collection and Processing

## Overview
This project consists of two phases for collecting and processing customer data from a web portal. The phases are implemented in two separate Python scripts using SeleniumBase and OpenPyXL.

### Phase 1: CollectIDs
The `CollectIDs` script navigates through the customer pages on the web portal, collects customer IDs, records the page number from which each ID was collected, and stores this information in `client_ids.xlsx`. A status column is also included with a default value of "Pending."

### Phase 2: FetchDetails
The `FetchDetails` script reads from `client_ids.xlsx`, finds the first unprocessed row, and starts collecting detailed information for each customer ID. It updates `client_details.xlsx` with the collected data and marks the corresponding row in `client_ids.xlsx` as "Processed."

## Files
- **config/config.py:** Contains configuration details such as login credentials and the number of pages to process.
- **phase1.py (CollectIDs):** Collects customer IDs and page numbers, and initializes the status as "Pending."
- **phase2.py (FetchDetails):** Collects customer details, updates `client_details.xlsx`, and marks the corresponding IDs as "Processed" in `client_ids.xlsx`.
- **client_ids.xlsx:** Stores customer IDs, page numbers, and processing status.
- **client_details.xlsx:** Stores detailed information about each customer.
- **requirements.txt:** Lists all Python dependencies required to run the scripts.

## How to Use

### Step 1: Install Dependencies
Before running the scripts, you need to install the required dependencies. Use the following command to install them from the `requirements.txt` file:
```sh
pip install -r requirements.txt
```

### Step 2: Necessary SeleniumBase Commands
SeleniumBase provides specific commands to run and manage test scripts. Here are some key commands you might need:

1. **Run a test script**:
   ```sh
   seleniumbase run path/to/your_script.py
   ```

2. **Run with a specific browser**:
   ```sh
   seleniumbase run path/to/your_script.py --browser=chrome
   ```

3. **Run in headless mode**:
   ```sh
   seleniumbase run path/to/your_script.py --headless
   ```

4. **Install web drivers** (e.g., for Chrome):
   ```sh
   seleniumbase install chromedriver
   ```

### Step 3: Run Phase 1 (CollectIDs)
1. Ensure that your credentials and page number range are correctly configured in `config.py`.
2. Run the `CollectIDs` script using the SeleniumBase command:
   ```sh
   seleniumbase run phase1.py
   ```
3. The script will navigate through the customer pages, collect IDs, and save them in `client_ids.xlsx` with a status of "Pending."

### Step 4: Run Phase 2 (FetchDetails)
1. Ensure that `client_ids.xlsx` has been generated and contains "Pending" IDs.
2. Run the `FetchDetails` script:
   ```sh
   seleniumbase run phase2.py
   ```
3. The script will start from the first unprocessed ID, collect details, update `client_details.xlsx`, and mark the ID as "Processed" in `client_ids.xlsx`.

## Configuration
Update the `config.py` file with your login credentials and the number of pages you want to process:
```python
class DataConfig():
    Email = 'your-email@example.com'
    Password = 'your-password'
    PageNumber = 5  # Number of pages to process
```

## Error Handling
- The scripts include error handling to ensure that the process continues even if a specific customer record fails to process.
- Any errors encountered during the execution will be logged to the console, and the script will move on to the next record.

## Notes
- Ensure that the necessary dependencies are installed from the `requirements.txt` file before running the scripts.
- The scripts are designed to run in a browser environment with Selenium WebDriver.
- Always check and update your browser drivers using SeleniumBase commands to ensure compatibility.

---