import time
from seleniumbase import BaseCase
from openpyxl import load_workbook
from selenium.webdriver.support.select import Select
from config.config import DataConfig

class FetchDetails(BaseCase):

    def test_fetch_details(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)

        try:
            self.open("https://app.cafcsn.it/#/login")
            self.wait_for_element("//input[@id='email']")
            self.type("//input[@id='email']", DataConfig.Email)
            self.wait_for_element("//input[@id='password']")
            self.type("//input[@id='password']", DataConfig.Password)
            self.click("//button[normalize-space()='Sign in']")
            self.wait_for_element("//a[normalize-space()='Logout']")


            # Load the Excel file with collected IDs
            wb = load_workbook("client_ids.xlsx")
            ws = wb.active

            # Add headers for the details
            ws['B1'] = 'taxid'
            ws['C1'] = 'customertype'
            ws['D1'] = 'firstname'
            ws['E1'] = 'lastname'
            ws['F1'] = 'telephone'
            ws['G1'] = 'mobile'
            ws['H1'] = 'dob'
            ws['I1'] = 'pob'
            ws['J1'] = 'citizenship'
            ws['K1'] = 'street1'
            ws['L1'] = 'street2'
            ws['M1'] = 'city'
            ws['N1'] = 'region'
            ws['O1'] = 'postcode'

            for row in range(2, ws.max_row + 1):
                customerid = ws.cell(row=row, column=1).value
                try:
                    self.open_new_tab()
                    self.get(f"https://app.cafcsn.it/#/pages/customers/edit/{customerid}")
                    time.sleep(2)

                    self.wait_for_element_visible('//button[@class="btn btn-danger float-md-right"]')
                    taxid = self.get_text("//input[@id='taxid']")
                    customertype = Select(self.find_element("//select[@id='customertype']")).first_selected_option.text
                    firstname = self.get_text("//input[@id='firstname']")
                    lastname = self.get_text("//input[@id='lastname']")
                    telephone = self.get_text("//input[@id='telephone']")
                    mobile = self.get_text("//input[@id='mobile']")
                    dob = self.get_text("//input[@id='dob']")
                    pob = self.get_text("//input[@id='pob']")
                    citizenship = self.get_text("//input[@id='citizenship']")
                    street1 = self.get_text("//input[@id='street1']")
                    street2 = self.get_text("//input[@id='street2']")
                    city = self.get_text("//input[@id='city']")
                    region = self.get_text("//input[@id='region']")
                    postcode = self.get_text("//input[@id='postcode']")

                    # Update Excel sheet with details
                    ws.cell(row=row, column=2).value = taxid
                    ws.cell(row=row, column=3).value = customertype
                    ws.cell(row=row, column=4).value = firstname
                    ws.cell(row=row, column=5).value = lastname
                    ws.cell(row=row, column=6).value = telephone
                    ws.cell(row=row, column=7).value = mobile
                    ws.cell(row=row, column=8).value = dob
                    ws.cell(row=row, column=9).value = pob
                    ws.cell(row=row, column=10).value = citizenship
                    ws.cell(row=row, column=11).value = street1
                    ws.cell(row=row, column=12).value = street2
                    ws.cell(row=row, column=13).value = city
                    ws.cell(row=row, column=14).value = region
                    ws.cell(row=row, column=15).value = postcode

                    print(f"Updated details for Client ID: {customerid}")

                except Exception as e:
                    print(f"An error occurred while fetching details for Client ID: {customerid}. Error: {e}")
                finally:
                    self.driver.close()
                    self.switch_to_default_tab()

            # Save the updated Excel file
            wb.save("client_details.xlsx")

        except Exception as e:
            print(f"An error occurred during details fetching: {e}")
            wb.save("client_details.xlsx")
