import time
from seleniumbase import BaseCase
from openpyxl import Workbook
from config.config import DataConfig

wb = Workbook()


class CollectIDs(BaseCase):

    def test_collect_ids(self):
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

            # Go to customers
            self.wait_for_element("//a[normalize-space()='Customers']")
            self.click("//a[normalize-space()='Customers']")
            self.wait_for_element("(//td)[1]")

            # Excel operation
            ws = wb.active
            ws['A1'] = 'customerid'  # Header for IDs

            pagination_no = DataConfig.PageNumber
            counter = 1

            for p in range(1, pagination_no + 1):
                self.click("//a[normalize-space()='%s']" % str(p))
                time.sleep(1)

                for i in range(1, 21):
                    try:
                        list_element = self.get_text("//tbody/tr[%s]/td[1]" % str(i))
                        ws.append([list_element])
                        counter += 1
                        print(f"Collected Client ID: {list_element}")
                    except Exception as e:
                        print(f"An error occurred while collecting ID on page {p}, row {i}: {e}")

            # Save IDs to the Excel file
            wb.save("client_ids.xlsx")
            print("Phase1: Completed, client_ids.xlsx updated correctly")
            print("Now you need to run phase2.py")


        except Exception as e:
            print(f"An error occurred during ID collection: {e}")
            wb.save("client_ids.xlsx")
