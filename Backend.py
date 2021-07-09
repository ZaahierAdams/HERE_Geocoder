'''

Author: Zaahier Adams
https://github.com/ZaahierAdams


Backend script for Curate
(1) Reads input file in pandas DF
(2) Scrubs addresses
(3) Parses addresses through HERE geocoding rest API
(4) Saves results to output file


First released: 07/06/2020
last updated:   07/06/2020

'''

from pandas import read_excel as pd_read_excel
from pandas import isna as pd_isna
from csv import writer as csv_writer
from re import sub as re_sub
from requests import get as requests_get
import time 
from xlrd import XLRDError
from difflib import SequenceMatcher


## Global variables
sheet_name  = 'curation_list'
file_ext    = '.xlsx'  
index_col   = 'RowID'
header_row  = 0
address_col = 'full_address'
PostCodeCol = 'postal_code'
CuratorCol  = 'curator_name/ID'

#API_key     = 'YybJWFlIGtKay67fsS3UULmQ5HzO0pCfRp73rmzahdY'

line_len    = 70

def main(API_key, input_file): 
#    input_file  = 'test_addresses'
    output_file = 'OUTPUT_'+input_file.replace(file_ext,'')+'.csv'
    NaN = ['nan', 'null', 'none', 'na', 'missing', '0']
    
    if file_ext in input_file:
        pass
    else:
        input_file = input_file + file_ext
    try:
        df = pd_read_excel(io = input_file, sheet_name = sheet_name,  index_col = index_col, header = header_row) # names = XXX, 
        shape_filter = df.shape
        
        file_line = 0
        try:
            with open(output_file, mode='w') as output:
                writer = csv_writer(output, delimiter=',', lineterminator = '\n')
                if file_line == 0:
                    writer.writerow([index_col,                                               
                                     address_col,                  
                                     PostCodeCol,       
                                     '',
                                     'QueryScore',                    
                                     'HouseNumber_Match',        
                                     'PostalCode_Match',
                                     '', 
                                     'Output_Address',       
                                     'Output_PostalCode',                  
                                     '',
                                     '',
                                     'Suburb',
                                     '',
                                     '',
                                     'Latitude',
                                     'Longitude'
                                     ])
                else:
                    pass
                
                validated   = 0
                failed      = 0 
                AccumQS     = 0 # Acculmulated Query Scores
                for index, row in df.iterrows():
                    try:
                        input_address = df.loc[index, address_col]
                        input_address0= input_address
#                        print('Checking:\t'+input_address0)
                        if pd_isna(input_address) is True or str(input_address).lower() in NaN: 
                            input_address = str(input_address)
                    except KeyError:
                        print('Input Address column is not found!\nEnsure that there is a column \"'+address_col+'\"')
                        break
                    try:
                        input_PostCode = df.loc[index, PostCodeCol]
                        input_PostCode0= input_PostCode
                    except KeyError:
                        print('Input Postal Code column is not found!\nEnsure that there is a column \"'+PostCodeCol+'\"')
                        break  
                    
                    input_address = Afrikaans_to_English(input_address)
                    input_address = SpecialChar_Remover(input_address)
                    street, Extract_PostCode, address_elem = Separate_Address(input_address)
                    
                    ## If PostCode col. is Null
                    if pd_isna(input_PostCode) is True or str(input_PostCode).lower() in NaN: 
                        ## If Address has PostCode
                        if Extract_PostCode is not None:
                            input_PostCode = Extract_PostCode
                        else:
                            input_PostCode = None
                    else:
                        pass 
                
                    F_address, F_suburb, F_postalCode, QueryScore, fs_HouseNo, fs_PostCode, validated, failed, AccumQS, Latitude, Longitude = Geocoder(street, input_PostCode, address_elem, input_file, file_ext, validated, failed, AccumQS, API_key)
                    
                    if F_address is False:
                        break
                    else:
                        pass
#                        print('_'*line_len)
#                        if F_address is None:
#                            print('Input Address:\t\t'      + input_address   + ', '  + str(input_PostCode)    )
#                            print()
#                            print('Could not validate'                                                          )
#                        else:
#                            print('Input Address:\t\t'      + input_address   + ', '  + str(input_PostCode)    )
#                            print('Output Address:\t\t'     + F_address       + ', '  + str(F_postalCode)      )
#                            print()
#                            print('Latitude, Longitude:\t'  + str(Latitude)   + ', '  + str(Longitude)         )
#                            print()
#                            print('Query Score:\t\t'        + str(QueryScore))
#                        print('_'*line_len)
#                        print()
                    
                    writer.writerow([index,                                               
                                     input_address0,                  
                                     input_PostCode0, 
                                     '',                  
                                     QueryScore,                    
                                     fs_HouseNo,       
                                     fs_PostCode,  
                                     '',
                                     F_address,       
                                     F_postalCode,                  
                                     '',
                                     '',
                                     F_suburb,
                                     '',
                                     '',
                                     Latitude,
                                     Longitude
                                     ])
       
                    
                    file_line+=1
                    progress_bar = ('Completed:\t'+str( round( (file_line/shape_filter[0])*100 , 0) )+'%')
                    print(progress_bar)
#                    os.system('cls')
                if file_line == 0:
                    pass
                else:
                    print()
                    print()
                    print('_'*line_len)
                    print('[Process Completed]')
                    print()
                    print('\t\t\t#\t%')
                    print('Scanned:\t\t'      +str(file_line) +'\t' +str(round(file_line/file_line,0)*100)+'%')
                    print('Validated:\t\t'    +str(validated) +'\t' +str(round(validated/file_line,2)*100)+'%')
                    print('Failed\t\t\t'      +str(failed)    +'\t' +str(round(failed/file_line,2)*100)+'%')
                    print()
                    print()
                    print('Overal Confidence in results:\t'         +str(round(AccumQS/file_line,2)*100)+'%')
                    print()
                    print('_'*line_len)
                    print('Output saved to: '+output_file)
                    print('Please review output before copying it over to submission file')
                    print('_'*line_len)
        except PermissionError:
            print('Please close Output file!')         
    except XLRDError:
        print('No sheet sheet named:', sheet_name
              +'\n\n(Or) file is encrypted and password protected.'
              +'\nRemove password protection to proceed.')
    except FileNotFoundError:
        print('No file named:', input_file
              +'\nEnsure that file is in the same directory as this application')
    except ValueError:
        print('Index column is not found!\nEnsure that there is a column \"'+index_col+'\"')
        
def Afrikaans_to_English(input_address):
    '''
    Replaces afrikaans path types 
    
    Translations:
    http://resource.capetown.gov.za/documentcentre/Documents/Bylaws%20and%20policies/Street%20Naming%20and%20Numbering%20Policy%20-%20(Policy%20number%2021288)%20approved%20on%2025%20June%202014.pdf
    '''
    Dictionary = {
            'Arkade'    :   'Arcade',
            'Laan'      :   'Avenue',
            'Verbypad'  :   'Bypass',
            'Sirkel'    :   'Circle',
            'Slot'      :   'Close',
            'Hof'       :   'Court',
            'Singel'    :   'Crescent',
            'Sgl'       :   'Cres',
            'Rylaan'    :   'Drive',
            'Einde'     :   'End',
            'Snelweg'   :   'Expressway',
            'Deurpad'   :   'Freeway',
            'Laning'    :   'Grove',
            'Steeg'     :   'Lane',
            'Skakelpad' :   'Link',
            'Draai'     :   'Loop',
            'Wandellaan':   'Mall',
            'Parkweg'   :   'Parkway',
            'Voetpad'   :   'Path',
            'Kaai'      :   'Quay',
            'Weg'       :   'Road',
            'Plein'     :   'Square',
            'Pln'       :   'Sq',
            'Trappe'    :   'Steps',
            'Straat'    :   'Street',
            'Wandelpad' :   'Trail',
            
            'Plek'      :   'Place',
            'Terras'    :   'Terrace',   
            'Oord'      :   'Resort',
            'Wandelhal' :   'Walkway',
            }
            # 'Ln'        :   'Ave',
            # 'Str'       :   'St',
        
    for key in Dictionary:
        if key.lower() in input_address.lower():
            input_address = input_address.replace(key.lower(), Dictionary[key])
            input_address = re_sub('([A-Z][a-z]+)', r' \1', re_sub('([A-Z]+)', r' \1', input_address)).split()
            input_address = ' '.join([str(elem) for elem in input_address])      
            break
        else:
            pass
    return input_address

def SpecialChar_Remover(input_address):
    '''
    Removes special characters
    '''
    SpecialChar_list_1 = ['-']
    SpecialChar_list_2 = ['_', '+','.']
    
    for elem in SpecialChar_list_1:
        if elem in input_address:
            if input_address.count(elem) > 1:
                input_address = input_address.replace(elem, ' ')
            else:
                pass
        else:
            pass 
#    any(elem in input_address for elem in SpecialChar_list_2)
    for elem in SpecialChar_list_2:
        if elem in input_address:
            input_address = input_address.replace(elem, ' ')
        else:
            pass
    return input_address

def Separate_Address(input_address):
    '''
    Attempt separate address into its components 
    '''
    
    ## Postal code range
    lowest = 6500
    highest = 8099
    
 ## Split by comma
    list_1 = input_address.split(',')
    list_1 = list(dict.fromkeys(list_1))
    len_1 = len(list_1)  
    if len_1 == 1:
        ## Search for digits 
        if any(char.isdigit() for char in input_address) is True:
            ## Split by space
            list_2 = input_address.split(' ')
            len_2 = len(list_2)
            if len_2 == 1:
                Post_Code = None 
            else:
                for elem in list_2:
                    if elem.isdigit() is True:
                        ## Search for WC PostCode
                        if int(elem) >= lowest and int(elem) < highest:
                            ## Extract PostCode
                            Post_Code = elem 
                            ## Remove post. code 
                            input_address = input_address.replace(Post_Code,'')
                        else:
                            Post_Code = None 
                            # Finding dwelling no. is problematic
                    else:
                        Post_Code = None 
        else:
            Post_Code = None 
        return input_address, Post_Code, None 
    else:
        ## Extract Street
        street = list_1[0]
        ## Remove street from list 1
        list_1.remove(street)
        ## Search for WC PostCode
        for elem in list_1:
            if elem.replace(' ','').isdigit() is True:
                ## Search for WC PostCode
                if int(elem) >= lowest and int(elem) < highest:
                    ## Extract PostCode
                    Post_Code = elem.replace(' ','') 
                    ## Remove post. code 
                    input_address = input_address.replace(Post_Code,'')
                    list_1.remove(elem)
                    if len(list_1) == 0:
                        list_1 = None
                else:
                    Post_Code = None 
            else:
                Post_Code = None 
        return street, Post_Code, list_1

def Geocoder(street, input_PostCode, address_elem, input_file, file_ext, validated, failed, AccumQS, API_key):
    '''
    Parses address through geocoder
    Finds best result
    Writes results to file
    '''
    inCountry   = 'ZAF'  # ISO 3166-1 alpha-3 
    inState     = 'Western Cape'
    Items_limit = 5
    PCTolerance = 5
    STolerance  = 0.80
    
    str_ASCII   = street.replace(' ','+').replace(',','%2C') 
    
    base_url    = 'https://geocode.search.hereapi.com/v1/geocode'
    endpoint    = f'{base_url}?q={str_ASCII}&in=countryCode%3A{inCountry}&limit={Items_limit}&apiKey={API_key}'
    
    response    = requests_get(endpoint)
    result_json = response.json()
    try:
        if result_json['error_description'] == 'apiKey invalid. apiKey not found.':
            print('Incorrect API key entered'
                  +'\n\nIf you do not have a HERE API key please see instructions on how to obtain one')
            return False, False, False, False, False, False, validated, failed, AccumQS
    except KeyError:
        pass
    json_items  = result_json['items']
    
    ambiguity       = []
    PostCodeMatch   = []
    ElemMatch       = []
    hereID          = None 
    
    ## Assess total amiguity
    for item in json_items: 
        State = item['address']['state'].title() 
        if State == inState:
#            item_loads = json.loads(str(item).replace('\'','\"'))
#            item_dumps = json.dumps(item_loads, indent=2)
#            print(item_dumps)
            ambiguity.append(item['id'])
        else:
            pass
    if len(ambiguity) == 1:
        hereID = ambiguity[0] 
    else:
        ## Attempt to find postal code
        if input_PostCode is None:
            pass
        else:
            for item in json_items:  
                State = item['address']['state'].title()
                if State.title() == inState:
                    try:
                        if int(item['address']['postalCode']) in range(int(input_PostCode)-PCTolerance,int(input_PostCode)+PCTolerance):
                            PostCodeMatch.append(item['id'])
                    except KeyError:
                        pass
                else:
                    pass
        if len(PostCodeMatch) == 1:
            hereID = PostCodeMatch[0]
        else:
            ## Attempt to find other address elements
            if address_elem is None:
                for item in json_items:
                    State = item['address']['state'].title()
                    if State.title() == inState:
                        if item['address']['houseNumber'] in street and item['scoring']['queryScore'] >= 0.7:
                            ElemMatch.append(item['id'])
                        else:
                            pass
                    else:
                        pass
            else:
                for elem in address_elem:
                    elem = elem.rstrip().lstrip().title()
                    for item in json_items:
                        State = item['address']['state'].title()
                        if State.title() == inState:
                            try:
                                County  = item['address']['county']
                                City    = item['address']['city']
                                District= item['address']['district'] 
                                if City == elem or District == elem:
                                    ElemMatch.append(item['id'])
                                elif SequenceMatcher(None, City, elem).ratio() > STolerance or SequenceMatcher(None, District, elem).ratio() > STolerance:
                                    ElemMatch.append(item['id'])
                            except KeyError:
                                pass
                        else:
                            pass
            unique_ElemMatch = list(dict.fromkeys(ElemMatch))
            if len(unique_ElemMatch) == 1:
                hereID = ElemMatch[0]
            elif len(unique_ElemMatch) > 1:
                max_occur = max(set(ElemMatch), key = ElemMatch.count) # Weak soln., does not reccognise more than 1 max value
                hereID = max_occur
            elif len(unique_ElemMatch) == 0:
                pass
    if hereID is None:
        failed+=1
        return None, None, None, None, None, None, validated, failed, AccumQS, None, None 
    else:
        for item in json_items:
            if hereID == item['id']:
#                try:
#                    final_title                   = item['title']
#                except KeyError:
#                    final_title                   = ''  

                try:
                    final_county                  = item['address']['county']
                except KeyError:
                    final_county                  = ''
                    
                try:
                    final_city                    = item['address']['city']
                except KeyError:
                    final_city                    = ''
                    
                try:
                    final_district                = item['address']['district']
                except KeyError:
                    final_district                = ''
                    
                try:
                    final_street                  = item['address']['street']
                except KeyError:
                    final_street                  = ''
                    
                try:
                    final_postalCode              = item['address']['postalCode']
                except KeyError:
                    final_postalCode              = ''
                    
                try:
                    final_houseNumber             = item['address']['houseNumber']
                except KeyError:
                    final_houseNumber             = ''
                    
                try:
                    final_latitude                = item['position']['lat']
                except KeyError:
                    final_latitude                = ''
                    
                try:
                    final_longitude               = item['position']['lng']
                except KeyError:
                    final_longitude               = ''
                    
                try:
                    final_queryScore              = item['scoring']['queryScore']
                except KeyError:
                    final_queryScore              = ''
                    
#                try:
#                    final_fieldScore_city         = item['scoring']['fieldScore']['city']
#                except KeyError:
#                    final_fieldScore_city         = ''
#                    
#                try:
#                    final_fieldScore_district     = item['scoring']['fieldScore']['district']
#                except KeyError:
#                    final_fieldScore_district     = ''
                    
                try:
                    final_fieldScore_postalCode   = item['scoring']['fieldScore']['postalCode']
                except KeyError:
                    final_fieldScore_postalCode   = ''
                    
                try:
                    final_fieldScore_houseNumber  = item['scoring']['fieldScore']['houseNumber']
                except KeyError:
                    final_fieldScore_houseNumber  = ''
                    
                suburb = ''
                if final_district == '':
                    suburb = final_city
                elif final_district != '':
                    suburb = final_district
                else:
                    pass 
                
                Output_address = (final_houseNumber 
                                  + ' '
                                  + str(final_street)
                                  + ', '
                                  + suburb
                                  + ', '
                                  + final_county)
                validated+=1
                AccumQS+=final_queryScore
            
                return Output_address, suburb, final_postalCode, final_queryScore, final_fieldScore_houseNumber, final_fieldScore_postalCode, validated, failed, AccumQS, final_latitude, final_longitude 
            
            else:
                pass

def Initiate(API_key, input_file):
    time_start  = time.time()
    main(API_key, input_file)
    time_end    = time.time()
    elapsed     = time_end - time_start
    format_time = time.strftime("%H:%M:%S", time.gmtime(elapsed)) 
    print('\n\nTime taken:\t\t' + format_time)
                    
#if __name__ == '__main__':
#    time_start  = time.time()
#    main()
#    time_end    = time.time()
#    elapsed     = time_end - time_start
#    format_time = time.strftime("%H:%M:%S", time.gmtime(elapsed)) 
#    print('\n\nTime taken:\t\t' + format_time)
    
