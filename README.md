# sqlalchemy-challenge

### Climate Analysis and Exploration
Used Python and SQLAlchemy to do basic climate analysis and data exploration of climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib:

- Used SQLAlchemy create_engine to connect to sqlite database.
- Used SQLAlchemy automap_base() to reflect tables into classes and saved a reference to those classes called station and measurement.

### Precipitation Analysis
- Designed a query to retrieve the last year of precipitation data.
- Loaded the query results into a Pandas DataFrame and set the index to the date column and sorted by date.
- Plotted the results using the DataFrame plot method.

### Station Analysis
- Designed a query to calculate the total number of stations.
- Designed a query to find the most active stations.
- Listed the stations and observation counts in descending order.
- Designed a query to retrieve the last year of temperature observation data (TOBS).
- Filtered by the station with the highest number of observations.

