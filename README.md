# Formula1-Data-Pipeline-Transformation-Databricks
Thrilled to share my latest project, where I took on the challenge of designing and orchestrating a data pipeline that transforms Formula 1 racing data into actionable insights using Databricks and Azure. 🚀
# Project Overview
This repository hosts the code and documentation for a comprehensive Data Pipeline Transformation project that leverages state-of-the-art technologies like Databricks, Azure, and PySpark to analyze historical Formula 1 race data. The project aims to ingest, transform, and visualize data to unearth insights into the performance of drivers and teams across decades of racing history.
# Data Source
The data is sourced from the Ergast Developer API,(http://ergast.com/mrd/) which provides extensive results from F1 races dating back to the 1950s. The API offers a rich set of tables, including race results, lap times, and more, which serve as the foundation for our analytical endeavors.
# Technologies Used
Databricks: For orchestrating the data transformation and analysis workflows.
Azure Data Lake Storage (ADLS): As the raw and processed data storage solution.
Azure Data Factory (ADF): For pipeline scheduling and monitoring.
PySpark: Utilized for data processing and transformation tasks.
Python: For creating helper functions and additional data manipulation.
# Pipeline Architecture
The pipeline follows a robust ETL (Extract, Transform, Load) process:

Ingest: Data is ingested from the Ergast API into the raw ADLS layer.
Transform: Data is processed and transformed into a structured format within Databricks.
Analyze: The transformed data is then analyzed to extract meaningful insights.
Report: Results are visualized using Databricks dashboards, primarily focusing on dominant drivers and teams.

Please refer to the Below picture for a detailed architecture diagram.
![data_pipeline](https://github.com/Revanthpotu/Formula1-Data-Pipeline-Transformation-Databricks/assets/64886845/5b2f5d18-698d-48ea-b258-45c142c0e52f)
# Results
## Dominant Divers
![dominant_drivers (1)](https://github.com/Revanthpotu/Formula1-Data-Pipeline-Transformation-Databricks/assets/64886845/3f5db3af-bdcc-4ddb-bbbe-61b1be1c219b)

## Dominant Teams
![dominant_teams (1)](https://github.com/Revanthpotu/Formula1-Data-Pipeline-Transformation-Databricks/assets/64886845/ca004cf3-7588-49a9-a6c7-d03932f2d1ae)




