# Created By JDB
# Objetivo -> Extraer información del sitio http://www.vamservices.com/technical_information/connection_ds_USA.aspx

if True:
    import time
    import json
    import pandas as pd
    import smtplib
    import functools
    import os
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
    from selenium.webdriver.support.ui import Select
    from time import sleep


def NoSuchElement(func):
    num_retries = 5
    @functools.wraps(func)
    def wrapper(*a, **kw):
        for i in range(num_retries):
            if i ==4:
                Notify_gmail()
                break
            try:
                return func(*a, **kw)
            except NoSuchElementException:
                sleep(2)
                print(i)
                print('re-try')
                Notify_gmail()
                return func(*a, **kw)

            except ElementClickInterceptedException:
                print(ElementClickInterceptedException)
                Notify_gmail()

    return wrapper


class VAMSearch():

    def __init__(self):
        self.sleep_time = 2
        self.options_OD = ""
        self.options_wt = ""
        self.options_GradeOrigin = ''
        self.options_Grade = ""
        self.options_Connection = ""
        self.options_CouplingOption = ""
        self.options_Design = ""
        self.options_DriftType = ""
        self.options_RBW = ""

    def setup_method(self, method):
        driver_path=r"C:\Users\Usuario\Downloads\chromedriver_win32 (80)\chromedriver.exe"
        option = webdriver.ChromeOptions()
        chrome_prefs = dict()
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        self.driver = webdriver.Chrome(driver_path,chrome_options=option)
        self.vars = {}

    def GoToSite(self):
        self.driver.get("http://www.vamservices.com/technical_information/connection_ds_USA.aspx")
        self.driver.set_window_size(1552, 840)

    def wait_load(self):
        wait = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_UpdateProgress1")
        
        if wait.get_attribute('style').find('hidden')>0:
            sleep(0.75)
            
        else:
            while wait.get_attribute('style').find('hidden')<0:
                wait = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_UpdateProgress1")
                sleep(1.25)

    @NoSuchElement
    def GenerateDS(self):
        self.wait_load()
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ViewCDS").click()
        self.wait_load()
        sleep(0.25)

    @NoSuchElement
    def ClearFilter(self):
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Bt_ResetCriteria").click()
        self.wait_load()

    @NoSuchElement
    def teardown_method(self, method):
        self.driver.quit()

    @NoSuchElement
    def Selection_OD(self,**kwargs):
        self.wait_load()
        dropdown_OD = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_OD")
        Selection = kwargs.get('Selection', None)
        if Selection is None:
            self.options_OD = dropdown_OD.text.split('\n')
        else:
            Selection=Selection.strip()
            dropdown_OD.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
            
            self.wait_load()

    @NoSuchElement
    def Selection_wt(self,**kwargs):
        self.wait_load()
        dropdown_wt = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Wall_Weight")
        Selection = kwargs.get('Selection', None)
        
        if Selection is None:
            self.options_wt = dropdown_wt.text.split('\n')
        
        else:
            Selection = Selection.strip()
            dropdown_wt.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
            self.wait_load()

    @NoSuchElement
    def Selection_GradeOrigin(self,**kwargs):
        self.wait_load()
        dropdown_origin = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_GradeOrigine")
        Selection = kwargs.get('Selection', None)
        
        if Selection is None:
            self.options_GradeOrigin = dropdown_origin.text.split('\n')

        else:
            Selection=Selection.strip()
            dropdown_origin.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
            self.wait_load()

    @NoSuchElement
    def Selection_Grade(self,**kwargs):
        self.wait_load()
        dropdown_grade = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Grade")

        Selection = kwargs.get('Selection', None)

        if Selection is None:
            self.options_Grade = dropdown_grade.text.split('\n')

        else:
            Selection=Selection.strip()
            dropdown_grade.find_element(By.XPATH, "//option[. = '{}']".format(Selection)).click()
            self.wait_load()

    @NoSuchElement
    def Selection_Connection(self,**kwargs):
        self.wait_load()                 
        dropdown_Connection = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product")
        Selection = kwargs.get('Selection', None)

        if Selection is None:
            self.options_Connection = dropdown_Connection.text.split('\n')

        else:
            dropdown_Connection.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
            self.wait_load()

    @NoSuchElement
    def Selection_Design(self,**kwargs):
        self.wait_load()
        dropdown_Design=self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Isolated")
        Selection = kwargs.get('Selection', None)

        if Selection is None:
            self.options_Design = dropdown_Design.text.split('\n')

        else:
            dropdown_Design.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
            self.wait_load()

    @NoSuchElement
    def Selection_CouplingOption(self,**kwargs): 
        self.wait_load()
        dropdown_CouplingOption = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Option")
        Selection = kwargs.get('Selection', None)
        
        if Selection is None:
            self.options_CouplingOption = dropdown_CouplingOption.text.split('\n')

        else:
            select=Select(dropdown_CouplingOption)
            select.select_by_visible_text(Selection.strip())
            self.wait_load()

    @NoSuchElement
    def Selection_DriftType(self,**kwargs):
        self.wait_load()
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType").click()
        dropdown_DriftType = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_DriftType")
        Selection = kwargs.get('Selection', None)

        if Selection is None:
            self.options_DriftType = dropdown_DriftType.text.split('\n')

        else:
            dropdown_DriftType.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
            self.wait_load()

    @NoSuchElement
    def Selection_RBW(self,**kwargs):
        self.wait_load()
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin").click()
        dropdown_RBW = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_WallThicknessMin")
        Selection=kwargs.get('Selection',None)

        if Selection is None:
            self.options_RBW = dropdown_RBW.text.split('\n')
        else:
            dropdown_RBW.find_element(By.XPATH, "//option[. = '{}']".format(Selection.strip())).click()
            self.wait_load()

    @NoSuchElement
    def DataFrameToRow(self, df):
        df = pd.DataFrame(df.values, columns=['FieldName', 'USC_Value', 'USC_Unit', 'SI_Value', 'SI_Unit'])
        df_output = dict()
        for index in df.index:
            FieldName = df.iloc[index].FieldName
            df_output[FieldName + '_USC'] = df.iloc[index].USC_Value
            df_output[FieldName + '_USC_UOM'] = df.iloc[index].USC_Unit
            df_output[FieldName + '_SI'] = df.iloc[index].SI_Value
            df_output[FieldName + '_SI_UOM'] = df.iloc[index].SI_Unit

        return pd.DataFrame(df_output, index=[0])

    @NoSuchElement
    def GetInfoFromNavegador(self):
        self.wait_load()
        titulo = self.driver.find_element(By.ID,
                                               "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Panel_TableHeaderCDS")
        PipeProperties = self.driver.find_element(By.ID, "Tbl_PIPE_Properties")
        ConnectionProperties = self.driver.find_element(By.ID, "Tbl_CONNECTION_Properties")
        ConnectionPerformance = self.driver.find_element(By.CLASS_NAME, "tableau_loading_performances")
        ConnectionTorques = self.driver.find_element(By.ID, "Tbl_torques")
        ConnectionReferenceVME = self.driver.find_element(By.ID,
                                                               "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Img_Marketing")
        FootNotes = self.driver.find_element(By.ID,
                                                  "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_DataList_CDS_ctl00_Lbl_Marketing")

        row_data = pd.DataFrame()

        for var in [PipeProperties, ConnectionProperties, ConnectionPerformance, ConnectionTorques]:
            read_html = pd.read_html(var.get_attribute('outerHTML'))[0]
            row_data = row_data.append(self.DataFrameToRow(pd.DataFrame(read_html)).T, ignore_index=False)
        row_data = row_data.T
        row_data['FootNote'] = FootNotes.get_attribute('innerText')
        row_data['VME_source'] = ConnectionReferenceVME.get_attribute('src')
        row_data['Title'] = titulo.get_attribute('innerText')

        return row_data

# FileNotFoundError: [Errno 2] No such file or directory: 're_start.json'

def FileNotFound(func):
    num_retries = 5
    @functools.wraps(func)
    def wrapper(*a, **kw):
        sleep_interval = 2
        for i in range(num_retries):
            try:
                return func(*a, **kw)
            except FileNotFoundError as ex:
                new_loc=input('Ingrese la ubicación del archivo json')
                new_loc=new_loc.replace('"','')
                return func(self=a[0],file_loc=new_loc,**kw)

    return wrapper


class re_start_class:

    def __init__(self, **kwargs):

        file_loc = kwargs.get('file_loc', None)

        if file_loc is None:
            self.load('re_start.json')
        else:
            self.load(file_loc)

    @FileNotFound
    def load(self, file_loc):
        with open(file_loc, 'r') as fp:
            self.data = json.load(fp)
            
    def save(self):
        with open(r're_start.json', 'w') as fp:
            json.dump(self.data, fp, indent=4)

    def update_data(self,Connection_, OD_, wt_, GradeOrigin_, Grade_):

        if Connection_ != re_start.data['Last_Connection']:
            re_start.data['Loaded_Connection'].append(re_start.data['Last_Connection'])
            re_start.data['Last_Connection'] = Connection_

        if OD_ != re_start.data['Last_OD']:
            re_start.data['Loaded_OD'].append(re_start.data['Last_OD'])
            re_start.data['Last_OD'] = OD_

        if wt_ != re_start.data['Last_wt']:
            re_start.data['Loaded_wt'].append(re_start.data['Last_wt'])
            re_start.data['Last_wt'] = wt_

        if GradeOrigin != re_start.data['Last_GradeOrigin']:
            if GradeOrigin_ != '':
                re_start.data['Loaded_GradeOrigin'].append(re_start.data['Last_GradeOrigin'])
                re_start.data['Last_GradeOrigin'] = GradeOrigin_
                if len(re_start.data['Loaded_Grade'])==3:
                    re_start.data['Loaded_Grade']=[]

        if Grade_ != re_start.data['Last_Grade']:
            re_start.data['Loaded_Grade'].append(re_start.data['Last_Grade'])
            re_start.data['Last_Grade'] = Grade_


def RemoveSelect(list_option):
    for option in list_option:
        if option.find('Select')>0:
            list_option.remove(option)
    return list_option


def Notify_gmail():

    gmail_user = 'background.job.python@gmail.com'
    gmail_password = 'mqinbmnvargppnat'

    sent_from = gmail_user
    to = ['joelduin@gmail.com']
    subject = 'VAM - Information'
    body = 'Se ha finalizado con error'

    email_text = """\
    From: {}
    To: {}
    Subject: {}

    {}
    """.format (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

    except:
        print('Error')

curr_dir=os.path.dirname(os.path.realpath(__file__))
os.chdir(curr_dir)
last_dir=max([int(x) for x in os.listdir() if os.path.isdir(x)])
os.chdir(str(last_dir))
re_start=re_start_class()
os.chdir(curr_dir)
os.mkdir(str(last_dir+1))
os.chdir(str(last_dir+1))


Navegador=VAMSearch()
Navegador.setup_method('')
Navegador.GoToSite()
Navegador.Selection_Connection()
list_Connection=RemoveSelect(Navegador.options_Connection)
VAM_data=pd.DataFrame()
n=0


# Pick from last Loaded

if True:
    Last_Connection = re_start.data['Last_Connection']
    Loaded_OD = re_start.data['Loaded_OD']
    Last_OD = re_start.data['Last_OD']
    Loaded_wt = re_start.data['Loaded_wt']
    Last_wt = re_start.data['Last_wt']
    Loaded_GradeOrigin = re_start.data['Loaded_GradeOrigin']
    Loaded_Grade = re_start.data['Loaded_Grade']

for Connection in list_Connection:

    Navegador.Selection_Connection(Selection = Connection); Navegador.Selection_OD()
    list_OD = RemoveSelect(Navegador.options_OD)

    if Connection==Last_Connection:
        list_OD = [x for x in list_OD if x not in Loaded_OD]

    for OD in list_OD:

        Navegador.Selection_OD(Selection=OD)

        # Aclaratoria: Estas tres lineas las dejé pues me di cuenta que cuando pasaba
        # del 6" al 6 5/8", al seleccionar 6 5/8" se des-seleccionaba la conexión
        # Generando errores. Me parece que es un tema de VAM

        selected_conn = Select(Navegador.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_Uc_datasheet_view_new1_Criteria_Product"))
        if selected_conn.first_selected_option.text == 'Select':
            Navegador.Selection_Connection(Selection=Connection)

        Navegador.Selection_wt()
        list_wt = RemoveSelect(Navegador.options_wt)

        if Connection ==  Last_Connection and OD == Last_OD:
            list_wt = [x for x in list_wt if x not in Loaded_wt]

        for wt in list_wt:
            Navegador.Selection_wt(Selection=wt); Navegador.Selection_GradeOrigin()
            list_GradeOrigin = RemoveSelect(Navegador.options_GradeOrigin)

            if (Connection ==  Last_Connection) and (OD == Last_OD) and (wt==Last_wt):
                list_GradeOrigin=[x for x in list_GradeOrigin if x not in Loaded_GradeOrigin]

            for GradeOrigin in list_GradeOrigin:
                Navegador.Selection_GradeOrigin(Selection=GradeOrigin); Navegador.Selection_Grade()
                list_Grade = RemoveSelect(Navegador.options_Grade)

                if (Connection == Last_Connection) and (OD ==Last_OD) and (wt == Last_wt):
                    list_Grade = [x for x in list_Grade if x not in Loaded_Grade]

                for Grade in list_Grade:
                    Navegador.Selection_Grade(Selection=Grade) ; Navegador.Selection_Design()
                    list_Design = RemoveSelect(Navegador.options_Design)

                    for Design in list_Design:
                        Navegador.Selection_Design(Selection=Design) ; Navegador.Selection_CouplingOption()
                        list_CouplingOption = RemoveSelect(Navegador.options_CouplingOption)

                        for CouplingOption in list_CouplingOption:

                            Navegador.Selection_CouplingOption(Selection=CouplingOption)
                            Navegador.Selection_DriftType()
                            list_drift=RemoveSelect(Navegador.options_DriftType)
                            Navegador.Selection_DriftType(Selection=list_drift[0])

                            Navegador.Selection_RBW()
                            list_RBW=RemoveSelect(Navegador.options_RBW)
                            Navegador.Selection_RBW(Selection=list_RBW[0])

                            print(n)
                            print('Connection      ->', Connection.strip())
                            print('OD              ->', OD.strip())
                            print('wt              ->', wt.strip())
                            print('GradeOrigin     ->', GradeOrigin.strip())
                            print('Grade           ->', Grade.strip())
                            print('Design          ->', Design.strip())
                            print('Coupling Option ->', CouplingOption.strip())
                            print('Drift           ->', list_drift[0].strip())
                            print('RBW             ->', list_RBW[0].strip(),'\n')

                            Navegador.GenerateDS()

                            row_data=Navegador.GetInfoFromNavegador()

                            row_data['Custom_Connection'] = Connection
                            row_data['Custom_OD'] = OD
                            row_data['Custom_wt'] = wt
                            row_data['Custom_GradeOrigin'] = GradeOrigin
                            row_data['Custom_Grade'] = Grade
                            row_data['Custom_Design'] = Design
                            row_data['Custom_CouplingOption'] = CouplingOption
                            row_data['Custom_DriftType'] = list_drift[0]
                            row_data['Custom_RBW'] = list_RBW[0]

                            VAM_data = VAM_data.append(row_data)
                            re_start.update_data(Connection, OD, wt, GradeOrigin, Grade)
                            n+=1

                            if n%10 == 0:
                                VAM_data.to_excel('VAM_DATA_{}.xlsx'.format(n))
                                re_start.save()

                    Navegador.ClearFilter() ; Navegador.Selection_Connection(Selection=Connection);  Navegador.Selection_OD(Selection=OD); Navegador.Selection_wt(Selection=wt);Navegador.Selection_GradeOrigin(Selection=GradeOrigin)

            Navegador.ClearFilter(); Navegador.Selection_Connection(Selection=Connection);  Navegador.Selection_OD(Selection=OD); Navegador.Selection_wt(Selection=wt)

        Navegador.ClearFilter(); Navegador.Selection_Connection(Selection=Connection)

    Navegador.ClearFilter(); Navegador.Selection_Connection(Selection=Connection)
