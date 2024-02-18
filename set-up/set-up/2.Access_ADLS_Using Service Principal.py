# Databricks notebook source
# MAGIC %md
# MAGIC ###Create a Service Principal:
# MAGIC
# MAGIC In Azure, you can create a service principal either through the Azure portal, Azure CLI, or Azure PowerShell. This involves creating an application registration, which generates a client ID and client secret (or certificate), and associating it with a role or roles that grant access to the data lake
# MAGIC
# MAGIC ####We can do this by assigning the access key to spark configuration called fs.azure.account.key
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 1. list files from container demo 
# MAGIC 1. read data from circuits.csv file
# MAGIC
# MAGIC

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.projectformula1.dfs.core.windows.net",
    "XOI1vqxfIqmfvV8/TdZi9o1yWBbXolGzzM/agpzOa+6Va98Vg7h48tHJXZ/VgTO5AhjTr25GyT+7+ASthsYrIg=="
)

# COMMAND ----------

# MAGIC %md
# MAGIC - To reference the data from the storage account microsoft recommends the abfs(azure blob file system driver) driver to access data stored in storage account 

# COMMAND ----------

dbutils.fs.ls("abfss://demo@projectformula1.dfs.core.windows.net")

# COMMAND ----------

 display(dbutils.fs.ls("abfss://demo@projectformula1.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@projectformula1.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------

