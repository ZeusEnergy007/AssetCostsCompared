# AssetCostsCompared
Project Overview:  This project will examine the median cost of a U.S. home, comparing prices in U.S. Dollars to Bitcoin (BTC) over a ten-year period from 2014 to 2024. In a natural free-market state, prices tend to decline to their nominal cost of production, creating a deflationary trend. However, using an inflation-prone "fiat" currency like the U.S. Dollar can distort this dynamic. In contrast, Bitcoin, with its fixed supply, offers a stable alternative for measuring value. This analysis will present graphs that illustrate the inflated cost of a home in U.S. Dollars alongside the deflating cost of the same home measured in Bitcoin. (A comparison with gold may also be included.)

Technical Insight:  To gather data, I will use APIs and/or available datasets from sources like Zillow, Realtor.com, the U.S. Census Bureau, and CoinMarketCap, with additional sources as needed based on my research findings. I will organize the data in a structured table with rows representing each year from 2014 through 2024. The columns will include:

U.S. median home value (in dollars)
Median income (in dollars)
Cost of Living Index
Bitcoin value (in dollars)
Home value (in Bitcoin)
For visualization, I will use Matplotlib or potentially other Python libraries (Seaborn, Plotly?) to produce two main types of graphs:

Graph 1: Vertical bar clusters representing each year's data from 2014 to 2024. Each cluster will display HomeInDollars, IncomeInDollars, BitcoinInDollars, and HomeInBitcoin on the X-axis, with values on the Y-axis ranging from 0 to 500,000. This will visually contrast the nominal dollar value of a home with equivalent values in Bitcoin and income.

Graph 2: A line plot that tracks each of the four metrics—HomeInDollars, IncomeInDollars, BitcoinInDollars, and HomeInBitcoin—over time, with years from 2014 to 2024 on the X-axis and values (initially set from 0 to 500,000) on the Y-axis. Each line will provide a comparative view of the value trends.

Note: The initial Y-axis scale of 0 to 500,000 may be recalibrated as data is collected to best represent the trends.  I also expect to calculate/convert dollar values to Bitcoin before presentation.

Optional Visual Aids:  I've include a few images as I am attempting to work out how resprent graphs.  These are
NOT representative of my final product at this point.