# COVID19

I made this program just for practice. It originally used python and Google Spreadsheets API. I got data from: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html?fbclid=IwAR3S1IMXpzD-EfOPqWCDttt96vuDQ77Uddrqhhf-iTRmYKxyOPQlPhsxG14#/bda7594740fd40299423467b48e9ecf6, provided by JHU CSSE.

Now I am using data from github where they update it now once a day.
Link to [github repository with data](https://github.com/CSSEGISandData/COVID-19).

For previous version where I used Google Spreadsheets data go to [this directory](../previous_version_files).

(update 16.02.2020)
**Things I have done:**
- [x] Did everything I needed to read data from Google Spreadsheets and used data to make some graphs **(look here: [previous_version_files/README.md](../previous_version_files/README.md))**.
- [x] Read data from github repository
- [x] Process data using **pandas**
- [x] Automated making graph with number of confirmed/deaths/recovered cases for China
- [x] Automated making separete graphs for countries with number of confirmed cases over and under certain limit (see below) - made two separate figures with plots so that the values from the charts could be better read
- [x] Automated making graph for absolute growth in number of confirmed and deaths/recovered cases

## Technologies used:
- Python 3
- Jupyter Notebook
- pandas 
- matplotlib
- git


## Here are some graphs I made using **matplotlib**:

<h3>Time series data for China</h3>
<p align="center">
<img src="img/china.png" width="650" />
</p>

<h3>Time series data for Italy</h3>
<p align="center">
<<<<<<< HEAD
<img src="img/italy.png" width="650" />
=======
<img src="img/italy.png" width="475" />
>>>>>>> df3d37a8b8f4f1d89ff69a4fecc039af952fcc91
</p>

The significant increase (about 15000 cases) in confirmed cases around 13th of February is caused by change in the definition of confirmed case.

<h3>Time series graphs for some other countries</h3>

<p align="center">
<img src="img/between_1500_15000.png">
</p>

<h3>Absolute growth</h3>
<p align="center">
<img src="img/abs_growth_confirmed.png" width="400" />
<img src="img/abs_growth_deaths_recovered.png" width="400" /> 
</p>