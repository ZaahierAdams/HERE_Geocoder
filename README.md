# Here Geocoder 
Convert batch addresses in an Excel file to geographical coordinates. 

## How it works 
<img alt="SystemDesign" src="https://i.imgur.com/284LiT0.png"></img>

1. Extracts addresses from Excel file
2. Cleans addresses. 
    - *Also converts Afrikaans addresses* 
3. Parse addresses to Here geocoding API
4. Save geographical coordinates to new excel file

## Setting up 
- Requirements: [Python](https://www.python.org/downloads/), [Pandas](https://pypi.org/project/pandas/), [Requests](https://pypi.org/project/requests/), [xlrd](https://pypi.org/project/xlrd/), [Pillow](https://pypi.org/project/Pillow/)


- The ```.xlsx``` file containing the addresses should have the following column headers:
<img alt="ColumnHeaders" src="https://i.imgur.com/GW39Gqb.png" width="40%"></img>

- The results are confined to a specific region. You are required to do the following changes in ``` Backend.py```:
	- On lines 274 and 275, change ```lowest``` and ```highest```. This is the range of postal code addresses accepted:
  
```
  ## Postal code range
  lowest = 1000
  highest = 2000
```
- 
  - On lines 335 and 336, change ```inCountry``` and ```instate```. This confines results to particular state in a country. **Note:** ```inCountry``` should be  *ISO 3166-1 alpha-3* format. 

```
inCountry   = 'ZAF'  # ISO 3166-1 alpha-3 
inState     = 'Western Cape'
```

- For more information watch the video tutorial:

<div align="center">
      <a href="https://youtu.be/hGmhmutrjnU">
         <img 
          src="https://i.imgur.com/xVXfCIC.png" 
          alt="Geocoder" width="70%">
      </a>
</div>
    

## Acknowledgements 
[Here](https://developer.here.com/develop/rest-apis)

**Disclaimer:** I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with Here

