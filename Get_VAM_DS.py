# Created By JDB
#import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

class VAMSearch():

  def __init__(self):
    self.sleep_time=5
    self.options_OD=""
    self.options_wt=""
    self.options_GradeOrigin=''
    self.options_Grade=""
    self.options_Connection=""
    self.options_CouplingOption=""
    self.options_Design = ""
    self.options_DrifType=""
    self.options_RBW=""

  def GoToSite(self):

    # Test name: VAM_Search
    # Step # | name | target | value
    # 1 | open | /technical_information/connection_ds_USA.aspx |
    self.driver.get("http://www.vamservices.com/technical_information/connection_ds_USA.aspx")
    # 2 | setWindowSize | 1552x840 |
    self.driver.set_window_size(1552, 840)
    # 3 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD |


    #RBW
    #TEST 26/04 Github

    # Generate DS

    ## 30 | click | id=Div1 |
    #self.driver.find_element(By.ID, "Div1").click()
    ## 31 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS").click()
    ## 32 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS").click()
    ## 33 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine").click()
    ## 34 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine").click()
    ## 35 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ResetCriteria |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ResetCriteria").click()
    ## 36 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD").click()
    ## 37 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD | label=7
    #dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD")
    #dropdown.find_element(By.XPATH, "//option[. = '7']").click()
    ## 38 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD").click()
    ## 39 | click | id=Div1 |
    #self.driver.find_element(By.ID, "Div1").click()
    ## 40 | click | id=Div1 |
    #self.driver.find_element(By.ID, "Div1").click()
    ## 41 | doubleClick | id=Div1 |
    #element = self.driver.find_element(By.ID, "Div1")
    #actions = ActionChains(self.driver)
    #actions.double_click(element).perform()
    ## 42 | click | id=aspnetForm |
    #self.driver.find_element(By.ID, "aspnetForm").click()
    ## 43 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight").click()
    ## 44 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight | label=29.00# /0.408
    #dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight")
    #dropdown.find_element(By.XPATH, "//option[. = '29.00# /0.408']").click()
    ## 45 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight").click()
    ## 46 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_td_GradeOrigine |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_td_GradeOrigine").click()
    ## 47 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine").click()
    ## 48 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine | label=API & Enhanced
    #dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine")
    #dropdown.find_element(By.XPATH, "//option[. = 'API & Enhanced']").click()
    ## 49 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine").click()
    ## 50 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade").click()
    ## 51 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade | label=T95
    #dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade")
    #dropdown.find_element(By.XPATH, "//option[. = 'T95']").click()
    ## 52 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade").click()
    ## 53 | mouseDown | id=blur |
    #element = self.driver.find_element(By.ID, "blur")
    #actions = ActionChains(self.driver)
    #actions.move_to_element(element).click_and_hold().perform()
    ## 54 | mouseUp | css=.vigilant |
    #element = self.driver.find_element(By.CSS_SELECTOR, ".vigilant")
    #actions = ActionChains(self.driver)
    #actions.move_to_element(element).release().perform()
    ## 55 | click | id=ctl00_MainBody |
    #self.driver.find_element(By.ID, "ctl00_MainBody").click()
    ## 56 | click | css=.vigilant |
    #self.driver.find_element(By.CSS_SELECTOR, ".vigilant").click()
    ## 57 | doubleClick | css=.vigilant |
    #element = self.driver.find_element(By.CSS_SELECTOR, ".vigilant")
    #actions = ActionChains(self.driver)
    #actions.double_click(element).perform()
    ## 58 | click | css=#ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Panel_FlagLanguage > div |
    #self.driver.find_element(By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Panel_FlagLanguage > div").click()
    ## 59 | click | css=#ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Panel_FlagLanguage > div |
    #self.driver.find_element(By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Panel_FlagLanguage > div").click()
    ## 60 | doubleClick | css=#ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Panel_FlagLanguage > div |
    #element = self.driver.find_element(By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Panel_FlagLanguage > div")
    #actions = ActionChains(self.driver)
    #actions.double_click(element).perform()
    ## 61 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product").click()
    ## 62 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product | label=VAM® 21
    #dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product")
    #dropdown.find_element(By.XPATH, "//option[. = 'VAM® 21']").click()
    ## 63 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product").click()
    ## 64 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Isolated |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Isolated").click()
    ## 65 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option").click()
    ## 66 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option | label=Regular
    #dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option")
    #dropdown.find_element(By.XPATH, "//option[. = 'Regular']").click()
    ## 67 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option").click()
    ## 68 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType").click()
    ## 69 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType | label=API Drift
    #dropdown = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType")
    #dropdown.find_element(By.XPATH, "//option[. = 'API Drift']").click()
    ## 70 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType").click()
    ## 71 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin").click()
    ## 72 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin").click()
    ## 73 | doubleClick | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin |
    #element = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin")
    #actions = ActionChains(self.driver)
    #actions.double_click(element).perform()
    ## 74 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS").click()
    ## 75 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_OD_value_imp |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_OD_value_imp").click()
    ## 76 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_OD_value_imp |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_OD_value_imp").click()
    ## 77 | doubleClick | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_OD_value_imp |
    #element = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_OD_value_imp")
    #actions = ActionChains(self.driver)
    #actions.double_click(element).perform()
    ## 78 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_ID_value_imp |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_ID_value_imp").click()
    ## 79 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_ID_value_imp |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_ID_value_imp").click()
    ## 80 | doubleClick | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_ID_value_imp |
    #element = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_ID_value_imp")
    #actions = ActionChains(self.driver)
    #actions.double_click(element).perform()
    ## 81 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_CS_value_imp |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_CS_value_imp").click()
    ## 82 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_CS_value_imp |
    #self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_CS_value_imp").click()
    ## 83 | doubleClick | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_CS_value_imp |
    #element = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_PIPENominal_CS_value_imp")
    #actions = ActionChains(self.driver)
    #actions.double_click(element).perform()
    ## 84 | click | css=.marketing_message |
    #self.driver.find_element(By.CSS_SELECTOR, ".marketing_message").click()

  def GenerateDS(self):
    # 29 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS |
    self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS").click()
    sleep(10)

  def ClearFilter(self):
    # 29 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS |
    self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ResetCriteria").click()
    sleep(self.sleep_time)

  def setup_method(self, method):
    driver_path=r"C:\Users\Usuario\Downloads\chromedriver_win32 (80)\chromedriver.exe"
    self.driver = webdriver.Chrome(driver_path)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def Selection_OD(self,**kwargs):
      Selection=kwargs.get('Selection', None)
      self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD").click()
      # 4 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD | label=7
      dropdown_OD = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD")
      if Selection is None:
        self.options_OD = dropdown_OD.text.split('\n')
      else:
        Selection=Selection.strip()
        dropdown_OD.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
        #print(Selection)
        sleep(self.sleep_time)

  def Selection_wt(self,**kwargs):
    # 6 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight |
    self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight").click()
    # 7 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight | label=29.00# /0.408
    dropdown_wt = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight")

    Selection = kwargs.get('Selection', None)

    if Selection is None:
      self.options_wt=dropdown_wt.text.split('\n')
    else:
      Selection = Selection.strip()
      dropdown_wt.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
      sleep(self.sleep_time)

    #print('********** Wall Thicknesss***************')

  def Selection_GradeOrigin(self,**kwargs):
    # 9 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine |
    self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine").click()
    # 10 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine | label=API & Enhanced
    dropdown_origin = self.driver.find_element(By.ID,
                                               "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine")

    Selection=kwargs.get('Selection', None)
    if Selection is None:
      self.options_GradeOrigin = dropdown_origin.text.split('\n')

    else:
      Selection=Selection.strip()

      dropdown_origin.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
      sleep(self.sleep_time)
    # 11 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine |
    #print('********** Grade Origin***************')

  def Selection_Grade(self,**kwargs):
    # 12 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade |
    self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade").click()
    # 13 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade | label=P110
    dropdown_grade = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade")

    Selection = kwargs.get('Selection', None)

    if Selection is None:
      self.options_Grade = dropdown_grade.text.split('\n')

    else:
      Selection=Selection.strip()
      dropdown_grade.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
      sleep(self.sleep_time)
    # 14 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade |
    #print('********** Grade ***************')

  def Selection_Connection(self,**kwargs):
    # 15 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product |
    self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product").click()
    # 16 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product | label=VAM® 21
    dropdown_Connection = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product")

    Selection=kwargs.get('Selection', None)

    if Selection is None:
      self.options_Connection = dropdown_Connection.text.split('\n')

    else:
      dropdown_Connection.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
      sleep(self.sleep_time)

  def Selection_Design(self,**kwargs):
    self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Isolated").click()
    dropdown_Design=self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Isolated")

    Selection = kwargs.get('Selection', None)

    if Selection is None:
      self.options_Design = dropdown_Design.text.split('\n')

    else:
      dropdown_Design.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
      sleep(self.sleep_time)

    #print('********** Connection ***************')

  def Selection_CouplingOption(self,**kwargs): #Coupling Option
      # 20 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option |
      self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option").click()
      # 21 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option | label=SC80
      dropdown_CouplingOption = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option")
      Selection = kwargs.get('Selection', None)
      if Selection is None:
        self.options_CouplingOption = dropdown_CouplingOption.text.split('\n')

      else:
        dropdown_CouplingOption.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
        sleep(self.sleep_time)
      #print('********** CouplingOption ***************')

  def Selection_DriftType(self,**kwargs):
      # 23 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType |
      self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType").click()
      # 24 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType | label=Special Drift
      dropdown_DriftType = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType")

      Selection = kwargs.get('Selection', None)

      if Selection is None:
        self.options_DrifType = dropdown_DriftType.text.split('\n')

      else:
        dropdown_DriftType.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
        sleep(self.sleep_time)
      #print('********** Drift Type ***************')

  def Selection_RBW(self,**kwargs):
      # 26 | click | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin |
      self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin").click()
      # 27 | select | id=ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin | label=90.0%
      dropdown_RBW = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin")

      Selection=kwargs.get('Selection',None)

      if Selection is None:
        self.options_RBW = dropdown_RBW.text.split('\n')
      else:
        dropdown_RBW.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
        sleep(self.sleep_time)
      #print('********** RBW ***************')

Navegador=VAMSearch()
Navegador.setup_method('')
Navegador.GoToSite()
Navegador.Selection_Connection()
list_Connection=Navegador.options_Connection

for connection in list_Connection:
  if not connection.find('Select')>0:
    Navegador.Selection_Connection(Selection=connection)
    print('********* Connection *********')
    print(connection)
    Navegador.Selection_OD()
    list_OD=Navegador.options_OD
    print('///////////')
    for od in list_OD:
      if not od.find('Select')>0:
        print('********* OD *********')
        print(od)
        Navegador.Selection_OD(Selection=od)
        Navegador.Selection_wt()
        print('********* wt *********')
        list_wt=Navegador.options_wt
        print(list_wt)
        for wt in list_wt:
          if not wt.find('Select')>0:
            print('**** wt ****')
            print(wt)
            Navegador.Selection_wt(Selection=wt)
            Navegador.Selection_GradeOrigin()
            list_GradeOrigin=Navegador.options_GradeOrigin
            for GradeOrigin in list_GradeOrigin:
              if not GradeOrigin.find('Select')>0:
                Navegador.Selection_GradeOrigin(Selection=GradeOrigin)
                Navegador.Selection_Grade()
                list_Grade=Navegador.options_Grade
                for Grade in list_Grade:
                  if not Grade.find('Select')>0:
                    print(Grade)
                    Navegador.Selection_Grade(Selection=Grade)
                    Navegador.Selection_Design()
                    list_Design=Navegador.options_Design
                    for Design in list_Design:
                      if not Design.find('Select')>0:
                        print(Design)
                        Navegador.Selection_Design(Selection=Design)
                        Navegador.Selection_CouplingOption()
                        list_CouplingOption=Navegador.options_CouplingOption
                        for CouplingOption in list_CouplingOption:
                          if not CouplingOption.find('Select')>0:
                            print(CouplingOption)
                            Navegador.Selection_CouplingOption(Selection=CouplingOption)
                            Navegador.Selection_DriftType(Selection='API Drift')
                            Navegador.Selection_DriftType(Selection='87.5%')
                            Navegador.GenerateDS()
                            titulo=Navegador.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Panel_TableHeaderCDS")
                            PipeProperties=Navegador.driver.find_element(By.ID,"Tbl_PIPE_Properties")
                            ConnectionProperties=Navegador.driver.find_element(By.ID,"Tbl_CONNECTION_Properties")
                            ConnectionPerformance=Navegador.driver.find_element(By.CLASS_NAME,"tableau_loading_performances")
                            ConnectionTorques = Navegador.driver.find_element(By.ID, "Tbl_torques")
                            print('**** Titulo ***\n',titulo.text,'\n')
                            print('**** PipeProperties ***\n', PipeProperties.text,'\n')
                            print('**** ConnectionProperties ***\n', ConnectionProperties.text,'\n')
                            print('**** ConnectionPerformance ***\n', ConnectionPerformance.text,'\n')
                            print('**** ConnectionTorques ***\n', ConnectionTorques.text,'\n')


      print('///////////')

  Navegador.ClearFilter()
