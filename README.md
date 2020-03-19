# COVID19

I made this program just for practice. It originally used python and Google Spreadsheets API. I got data from: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html?fbclid=IwAR3S1IMXpzD-EfOPqWCDttt96vuDQ77Uddrqhhf-iTRmYKxyOPQlPhsxG14#/bda7594740fd40299423467b48e9ecf6, provided by JHU CSSE.

Now I am using data from github where they update it now once a day.
Link to [github repository with data](https://github.com/CSSEGISandData/COVID-19).

For previous version where I used Google Spreadsheets data go to [this directory](../previous_version_files).

**Things I have done:**
- [x] Did everything I needed to read data from Google Spreadsheets and used data to make some graphs **(look here: [previous_version_files/README.md](../previous_version_files/README.md))**.
- [x] Read data from github repository
- [x] Process data using **pandas**
- [x] Automated making graph with number of confirmed/deaths/recovered cases for China and Italy
- [x] Automated making figure with graphs of countries with most confirmed casese (without China and Italy)
- [x] Automated making graph for absolute growth in number of confirmed and deaths/recovered cases

## Technologies used:
- Python 3
- Jupyter Notebook
- pandas 
- matplotlib
- seaborn
- git


## Here are some graphs I made using **matplotlib**:

<h3>Time series data for China</h3>
<p align="center">
<img src="img/china.png" width="650" />
</p>

<h3>Time series data for Italy</h3>
<p align="center">
<img src="img/italy.png" width="650" />
</p>

The significant increase (about 15000 cases) in confirmed cases around 13th of February is caused by change in the definition of confirmed case.

<h3>Time series graph for other countries with biggest number of confirmed cases</h3>

<p align="center">
<img src="img/most_confirmed_cases.png">
</p>

<h3>Absolute growth</h3>
<p align="center">
<img src="img/abs_growth_confirmed.png" width="400" />
<img src="img/abs_growth_deaths_recovered.png" width="400" /> 
</p>
