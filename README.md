# surfs_up

## Purpose

The purpose of the analysis was to explain the structures, interactions, and types of data of a provided dataset in SQLite, use SQLAlchemy to connect to and query a SQLite database, use statistics like minimum, maximum, and average to analyze data and design a Flask application.


## Results

As a result the temperature statistics was received for all Junes and Decembers within provided data.
Screenshots as follows:

June

![June_temp_stats](https://github.com/AlekseiPronin/surfs_up/blob/main/Resources/june_temp_stats.png)


December

![december_temp_stats](https://github.com/AlekseiPronin/surfs_up/blob/main/Resources/december_temp_stats.png)


The key differences between theese statistics are:

* The count for June temps is higher, which means the higher quantity of observations and therefore more presice data
* The standard deviation of December is higher than in June, which means that values are spread out over a wider range, so there is a bigger difference in temps for cooler and warmer days
* Even though quartiles and maximum temps are proportionally higher in June, the difference is not crucial, hovewer minimum temp in December is 8 degrees cooler than in June, which can result in fewer customers during this month


## Summary

The statistics for June and December provided some ideas about what to expect during these periods of time. 
Hovewer, additional queries can provide more information for better analysis. The good idea would be adding the info about precipitation for both periods.
It can be performed with the following code:

For June:
```
june_results = session.query(Measurement.date, Measurement.tobs, Measurement.prcp).filter(extract('month',Measurement.date)==6).all()
june_df = pd.DataFrame(june_results, columns=['date', 'temperature', 'precipitation'])
june_df.set_index(june_df['date'], inplace=True)
june_df.describe()
```

For December:
```
december_results = session.query(Measurement.date, Measurement.tobs, Measurement.prcp).filter(extract('month',Measurement.date)==12).all()
december_df = pd.DataFrame(december_results, columns=['date', 'temperature', 'precipitation'])
december_df.set_index(december_df['date'], inplace=True)
december_df.describe()
```
