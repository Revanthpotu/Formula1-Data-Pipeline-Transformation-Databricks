# Databricks notebook source
# MAGIC %md
# MAGIC ###In order to access data from ADLS GEN 2 storage account we need to provide one of the access keys to azure databricks so that it can authenticate to ADLS GEN 2
# MAGIC ####We can do this by assigning the access key to spark configuration called fs.azure.account.key
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 1. list files from container demo 
# MAGIC 1. read data from circuits.csv file
# MAGIC
# MAGIC

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

Seckey = dbutils.secrets.get(scope= 'projectformula1-scope', key='projectformula1-key')

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.projectformula1.dfs.core.windows.net",
    Seckey)

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

