# Parsing rip current forecasts
In an effort to measure whether there's been a change in high-risk rip currents off the coast of North Carolina, WRAL News examined 10 years of surf forecast reports from the National Weather Service from its Wilmington, N.C., office.

The analysis revealed that the state's southeastern beaches [have seen an uptick in higher-risk rip current forecasts over the last decade](https://wral.com/18502312).

## Methodology
Reporters downloaded surf report information on June 20, 2019, from [Iowa State University's Mesonet](https://mesonet.agron.iastate.edu/wx/afos), a repository of the weather products issued by the NWS.

The downloaded file [was in plain text format](https://github.com/mtdukes/rip-current-analysis/blob/master/afos-srfilm-20190620-20030515.txt). [A Python script](https://github.com/mtdukes/rip-current-analysis/blob/master/parseRips.py) using regular expressions parsed the file into [a comma-separated value file](https://github.com/mtdukes/rip-current-analysis/blob/master/rip_risk.csv), which could then be cleaned and analyzed in Excel. [The resulting Excel file](https://github.com/mtdukes/rip-current-analysis/blob/master/rip_risk_ilm.xlsx) contained more than 31,000 discrete forecasts for southeastern North Carolina and northeastern South Carolina beaches.

Analysis of the data focused only on "Today" forecasts and North Carolina beaches. These forecasts typically run from March or April through October.

For each month, the analysis counted the number of rip current forecasts that were either low risk or moderate/high risk. We then plotted the percentage of moderate/high risk forecasts out of the number of total forecasts for each month and ran analyzed the trend using a linear regression in Excel.

The analysis shows that from 2008 through early 2019, there's been a slight rise in the percentage of moderate- or high-risk forecasts for rip currents at these beaches overall. 

The R-value of the regression is 0.22, with a t-stat of 2.04 and P-value of 0.04.

## Get the data
* [Source forecast file (TXT)](https://github.com/mtdukes/rip-current-analysis/blob/master/afos-srfilm-20190620-20030515.txt)
* [Parsed output (CSV)](https://github.com/mtdukes/rip-current-analysis/blob/master/rip_risk.csv)
* [Cleaned file for analysis (Excel)](https://github.com/mtdukes/rip-current-analysis/blob/master/rip_risk_ilm.xlsx)

## Questions?
Contact WRAL investigative reporter [Tyler Dukes](https://www.wral.com/rs/bio/13311372/).