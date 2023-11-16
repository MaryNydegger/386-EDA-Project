# Car Data Compilation Project

### Project Goals
* The aim of this project is to compile datasets related to automobiles. This involves gathering information on car prices (MSRP - Manufacturer's Suggested Retail Price) and mapping each car brand to its respective country of origin.

### Question
* How does the country of origin influence car pricing and market preferences?

### Included Datasets
* *MSRP Dataset*: The MSRP dataset contains details of various car models, including pricing information and specifications. This dataset is crucial for understanding the suggested retail prices across different vehicle types. (Found at this website `https://www.kaggle.com/datasets/CooperUnion/cardataset`)

* *Car Brands - Country of Origin Dataset*: This dataset correlates car brands with their respective countries of origin. It provides insight into the global representation of different automotive manufacturers. (Found at this website `https://www.canstarblue.com.au/vehicles/car-country-of-origin/`)

### Running the Python Scripts
* *Data Scraping*:
* To retrieve the datasets, run the following Python scripts:
* `scrape_msrp.py`: Scrapes the MSRP data.
* `scrape_car_brands.py`: Extracts car brand details and their countries of origin. 
* *Data Cleaning and Compilation*:
* After scraping the data, clean and compile it using:
* `clean_data.py`: Cleans and merges the scraped datasets. This script adds the 'Country of Origin' column to the MSRP dataset based on the car brand information.

### Accessing the Datasets
* The compiled datasets can be accessed as CSV files:
* `msrp_data.csv`: Contains cleaned MSRP data with added 'Country of Origin' column.
* `car_brands_data.csv`: Provides details on car brands and their respective countries.




